"""
demo.py - 한 사이클 자동 시연
터미널 두 개에서 dsp.py 를 각각 띄운 뒤 이 스크립트를 실행하세요.

  # 터미널 1
  python dsp.py --port 8001 --name "company-A"

  # 터미널 2
  python dsp.py --port 8002 --name "company-B"

  # 터미널 3
  python demo.py
"""

import httpx

A = "http://localhost:8001"
B = "http://localhost:8002"

print("=" * 50)
print("STEP 1. company-A: VC 발급")
vc_a = httpx.post(f"{A}/issue-vc", json={
    "participant_id": "did:web:company-A",
    "country": "DE",
    "membership_id": "company-A"
}).json()["vc_jwt"]
print(f"  VC (JWT): {vc_a[:60]}...")

print("\nSTEP 2. company-A: Asset 등록 (country=DE 만 허용)")
asset = httpx.post(f"{A}/assets", json={
    "name": "항로 기상 데이터",
    "data_url": "http://52.78.244.211/api/griddata?source=ecmwf&dataset_code=computed&model=ifs&variable=wind_dir_10m&run_time_utc=2025-07-01T00:00:00Z&step_hours=0&lat=35.0&lon=129.0&buffer_km=50.0",
    "policy": {"country": "DE"}
}).json()
print(f"  asset_id:  {asset['asset_id']}")
print(f"  policy_id: {asset['policy_id']}")

print("\nSTEP 3. company-B: VC 발급")
vc_b = httpx.post(f"{B}/issue-vc", json={
    "participant_id": "did:web:company-B",
    "country": "DE",
    "membership_id": "company-B"
}).json()["vc_jwt"]
print(f"  VC (JWT): {vc_b[:60]}...")

print("\nSTEP 4. company-B → company-A: 한 번에 catalog→negotiate→transfer")
result = httpx.post(f"{B}/fetch-from", json={
    "target_url": A,
    "my_vc_jwt":  vc_b,
    "my_id":      "did:web:company-B"
}, timeout=30).json()
print(f"  공급자:   {result['from']}")
print(f"  결과:     {result['result']}")

print("\nSTEP 5. 정책 위반 케이스 테스트 (country=KR)")
vc_kr = httpx.post(f"{A}/issue-vc", json={
    "participant_id": "did:web:company-C",
    "country": "KR",
    "membership_id": "company-C"
}).json()["vc_jwt"]

catalog_resp = httpx.get(f"{A}/catalog",
    headers={"Authorization": f"Bearer {vc_kr}"}
).json()
print(f"  조회된 오퍼 수: {len(catalog_resp['offers'])}  (0이면 정책 차단 정상)")

print("\n" + "=" * 50)
print("한 사이클 완료!")
