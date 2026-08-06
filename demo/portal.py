"""
Portal (Dataspace Participant) - MVP
하나의 앱을 포트만 다르게 두 번 띄우면 Portal-A <-> Portal-B 가 됩니다.

실행:
  pip install fastapi uvicorn pyjwt cryptography httpx
  python Portal.py --port 8001 --name "company-A"
  python Portal.py --port 8002 --name "company-B"
"""

import argparse
import uuid
import jwt
import httpx

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

from fastapi.middleware.cors import CORSMiddleware

# ── 키 로드 ──────────────────────────────────────────────────────────────────
with open("keys/issuer_private.pem") as f:
    PRIVATE_KEY = f.read()
with open("keys/issuer_public.pem") as f:
    PUBLIC_KEY = f.read()

# ── 포트 (argparse 전에 기본값, 실행 시 덮어씀) ──────────────────────────────
PARTICIPANT_PORT = 8001   # uvicorn 실행 포트와 동일하게 맞춰야 함

def self_url() -> str:
    """이 Portal 자신의 base URL을 반환합니다."""
    return f"http://localhost:{PARTICIPANT_PORT}"

def self_did() -> str:
    """did:web 형식의 자기 DID를 반환합니다. 포트 포함 시 %3A로 인코딩."""
    return f"did:web:localhost%3A{PARTICIPANT_PORT}"

# ── 인메모리 저장소 ───────────────────────────────────────────────────────────
service_offerings = {}   # service_offering_id -> service_offering dict
usage_policies    = {}   # usage_policy_id -> usage_policy dict
contracts         = {}   # contract_id -> {"service_offering_id", "consumer_id"}
negotiate_logs    = []   # 협상 이력 (최근 50건)

# ── FastAPI ───────────────────────────────────────────────────────────────────
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8001",
        "http://localhost:8002",
        "http://127.0.0.1:8001",
        "http://127.0.0.1:8002",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PARTICIPANT_ID = "unknown"  # argparse로 덮어씀


# ── UI 서빙 ───────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    """대시보드 HTML을 서빙합니다."""
    html_path = os.path.join(os.path.dirname(__file__), "dashboard.html")
    with open(html_path, encoding="utf-8") as f:
        return f.read()

@app.get("/participant")
def get_participant():
    return {"name": PARTICIPANT_ID}


# ── DID 문서 서빙 ─────────────────────────────────────────────────────────────
@app.get("/.well-known/did.json")
def get_did_document():
    """
    did:web resolve 엔드포인트.
    did:web:localhost%3A8001  →  GET http://localhost:8001/.well-known/did.json
    공개키를 JWK 형식으로 노출합니다.
    """
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    import base64
    import cryptography.hazmat.primitives.serialization as ser

    pub = ser.load_pem_public_key(PUBLIC_KEY.encode())
    # Ed25519 raw 32바이트 → base64url
    raw_bytes = pub.public_bytes(Encoding.Raw, PublicFormat.Raw)
    pub_b64 = base64.urlsafe_b64encode(raw_bytes).rstrip(b"=").decode()

    did = self_did()
    key_id = f"{did}#key-1"

    return {
        "@context": ["https://www.w3.org/ns/did/v1"],
        "id": did,
        "verificationMethod": [{
            "id": key_id,
            "type": "JsonWebKey2020",
            "controller": did,
            "publicKeyJwk": {
                "kty": "OKP",
                "crv": "Ed25519",
                "x": pub_b64,
            }
        }],
        "authentication": [key_id],
        "assertionMethod": [key_id],
    }


# ── VC 발급 ───────────────────────────────────────────────────────────────────
class VCRequest(BaseModel):
    participant_id: str   # e.g. "did:web:company-A"
    country: str          # e.g. "DE"
    membership_id: str    # e.g. "company-A"

@app.post("/issue-vc")
def issue_vc(req: VCRequest):
    """간단한 Membership VC를 JWT로 발급합니다."""
    issuer_did = self_did()
    payload = {
        "iss": issuer_did,
        "sub": req.participant_id,
        "vc": {
            "type": ["VerifiableCredential", "MembershipCredential"],
            "credentialSubject": {
                "id": req.participant_id,
                "membership": {
                    "country": req.country,
                    "membershipId": req.membership_id,
                }
            }
        }
    }
    token = jwt.encode(payload, PRIVATE_KEY, algorithm="EdDSA",
                       headers={"kid": f"{issuer_did}#key-1"})
    return {"vc_jwt": token}


