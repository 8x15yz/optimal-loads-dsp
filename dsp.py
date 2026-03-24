"""
DSP (Dataspace Participant) - MVP
하나의 앱을 포트만 다르게 두 번 띄우면 DSP-A <-> DSP-B 가 됩니다.

실행:
  pip install fastapi uvicorn pyjwt cryptography httpx
  python dsp.py --port 8001 --name "company-A"
  python dsp.py --port 8002 --name "company-B"
"""

import argparse
import uuid
import jwt
import httpx

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

# ── 키 로드 ──────────────────────────────────────────────────────────────────
with open("keys/issuer_private.pem") as f:
    PRIVATE_KEY = f.read()
with open("keys/issuer_public.pem") as f:
    PUBLIC_KEY = f.read()

# ── 인메모리 저장소 ───────────────────────────────────────────────────────────
assets    = {}   # asset_id -> asset dict
policies  = {}   # policy_id -> policy dict
contracts = {}   # contract_id -> {"asset_id", "consumer_id"}

# ── FastAPI ───────────────────────────────────────────────────────────────────
app = FastAPI()
PARTICIPANT_ID = "unknown"  # argparse로 덮어씀


# ── VC 발급 ───────────────────────────────────────────────────────────────────
class VCRequest(BaseModel):
    participant_id: str   # e.g. "did:web:company-A"
    country: str          # e.g. "DE"
    membership_id: str    # e.g. "company-A"

@app.post("/issue-vc")
def issue_vc(req: VCRequest):
    """간단한 Membership VC를 JWT로 발급합니다."""
    payload = {
        "iss": "did:web:issuer",
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
                       headers={"kid": "did:web:issuer#key-1"})
    return {"vc_jwt": token}


# ── VC 검증 헬퍼 ──────────────────────────────────────────────────────────────
def verify_vc(vc_jwt: str) -> dict:
    """JWT 서명 검증 후 membership 클레임을 반환합니다."""
    try:
        decoded = jwt.decode(vc_jwt, PUBLIC_KEY, algorithms=["EdDSA"],
                             options={"verify_exp": False})
        return decoded["vc"]["credentialSubject"]["membership"]
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"VC 검증 실패: {e}")


# ── Asset 등록 ────────────────────────────────────────────────────────────────
class AssetRequest(BaseModel):
    name: str
    data_url: str         # 실제 데이터 위치 (다른 DSP에는 숨김)
    policy: dict          # e.g. {"country": "DE"}

@app.post("/assets")
def register_asset(req: AssetRequest):
    asset_id  = str(uuid.uuid4())
    policy_id = str(uuid.uuid4())
    assets[asset_id]   = {"name": req.name, "data_url": req.data_url}
    policies[policy_id] = {"asset_id": asset_id, "rules": req.policy}
    return {"asset_id": asset_id, "policy_id": policy_id}


# ── Catalog 조회 ──────────────────────────────────────────────────────────────
@app.get("/catalog")
def get_catalog(authorization: str = Header(...)):
    """
    Authorization: Bearer <vc_jwt>
    VC 검증 후, 정책 조건에 맞는 오퍼만 반환합니다.
    """
    vc_jwt = authorization.removeprefix("Bearer ")
    claims = verify_vc(vc_jwt)

    offers = []
    for policy_id, policy in policies.items():
        asset = assets.get(policy["asset_id"], {})
        rules = policy["rules"]

        # 정책 평가: country 조건만 체크 (MVP)
        if "country" in rules and claims.get("country") != rules["country"]:
            continue

        offers.append({
            "offer_id":  policy_id,
            "asset_name": asset.get("name"),
            "policy":    rules,
        })

    return {"participant": PARTICIPANT_ID, "offers": offers}


# ── 계약 협상 ─────────────────────────────────────────────────────────────────
class NegotiateRequest(BaseModel):
    offer_id: str
    consumer_id: str

@app.post("/negotiate")
def negotiate(req: NegotiateRequest, authorization: str = Header(...)):
    """VC 검증 + 정책 재확인 후 계약 ID를 발급합니다."""
    vc_jwt = authorization.removeprefix("Bearer ")
    claims = verify_vc(vc_jwt)

    policy = policies.get(req.offer_id)
    if not policy:
        raise HTTPException(status_code=404, detail="오퍼 없음")

    rules = policy["rules"]
    if "country" in rules and claims.get("country") != rules["country"]:
        raise HTTPException(status_code=403, detail="정책 조건 불일치")

    contract_id = str(uuid.uuid4())
    contracts[contract_id] = {
        "asset_id":    policy["asset_id"],
        "consumer_id": req.consumer_id,
    }
    return {"contract_id": contract_id}


# ── 데이터 전송 ───────────────────────────────────────────────────────────────
class TransferRequest(BaseModel):
    contract_id: str
    consumer_id: str

@app.post("/transfer")
def transfer(req: TransferRequest):
    contract = contracts.get(req.contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="계약 없음")
    if contract["consumer_id"] != req.consumer_id:
        raise HTTPException(status_code=403, detail="consumer_id 불일치")

    asset = assets[contract["asset_id"]]
    
    # 실제 API 호출
    actual_data = httpx.get(asset["data_url"], timeout=30).json()
    return {
        "status": "transferred",
        "data": actual_data,
        "message": f"'{asset['name']}' 데이터 전송 완료",
    }

# ── Consumer 역할: 상대 DSP에서 데이터 가져오기 ───────────────────────────────
class FetchRequest(BaseModel):
    target_url: str    # 상대 DSP 주소, e.g. "http://localhost:8001"
    my_vc_jwt: str     # 내 VC (issue-vc로 미리 발급받은 것)
    my_id: str         # e.g. "did:web:company-B"

@app.post("/fetch-from")
def fetch_from(req: FetchRequest):
    headers = {"Authorization": f"Bearer {req.my_vc_jwt}"}

    # 1) Catalog 조회
    catalog = httpx.get(f"{req.target_url}/catalog", headers=headers, timeout=30).json()
    offers  = catalog.get("offers", [])
    if not offers:
        raise HTTPException(status_code=404, detail="이용 가능한 오퍼 없음")
    offer_id = offers[0]["offer_id"]

    # 2) 협상
    neg = httpx.post(f"{req.target_url}/negotiate", headers=headers, json={
        "offer_id": offer_id, "consumer_id": req.my_id
    }, timeout=30).json()
    contract_id = neg["contract_id"]

    # 3) 전송 요청
    result = httpx.post(f"{req.target_url}/transfer", json={
        "contract_id": contract_id, "consumer_id": req.my_id
    }, timeout=30).json()

    return {"from": catalog["participant"], "result": result}


# ── 실행 ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8001)
    parser.add_argument("--name", type=str, default="dsp-participant")
    args = parser.parse_args()

    PARTICIPANT_ID = args.name
    uvicorn.run(app, host="0.0.0.0", port=args.port)