# ── DID resolve 헬퍼 ─────────────────────────────────────────────────────────
def resolve_did_public_key(kid: str) -> str:
    """
    kid 예시: "did:web:localhost%3A8001#key-1"
    1. DID 부분만 추출  →  did:web:localhost%3A8001
    2. URL로 변환       →  http://localhost:8001/.well-known/did.json
    3. DID 문서에서 publicKeyJwk.x 꺼내서 PEM으로 변환 후 반환
    """
    import base64
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    from cryptography.hazmat.primitives import serialization

    # kid → did (fragment 제거)
    did = kid.split("#")[0]  # "did:web:localhost%3A8001"

    # did:web → URL 변환 (RFC 준수)
    # did:web:localhost%3A8001  →  http://localhost:8001/.well-known/did.json
    method_specific = did.removeprefix("did:web:")          # "localhost%3A8001"
    decoded = method_specific.replace("%3A", ":").replace("%2F", "/")
    did_url = f"http://{decoded}/.well-known/did.json"

    # DID 문서 fetch
    try:
        resp = httpx.get(did_url, timeout=10)
        resp.raise_for_status()
        did_doc = resp.json()
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"DID resolve 실패 ({did_url}): {e}")

    # verificationMethod에서 공개키 추출
    methods = did_doc.get("verificationMethod", [])
    target_id = kid
    jwk = None
    for m in methods:
        if m.get("id") == target_id:
            jwk = m.get("publicKeyJwk")
            break
    if not jwk:
        raise HTTPException(status_code=401, detail=f"kid '{kid}' 에 해당하는 키 없음")

    # JWK(x: base64url) → Ed25519PublicKey → PEM
    x_bytes = base64.urlsafe_b64decode(jwk["x"] + "==")
    pub_key = Ed25519PublicKey.from_public_bytes(x_bytes)
    pem = pub_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    return pem


# ── VC 검증 헬퍼 ──────────────────────────────────────────────────────────────
def verify_vc(vc_jwt: str) -> dict:
    """
    1. JWT header의 kid 추출
    2. kid로 DID resolve → 공개키 PEM 획득
    3. 공개키로 서명 검증
    4. membership 클레임 반환
    """
    try:
        header = jwt.get_unverified_header(vc_jwt)
        kid = header.get("kid")
        if not kid:
            raise ValueError("JWT header에 kid 없음")

        public_key_pem = resolve_did_public_key(kid)

        decoded = jwt.decode(vc_jwt, public_key_pem, algorithms=["EdDSA"],
                             options={"verify_exp": False})
        return decoded["vc"]["credentialSubject"]["membership"]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"VC 검증 실패: {e}")


# ── Service Offering 등록 ─────────────────────────────────────────────────────
class ServiceOfferingRequest(BaseModel):
    name: str
    data_url: str         # 실제 데이터 위치 (다른 Portal에는 숨김)
    usage_policy: dict    # e.g. {"country": "DE"}

@app.post("/service-offerings")
def register_service_offering(req: ServiceOfferingRequest):
    service_offering_id = str(uuid.uuid4())
    usage_policy_id     = str(uuid.uuid4())
    service_offerings[service_offering_id] = {"name": req.name, "data_url": req.data_url}
    usage_policies[usage_policy_id] = {"service_offering_id": service_offering_id, "rules": req.usage_policy}
    return {"service_offering_id": service_offering_id, "usage_policy_id": usage_policy_id}


# ── Catalog 조회 ──────────────────────────────────────────────────────────────
@app.get("/catalog")
def get_catalog(authorization: str = Header(...)):
    """
    Authorization: Bearer <vc_jwt>
    VC를 검증하고 모든 Service Offering을 반환합니다.
    Usage Policy 조건 검증은 Negotiate 단계에서 수행합니다.
    """
    vc_jwt = authorization.removeprefix("Bearer ")
    verify_vc(vc_jwt)  # VC 서명만 확인, country 필터링은 하지 않음

    result = []
    for usage_policy_id, usage_policy in usage_policies.items():
        service_offering = service_offerings.get(usage_policy["service_offering_id"], {})
        rules = usage_policy["rules"]

        result.append({
            "service_offering_id": usage_policy_id,
            "name":                service_offering.get("name"),
            "usage_policy":        rules,
        })

    return {"participant": PARTICIPANT_ID, "service_offerings": result}


# ── 계약 협상 ─────────────────────────────────────────────────────────────────
class NegotiateRequest(BaseModel):
    service_offering_id: str
    consumer_id: str

@app.post("/negotiate")
def negotiate(req: NegotiateRequest, authorization: str = Header(...)):
    """Verify VC + re-validate Usage Policy, then issue a Contract ID."""
    import datetime

    vc_jwt = authorization.removeprefix("Bearer ")
    trace = []

    # Step 1: VC signature verification
    try:
        claims = verify_vc(vc_jwt)
        trace.append({
            "step": 1,
            "name": "VC Signature Verification",
            "status": "success",
            "detail": f"consumer_id={req.consumer_id} | issuer DID signature verified"
        })
    except HTTPException as e:
        trace.append({"step": 1, "name": "VC Signature Verification", "status": "fail", "detail": str(e.detail)})
        _save_log(req.consumer_id, trace, "fail")
        raise

    # Step 2: Service Offering lookup
    usage_policy = usage_policies.get(req.service_offering_id)
    if not usage_policy:
        trace.append({"step": 2, "name": "Service Offering Lookup", "status": "fail",
                      "detail": f"service_offering_id={req.service_offering_id} not found"})
        _save_log(req.consumer_id, trace, "fail")
        raise HTTPException(status_code=404, detail="Service Offering not found")

    service_offering = service_offerings.get(usage_policy["service_offering_id"], {})
    trace.append({
        "step": 2,
        "name": "Service Offering Lookup",
        "status": "success",
        "detail": f"name={service_offering.get('name')} | id={req.service_offering_id[:8]}…"
    })

    # Step 3: Usage Policy country validation
    rules = usage_policy["rules"]
    consumer_country = claims.get("country", "(none)")
    policy_country   = rules.get("country", "(unrestricted)")

    if "country" in rules and consumer_country != rules["country"]:
        trace.append({
            "step": 3,
            "name": "Usage Policy Check — country",
            "status": "fail",
            "detail": f"consumer country={consumer_country} | policy requires country={policy_country} → mismatch"
        })
        _save_log(req.consumer_id, trace, "fail")
        raise HTTPException(status_code=403, detail="Usage Policy condition not satisfied")

    trace.append({
        "step": 3,
        "name": "Usage Policy Check — country",
        "status": "success",
        "detail": f"consumer country={consumer_country} | policy requires country={policy_country} → match"
    })

    # Step 4: Contract issuance
    contract_id = str(uuid.uuid4())
    contracts[contract_id] = {
        "service_offering_id": usage_policy["service_offering_id"],
        "consumer_id":         req.consumer_id,
    }
    trace.append({
        "step": 4,
        "name": "Contract Issuance",
        "status": "success",
        "detail": f"contract_id={contract_id[:8]}… issued successfully"
    })

    _save_log(req.consumer_id, trace, "success")
    return {"contract_id": contract_id, "negotiation_trace": trace}


def _save_log(consumer_id: str, trace: list, overall: str):
    import datetime
    negotiate_logs.append({
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "consumer_id": consumer_id,
        "overall": overall,
        "trace": trace,
    })
    if len(negotiate_logs) > 50:
        negotiate_logs.pop(0)


@app.get("/negotiate-log")
def get_negotiate_log():
    """최근 협상 이력을 반환합니다."""
    return {"participant": PARTICIPANT_ID, "logs": list(reversed(negotiate_logs))}


# ── 데이터 전송 ───────────────────────────────────────────────────────────────
class TransferRequest(BaseModel):
    contract_id: str
    consumer_id: str

@app.post("/transfer")
def transfer(req: TransferRequest):
    contract = contracts.get(req.contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract 없음")
    if contract["consumer_id"] != req.consumer_id:
        raise HTTPException(status_code=403, detail="consumer_id 불일치")

    service_offering = service_offerings[contract["service_offering_id"]]

    # 실제 API 호출
    actual_data = httpx.get(service_offering["data_url"], timeout=30).json()
    return {
        "status": "transferred",
        "data": actual_data,
        "message": f"'{service_offering['name']}' Data transfer completed.",
    }

# ── Consumer 역할: 상대 Portal에서 데이터 가져오기 ───────────────────────────────
class FetchRequest(BaseModel):
    target_url: str    # 상대 Portal 주소, e.g. "http://localhost:8001"
    my_vc_jwt: str     # 내 VC (issue-vc로 미리 발급받은 것)
    my_id: str         # e.g. "did:web:company-B"

@app.post("/fetch-from")
def fetch_from(req: FetchRequest):
    headers = {"Authorization": f"Bearer {req.my_vc_jwt}"}

    # 1) Catalog 조회
    catalog = httpx.get(f"{req.target_url}/catalog", headers=headers, timeout=30).json()
    offerings = catalog.get("service_offerings", [])
    if not offerings:
        raise HTTPException(status_code=404, detail="이용 가능한 Service Offering 없음")
    service_offering_id = offerings[0]["service_offering_id"]

    # 2) 계약 협상
    neg = httpx.post(f"{req.target_url}/negotiate", headers=headers, json={
        "service_offering_id": service_offering_id, "consumer_id": req.my_id
    }, timeout=30).json()
    contract_id = neg["contract_id"]

    # 3) 데이터 전송 요청
    result = httpx.post(f"{req.target_url}/transfer", json={
        "contract_id": contract_id, "consumer_id": req.my_id
    }, timeout=30).json()

    return {"from": catalog["participant"], "result": result}


# ── 실행 ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8001)
    parser.add_argument("--name", type=str, default="Portal-participant")
    args = parser.parse_args()

    PARTICIPANT_ID   = args.name
    PARTICIPANT_PORT = args.port
    uvicorn.run(app, host="localhost", port=args.port)