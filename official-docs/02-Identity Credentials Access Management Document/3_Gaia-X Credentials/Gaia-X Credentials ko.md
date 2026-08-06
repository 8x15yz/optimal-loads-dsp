# 5. Gaia-X 자격증명(Gaia-X Credentials)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#gaia-x-credentials "Permanent link")

## 5.1 개요[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#overview "Permanent link")

이 장에서는 W3C VC 데이터 모델 2.0을 준수하여 Gaia-X 신뢰 프레임워크(trust framework) 내에서 검증 가능한 자격증명(Verifiable Credential, VC)을 어떻게 모델링하고, 구조화하며, 활용하는지를 정의합니다. 또한 Gaia-X 규격 자격증명의 발급 및 검증을 위한 인코딩 방식, 필수 속성, 처리 규칙을 상세히 설명합니다. 이 장의 목표는 Gaia-X 에코시스템(ecosystem) 참여자 간의 의미론적 일관성과 기술적 상호운용성(interoperability)을 보장하는 것입니다.

## 5.2 핵심 데이터 모델 기반[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#core-data-model-foundations "Permanent link")

### 5.2.1 네임스페이스 바인딩과 컨텍스트[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#namespace-bindings-and-contexts "Permanent link")

Gaia-X 자격증명은 자격증명/프레젠테이션 표현의 일부로 JSON-LD 컨텍스트와 네임스페이스 바인딩을 사용합니다(예: `@context`를 통해).

검증 가능한 프레젠테이션(Verifiable Presentation) 수준과 그 안에 포함된 검증 가능한 자격증명(Verifiable Credential) 수준 모두에서, Gaia-X 자격증명은 검증 가능한 자격증명 데이터 모델의 어휘(vocabulary), 즉 `https://www.w3.org/2018/credentials#` 네임스페이스의 용어를 사용해야 합니다(MUST).

Gaia-X 자격증명을 직접 작성하는 사람이 이 용어들을 편리하게 표기할 수 있도록, 검증 가능한 프레젠테이션 수준에서 `@context` 키워드를 사용하여 다음 방법 중 하나를 선택할 수 있습니다(MAY):

- 초기 예시에서처럼 검증 가능한 자격증명 데이터 모델이 제공하는 [JSON-LD 컨텍스트](https://www.w3.org/TR/json-ld11/#the-context)(https://www.w3.org/ns/credentials/v2)를 참조하거나,
- 다음 조건 중 하나를 만족하는 자체 컨텍스트를 정의합니다:
- `@vocab` 키워드를 사용하여 위 네임스페이스를 기본 어휘로 정의하거나,
- 위 네임스페이스를 지정된 접두사(예: `"cred"`)로 매핑합니다.

마찬가지로, 자격증명 주체(credential subject)에 관한 클레임(claim)은 [Gaia-X 온톨로지(Gaia-X Ontology)](https://w3id.org/gaia-x/)에 게시된 Gaia-X 자격증명 스키마의 어휘를 반드시 따라야 합니다(MUST).

### 5.2.2 식별자[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers "Permanent link")

`@id`는 특정 `issuer`(발급자)에 대해 존재해야 하며 고유해야 합니다(MUST).

`@id` 키워드는 `id`로 별칭(alias) 지정할 수 있습니다(이 별칭 또한 사용 가능합니다).

`@id`가 해석 가능한 [URL](https://url.spec.whatwg.org/)인지 여부는 `issuer`(발급자)가 결정합니다.

다음 각 항목은 서로 다른 식별자를 가져야 합니다(MUST):

- 검증 가능한 프레젠테이션(Verifiable Presentation)
- 검증 가능한 프레젠테이션 내부의 검증 가능한 자격증명(Verifiable Credential)
- 검증 가능한 자격증명의 주체(subject), 즉 클레임이 서술하는 개념 모델 엔티티

Gaia-X 자격증명은 다른 Gaia-X 자격증명을 참조할 수 있습니다(MAY). 예를 들어, *서비스 오퍼링(ServiceOffering)*이 다음과 같은 경우를 생각해볼 수 있습니다:

- *프로바이더(Provider)*가 제공하거나,
- 다른 *서비스 오퍼링*들의 조합이거나,
- *리소스(Resource)*의 집합으로 구성된 경우.

### 5.2.3 타입 속성[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#type-property "Permanent link")

`@type` 속성은 검증 가능한 프레젠테이션과 검증 가능한 자격증명 모두에 반드시 존재해야 합니다(MUST).
첫 번째 `@type` 속성의 예상 값은 다음과 같습니다:

- 검증 가능한 프레젠테이션의 경우: `"VerifiablePresentation"`
- VC-JWT로 인코딩된 봉투형 검증 가능한 프레젠테이션의 경우: `"EnvelopedVerifiablePresentation"`
- 검증 가능한 자격증명의 경우: `"VerifiableCredential"`
- VC-JWT로 인코딩된 봉투형 검증 가능한 자격증명의 경우: `"EnvelopedVerifiableCredential"`

이 `@type`에는 자격증명 관련 타입이 하나 이상 추가될 수 있습니다(예: `@type: ['Verifiable Credential', 'gx:LegalPerson']`).

`@type` 키워드는 `type`으로 별칭 지정할 수 있습니다(이 별칭 또한 사용 가능합니다).

자격증명 주체의 `@type` 속성에 대한 예상 값은 [Gaia-X 온톨로지](https://w3id.org/gaia-x/)에 정의된 클래스 분류 체계에 따르며, 상위 클래스로 `Participant`(참여자), `ServiceOffering`(서비스 오퍼링), `Resource`(리소스)를 가집니다.

에코시스템은 레지스트리(Registry)에 추가적인 형태(shape)를 정의하고 호스팅하여 이들의 하위 클래스를 추가로 정의할 수 있습니다(MAY).

향후 Gaia-X 및 기타 에코시스템은 더 구체적인 자격증명 타입을 추가로 정의할 수 있습니다.

자격증명 주체에 관한 클레임의 어휘로 사용되는 Gaia-X 자격증명의 형태(shape)는 Gaia-X 레지스트리 또는 연합체(Federation) 카탈로그에 SHACL 형태([W3C SHACL(Shapes Constraint Language)](https://www.w3.org/TR/shacl/) 참조)로 반드시 제공되어야 합니다(MUST).  
Gaia-X 자격증명이 생성되거나 수신되는 시점에는 일정한 SHACL 형태 집합이 알려져 있으며, 이것이 *형태 그래프(shapes graph)*를 형성합니다.  
Gaia-X 자격증명은 *데이터 그래프(data graph)*를 구성합니다. Gaia-X 및/또는 다른 에코시스템 규격 준수를 위해 이 *데이터 그래프*는 [SHACL 명세](https://www.w3.org/TR/shacl/#validation-definition)에 따라 지정된 *형태 그래프*를 대상으로 검증되어야 합니다(MUST).

## 5.3 자격증명 포맷 명세[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-format-specification "Permanent link")

**Gaia-X 자격증명**은 [W3C 검증 가능한 자격증명 데이터 모델 2.0](https://www.w3.org/TR/vc-data-model-2.0/)을 준수하며, Gaia-X 레지스트리를 통해 제공되는 Gaia-X 온톨로지를 사용합니다.

### 5.3.1 인코딩 요구사항[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#encoding-requirements "Permanent link")

Gaia-X는 VC-JWT를 통한 자격증명 인코딩을 의무화하며, JSON 웹 서명(JSON Web Signature, JWS)을 사용하여 암호화 증명을 구성함으로써 페이로드(payload), 헤더(header), 서명(signature)의 진위성과 무결성을 검증할 수 있습니다.

아래는 JSON 문서의 기본 형태(예: document.json)와 이를 JOSE 기반 서명(및 선택적 암호화)을 통해 VC-JWT로 인코딩하는 방법을 보여주는 예시입니다. 이는 일반 JSON 검증 가능한 자격증명이 VC-JWT/JOSE/COSE 프레임워크 하에서 암호화적으로 검증 가능한 형태로 변환되는 과정을 설명합니다.

검증 가능한 자격증명 예시

| document.json | |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` {   "@context": [     "https://www.w3.org/ns/credentials/v2",     "https://w3id.org/gaia-x/development#"   ],   "@type": [     "VerifiableCredential",     "LegalPerson"   ],   "@id": "https://example.org/legal-participant/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",   "issuer": "did:web:example.org",   "validFrom": "2024-01-01T12:26:22.601516+00:00",   "validUntil": "2024-04-01T12:26:22.601516+00:00",   "credentialSubject": {     "id": "https://example.org/legal-participant-json/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",     "type": "gx:LegalPerson",     "gx:legalName": "Example Org",     "gx:legalRegistrationNumber": {       "id": "https://example.org/gaiax-legal-registration-number/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json"     },     "gx:headquarterAddress": {       "gx:countrySubdivisionCode": "FR-75"     },     "gx:legalAddress": {       "gx:countrySubdivisionCode": "FR-75"     }   } } ``` |

[VC-JWT 명세](https://www.w3.org/TR/vc-jose-cose/#securing-json-ld-verifiable-credentials-with-jose)를 사용하여 인코딩하면 다음과 같은 검증 가능한 자격증명이 생성됩니다:

```
eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA
```

이 VC-JWT는 [JWT.io 디버거](https://jwt.io/#debugger-io?token=eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb\_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE\_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA) 등의 도구를 통해 분석하고 검증할 수 있습니다.
아래의 개인 키와 공개 키 쌍은 이 VC-JWT 예시 및 **이후 장의 모든 예시**에 서명하는 데 사용되었습니다.
이 키 쌍의 ID는 `did:web:example.org#JWK-RSA`이며, 아래 예시 JWT의 `kid` 헤더 클레임에서 확인할 수 있습니다.

```
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC7VJTUt9Us8cKj
MzEfYyjiWA4R4/M2bS1GB4t7NXp98C3SC6dVMvDuictGeurT8jNbvJZHtCSuYEvu
NMoSfm76oqFvAp8Gy0iz5sxjZmSnXyCdPEovGhLa0VzMaQ8s+CLOyS56YyCFGeJZ
qgtzJ6GR3eqoYSW9b9UMvkBpZODSctWSNGj3P7jRFDO5VoTwCQAWbFnOjDfH5Ulg
p2PKSQnSJP3AJLQNFNe7br1XbrhV//eO+t51mIpGSDCUv3E0DDFcWDTH9cXDTTlR
ZVEiR2BwpZOOkE/Z0/BVnhZYL71oZV34bKfWjQIt6V/isSMahdsAASACp4ZTGtwi
VuNd9tybAgMBAAECggEBAKTmjaS6tkK8BlPXClTQ2vpz/N6uxDeS35mXpqasqskV
laAidgg/sWqpjXDbXr93otIMLlWsM+X0CqMDgSXKejLS2jx4GDjI1ZTXg++0AMJ8
sJ74pWzVDOfmCEQ/7wXs3+cbnXhKriO8Z036q92Qc1+N87SI38nkGa0ABH9CN83H
mQqt4fB7UdHzuIRe/me2PGhIq5ZBzj6h3BpoPGzEP+x3l9YmK8t/1cN0pqI+dQwY
dgfGjackLu/2qH80MCF7IyQaseZUOJyKrCLtSD/Iixv/hzDEUPfOCjFDgTpzf3cw
ta8+oE4wHCo1iI1/4TlPkwmXx4qSXtmw4aQPz7IDQvECgYEA8KNThCO2gsC2I9PQ
DM/8Cw0O983WCDY+oi+7JPiNAJwv5DYBqEZB1QYdj06YD16XlC/HAZMsMku1na2T
N0driwenQQWzoev3g2S7gRDoS/FCJSI3jJ+kjgtaA7Qmzlgk1TxODN+G1H91HW7t
0l7VnL27IWyYo2qRRK3jzxqUiPUCgYEAx0oQs2reBQGMVZnApD1jeq7n4MvNLcPv
t8b/eU9iUv6Y4Mj0Suo/AU8lYZXm8ubbqAlwz2VSVunD2tOplHyMUrtCtObAfVDU
AhCndKaA9gApgfb3xw1IKbuQ1u4IF1FJl3VtumfQn//LiH1B3rXhcdyo3/vIttEk
48RakUKClU8CgYEAzV7W3COOlDDcQd935DdtKBFRAPRPAlspQUnzMi5eSHMD/ISL
DY5IiQHbIH83D4bvXq0X7qQoSBSNP7Dvv3HYuqMhf0DaegrlBuJllFVVq9qPVRnK
xt1Il2HgxOBvbhOT+9in1BzA+YJ99UzC85O0Qz06A+CmtHEy4aZ2kj5hHjECgYEA
mNS4+A8Fkss8Js1RieK2LniBxMgmYml3pfVLKGnzmng7H2+cwPLhPIzIuwytXywh
2bzbsYEfYx3EoEVgMEpPhoarQnYPukrJO4gwE2o5Te6T5mJSZGlQJQj9q4ZB2Dfz
et6INsK0oG8XVGXSpQvQh3RUYekCZQkBBFcpqWpbIEsCgYAnM3DQf3FJoSnXaMhr
VBIovic5l0xFkEHskAjFTevO86Fsz1C2aSeRKSqGFoOQ0tmJzBEs1R6KqnHInicD
TQrKhArgLXX4v3CddjfTRJkFWDbE/CkvKZNOrcf1nhaGCPspRJj2KUkj1Fhl9Cnc
dn/RsYEONbwQSjIfMPkvxF+8HQ==
-----END PRIVATE KEY-----

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu1SU1LfVLPHCozMxH2Mo
4lgOEePzNm0tRgeLezV6ffAt0gunVTLw7onLRnrq0/IzW7yWR7QkrmBL7jTKEn5u
+qKhbwKfBstIs+bMY2Zkp18gnTxKLxoS2tFczGkPLPgizskuemMghRniWaoLcyeh
kd3qqGElvW/VDL5AaWTg0nLVkjRo9z+40RQzuVaE8AkAFmxZzow3x+VJYKdjykkJ
0iT9wCS0DRTXu269V264Vf/3jvredZiKRkgwlL9xNAwxXFg0x/XFw005UWVRIkdg
cKWTjpBP2dPwVZ4WWC+9aGVd+Gyn1o0CLelf4rEjGoXbAAEgAqeGUxrcIlbjXfbc
mwIDAQAB
-----END PUBLIC KEY-----
```

### 5.3.2 자격증명 구조[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-structure "Permanent link")

#### 5.3.2.1 헤더[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#header "Permanent link")

VC-JWT 헤더는 다음 필드를 반드시 포함해야 합니다(MUST):

- `alg`: 서명 알고리즘 (예: `PS256`)
- `typ`: JWT 미디어 타입으로 반드시 `vc+jwt`로 설정해야 합니다(MUST)
- `cty`: 페이로드 콘텐츠 타입으로 반드시 `vc`로 설정해야 합니다(MUST)
- `kid`: `did:web` 또는 [DID 문서 내 검증 메서드](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#json-web-key)에 대한 URL 참조를 사용하는 검증 메서드
- `iss`: 발급자(issuer)의 DID 주소

[VC-JWT](https://www.w3.org/TR/vc-jose-cose/), [JWT](https://datatracker.ietf.org/doc/html/rfc7519) 또는 [JWS](https://datatracker.ietf.org/doc/html/rfc7515) 명세에 기술되지 않은 추가 헤더는 무시하는 것이 권장됩니다(SHOULD).

#### 5.3.2.2 VC-JWT 페이로드[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#vc-jwt-payload "Permanent link")

VC-JWT의 페이로드는 [검증 가능한 자격증명 데이터 모델 v2.0](https://www.w3.org/TR/vc-data-model-2.0/) 명세에 기술된 클레임을 포함하는 표준 검증 가능한 자격증명입니다.

[JWT 명세](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1)의 일부 페이로드 클레임은 다음과 같이 검증 가능한 자격증명 필드로 대체되어야 합니다(MUST):

- `jti`는 검증 가능한 자격증명의 `id` 또는 `@id`로 대체됩니다.
- `sub`는 검증 가능한 자격증명의 `credentialSubject.id` 또는 `credentialSubject.@id`로 대체됩니다.

`vc` 및 `vp` 페이로드 클레임은 존재해서는 안 됩니다(MUST NOT).

> ℹ️ `iat` 및 `exp` 페이로드 클레임은 JWT 서명의 유효 기간을 나타내는 반면, `validFrom` 및 `validUntil` 검증 가능한 자격증명 페이로드 클레임은 자격증명 데이터의 [유효 기간](https://www.w3.org/TR/vc-data-model-2.0/#validity-period)을 나타냅니다. 따라서 이 클레임들은 페이로드 내에 공존할 수 있습니다.

`@type`이 "VerifiableCredential"인 경우, `credentialSubject` 속성이 반드시 정의되어야 합니다(MUST). `credentialSubject`의 값은 단일 자격증명 또는 자격증명 배열일 수 있습니다. 검증 가능한 자격증명은 다음을 반드시 포함해야 합니다:

- [`@id`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers)
- `iss` JWT 헤더와 일치하는 [`issuer`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#issuers)
- [`@type`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#types)
- [`credentialSubject`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-subject) 객체 또는 [`credentialSubject`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-subject) 배열

> 참고: `@id`와 `@type` 키워드는 각각 `id`와 `type`으로 별칭 지정할 수 있습니다. 따라서 이 별칭들도 사용 가능합니다.

#### 5.3.2.3 서명[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#signature "Permanent link")

VC-JWT의 마지막 요소는 서명으로, 무결성을 암호화적으로 보장하여 검증 가능한 자격증명을 변조 불가능(tamper-proof)하게 만듭니다.

JWS는 발급자(issuer)의 개인 키로 서명되며, 발급자의 DID 문서를 통해 얻을 수 있는 발급자의 공개 키(`kid` JWS 헤더에 참조됨)로 검증할 수 있습니다.

VC-JWT 서명은 [JSON 웹 서명(JWS)](https://datatracker.ietf.org/doc/html/rfc7515) 명세에 따라 생성됩니다. JWS 생성을 위한 [다양한 라이브러리](https://jwt.io/libraries)를 온라인에서 찾을 수 있습니다.

### 5.3.3 자격증명 주체[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-subject "Permanent link")

`credentialSubject`는 클레임(claim)을 포함하는 객체 또는 객체 배열일 수 있습니다.

하나의 Gaia-X 엔티티에 관한 클레임은 여러 자격증명과 그 주체에 걸쳐 분산될 수 있습니다.

각 자격증명 주체는 반드시 [`@id`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers)를 가져야 합니다(MUST).

자격증명 주체는 *값으로(by value)* 기술될 수 있습니다. 즉, 해당 위치에서 하나 이상의 클레임을 명시하는 방식입니다. 이 경우 아래에 지정된 [`@type`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#types)을 반드시 포함해야 합니다(MUST).

또는 자격증명 주체는 *참조로(by reference)* 기술될 수도 있습니다. 이 경우 `@id`는 동일한 `@id`, `@type`, 그리고 하나 이상의 클레임을 가진 RDF 리소스로 해석 가능해야 합니다(MUST). 자세한 내용은 [식별자](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers) 섹션을 참조하세요.

`@type` 속성의 값은 자격증명 주체에 관한 클레임 정의에 사용할 수 있는 [Gaia-X 온톨로지](https://w3id.org/gaia-x/)의 어휘를 결정합니다. 예: `LegalPerson`, `ServiceOffering`, `DataResource` 등.

credentialSubject 예시

```
{
  "@id": "https://example.com/legalPersonABC?vcid=c93b5075b3988eda4a529afce7e7c127f607b55dc08bb12e8c9adc9e33fe814f",
  "@type": "gx:legalPerson",
  "gx:legalName": "Legal Person ABC",
  "gx:legalRegistrationNumber": {
    "@id": "https://gaia-x.eu/legalRegistrationNumber_VC.json"
  },
  "gx:headquarterAddress": {
    "gx:countrySubdivisionCode": "FR-IDF"
  },
  "gx:legalAddress": {
    "gx:countrySubdivisionCode": "FR-IDF"
  }
}
```

## 5.4 검증 가능한 자격증명(Verifiable Credentials)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-credentials "Permanent link")

### 5.4.1 표준 검증 가능한 자격증명[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#standard-verifiable-credential "Permanent link")

검증 가능한 자격증명은 [VC-JWT 명세](https://www.w3.org/TR/vc-jose-cose/)에 기술된 대로 [JSON 웹 토큰(JWT)](https://datatracker.ietf.org/doc/html/rfc7519)으로 인코딩됩니다. 이 증명 방식은 [봉투형 증명(enveloping proof)](https://www.w3.org/TR/vc-data-model-2.0/#securing-mechanisms)입니다.

JWT는 헤더, 페이로드, 서명 세 요소로 구성되며 각 요소는 점(`.`)으로 구분됩니다.

검증 가능한 자격증명 예시
다음 자격증명을 사용하는 경우:

```
{
  "@context": [
    "https://www.w3.org/2018/credentials/v2",
    "https://w3id.org/gaia-x/development#"
  ],
  "@type": [
    "VerifiableCredential",
    "LegalParticipant"
  ],
  "@id": "https://example.org/legal-participant/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",
  "issuer": "did:web:example.org",
  "validFrom": "2024-04-01T12:26:22.601516+00:00",
  "validUntil": "2024-01-01T12:26:22.601516+00:00",
  "credentialSubject": {
    "id": "https://example.org/legal-participant-json/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",
    "type": "gx:LegalPerson",
    "gx:legalName": "Example Org",
    "gx:legalRegistrationNumber": {
      "id": "https://example.org/gaiax-legal-registration-number/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json"
    },
    "gx:headquarterAddress": {
      "gx:countrySubdivisionCode": "FR-75"
    },
    "gx:legalAddress": {
      "gx:countrySubdivisionCode": "FR-75"
    }
  }
}
```

VC-JWT 형태의 검증 가능한 자격증명 표현은 다음과 같습니다:

```
eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA
```

이 예시의 헤더, 페이로드, 서명을 JWT.io에서 확인하려면 [여기를 클릭하세요](https://jwt.io/#debugger-io?token=eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb\_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE\_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA).

### 5.4.2 봉투형 검증 가능한 자격증명(Enveloped Verifiable Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-credential "Permanent link")

봉투형 검증 가능한 자격증명(Enveloped Verifiable Credential)은 VC-JWT와 같은 봉투형 증명(enveloping proof)으로 인코딩된 검증 가능한 자격증명을 편리하게 표현하는 방법입니다.

세 가지 필드로 구성된 기본 JSON 객체로 표현됩니다:

- `@context`: 일반적으로 `https://www.w3.org/ns/credentials/v2`로 설정
- `id`: `application/vc+jwt` [데이터 URL](https://www.rfc-editor.org/rfc/rfc2397) 형태의 VC-JWT 데이터를 포함
- `type`: 반드시 `EnvelopedVerifiableCredential`로 설정해야 합니다(MUST)

이 유형의 검증 가능한 자격증명은 여러 검증 가능한 자격증명을 하나의 [검증 가능한 프레젠테이션](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-presentation)에 포함할 때 특히 유용합니다.

봉투형 검증 가능한 자격증명 예시
아래는 [검증 가능한 자격증명 예시](#verifiable-credential)를 봉투형 검증 가능한 자격증명으로 표현한 예시입니다.

```
{
  "@context": "https://www.w3.org/ns/credentials/v2",
  "id": "data:application/vc+jwt;eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmc6bGVnYWxQZXJzb25BQkMja2V5In0.eyJAaWQiOiJkaWQ6d2ViOmV4YW1wbGUub3JnOmxlZ2FsUGVyc29uQUJDIiwiQHR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiXSwiaXNzdWVyIjoiZGlkOndlYjpleGFtcGxlLm9yZzpsZWdhbFBlcnNvbkFCQyIsInZhbGlkRnJvbSI6IjIwMjQtMDEtMDFUMDA6MDA6MDBaIiwidmFsaWRVbnRpbCI6IjIwMjQtMDQtMDFUMDA6MDA6MDBaIiwiY3JlZGVudGlhbFN1YmplY3QiOlt7IkBpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWxQZXJzb25BQkMiLCJAdHlwZSI6Imd4OmxlZ2FsUGVyc29uIiwiZ3g6bGVnYWxOYW1lIjoiTGVnYWwgUGVyc29uIEFCQyIsImd4OmxlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyIjp7IkBpZCI6Imh0dHBzOi8vZ2FpYS14LmV1L2xlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyX1ZDLmpzb24ifSwiZ3g6aGVhZHF1YXJ0ZXJBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifSwiZ3g6bGVnYWxBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifX1dfQ.RIQKYwKsYEhH9p3m9tbG6zQKae3A7Qz3oAHXMI9RwXYVCL-euaBG7fWGTQ_F6yqWSPeQ6veHqkxKkvtdLIkSSpxZRJCtQs2HiORQX3tc21dkqtziKJIDJhmIBIq-2zDToPb5D4Yb_ryP0aTgcnBavAuiNCf7x3_gS6tBtYd_ZNnh3cifFiLGLop6PUhqhaTEYBlw1ou-28XUCHPeaarGrmxyZzxiBV_3J5hAe8XvfnFo9Y__LcbuOjNMsU2kKhI9otw9Ll4C8IZ9Qsqdq52QFCvkbvtcvX_3IJpzyxSS7TxOXAPPwYbYV_u7tgygPRvvmQG99Q651y62tQGA_B6Eqg",
  "type": "EnvelopedVerifiableCredential"
}
```

## 5.5 검증 가능한 프레젠테이션(Verifiable Presentations)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-presentations "Permanent link")

### 5.5.1 표준 검증 가능한 프레젠테이션[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#standard-verifiable-presentation "Permanent link")

`@type`이 `VerifiablePresentation`인 경우, `verifiableCredential` 속성이 반드시 정의되어야 합니다(MUST).
`verifiableCredential` 속성의 값은 하나 이상의 [봉투형 검증 가능한 자격증명](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-credential)으로 구성된 배열이어야 합니다(MUST).
검증 가능한 프레젠테이션은 다음을 반드시 포함해야 합니다:

- [`@type`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#types)
- `EnvelopedVerifiableCredential`로 구성된 [`verifiableCredential`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-credential) 배열

검증 가능한 프레젠테이션 예시
아래는 [봉투형 검증 가능한 자격증명](#enveloped-verifiable-credential) 장의 예시를 포함하는 검증 가능한 프레젠테이션 예시입니다.

```
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2"
  ],
  "@id": "https://gaia-x.eu/verifiablePresentation/1",
  "type": [
    "VerifiablePresentation"
  ],
  "verifiableCredential": [
    {
      "@context": "https://www.w3.org/ns/credentials/v2",
      "id": "data:application/vc+jwt;eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmc6bGVnYWxQZXJzb25BQkMja2V5In0.eyJAaWQiOiJkaWQ6d2ViOmV4YW1wbGUub3JnOmxlZ2FsUGVyc29uQUJDIiwiQHR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiXSwiaXNzdWVyIjoiZGlkOndlYjpleGFtcGxlLm9yZzpsZWdhbFBlcnNvbkFCQyIsInZhbGlkRnJvbSI6IjIwMjQtMDEtMDFUMDA6MDA6MDBaIiwidmFsaWRVbnRpbCI6IjIwMjQtMDQtMDFUMDA6MDA6MDBaIiwiY3JlZGVudGlhbFN1YmplY3QiOlt7IkBpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWxQZXJzb25BQkMiLCJAdHlwZSI6Imd4OmxlZ2FsUGVyc29uIiwiZ3g6bGVnYWxOYW1lIjoiTGVnYWwgUGVyc29uIEFCQyIsImd4OmxlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyIjp7IkBpZCI6Imh0dHBzOi8vZ2FpYS14LmV1L2xlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyX1ZDLmpzb24ifSwiZ3g6aGVhZHF1YXJ0ZXJBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifSwiZ3g6bGVnYWxBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifX1dfQ.RIQKYwKsYEhH9p3m9tbG6zQKae3A7Qz3oAHXMI9RwXYVCL-euaBG7fWGTQ_F6yqWSPeQ6veHqkxKkvtdLIkSSpxZRJCtQs2HiORQX3tc21dkqtziKJIDJhmIBIq-2zDToPb5D4Yb_ryP0aTgcnBavAuiNCf7x3_gS6tBtYd_ZNnh3cifFiLGLop6PUhqhaTEYBlw1ou-28XUCHPeaarGrmxyZzxiBV_3J5hAe8XvfnFo9Y__LcbuOjNMsU2kKhI9otw9Ll4C8IZ9Qsqdq52QFCvkbvtcvX_3IJpzyxSS7TxOXAPPwYbYV_u7tgygPRvvmQG99Q651y62tQGA_B6Eqg",
      "type": "EnvelopedVerifiableCredential"
    }
  ]
}
```

### 5.5.2 봉투형 검증 가능한 프레젠테이션(Enveloped Verifiable Presentation)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-presentation "Permanent link")

[봉투형 검증 가능한 자격증명](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-credential)과 마찬가지로, 봉투형 검증 가능한 프레젠테이션(Enveloped Verifiable Presentation)은 `application/vp+jwt` [데이터 URL](https://www.rfc-editor.org/rfc/rfc2397)을 포함하는 기본 JSON 객체 형태의 [검증 가능한 프레젠테이션](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-presentation) 표현입니다.

이 데이터 URL은 JWS로 보안이 적용된 검증 가능한 프레젠테이션을 표현합니다.
검증 가능한 프레젠테이션의 VC-JWT에는 [검증 가능한 자격증명](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-credential)과 동일한 헤더가 사용되지만, 다음 항목은 예외입니다:

- `typ` 헤더는 `vp+jwt`로 설정
- `cty` 헤더는 `vp`로 설정

봉투형 검증 가능한 프레젠테이션 예시
아래는 [검증 가능한 프레젠테이션 예시](#verifiable-presentation)를 봉투형 검증 가능한 프레젠테이션으로 표현한 예시입니다.

```
{
  "@context": "https://www.w3.org/ns/credentials/v2",
  "id": "data:application/vp+jwt;eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmc6bGVnYWxQZXJzb25BQkMja2V5In0.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvbnMvY3JlZGVudGlhbHMvdjIiXSwiQGlkIjoiaHR0cHM6Ly9nYWlhLXguZXUvdmVyaWZpYWJsZVByZXNlbnRhdGlvbi8xIiwidHlwZSI6WyJWZXJpZmlhYmxlUHJlc2VudGF0aW9uIl0sInZlcmlmaWFibGVDcmVkZW50aWFsIjpbeyJAY29udGV4dCI6Imh0dHBzOi8vd3d3LnczLm9yZy9ucy9jcmVkZW50aWFscy92MiIsImlkIjoiZGF0YTphcHBsaWNhdGlvbi92YytsZCtqc29uK2p3dDtleUpoYkdjaU9pSlFVekkxTmlJc0luUjVjQ0k2SW5aaksyeGtLMnB6YjI0cmFuZDBJaXdpWTNSNUlqb2lkbU1yYkdRcmFuTnZiaUlzSW10cFpDSTZJbVJwWkRwM1pXSTZaWGhoYlhCc1pTNXZjbWM2YkdWbllXeFFaWEp6YjI1QlFrTWphMlY1SW4wLmV5SkFhV1FpT2lKa2FXUTZkMlZpT21WNFlXMXdiR1V1YjNKbk9teGxaMkZzVUdWeWMyOXVRVUpESWl3aVFIUjVjR1VpT2xzaVZtVnlhV1pwWVdKc1pVTnlaV1JsYm5ScFlXd2lYU3dpYVhOemRXVnlJam9pWkdsa09uZGxZanBsZUdGdGNHeGxMbTl5Wnpwc1pXZGhiRkJsY25OdmJrRkNReUlzSW5aaGJHbGtSbkp2YlNJNklqSXdNalF0TURFdE1ERlVNREE2TURBNk1EQmFJaXdpZG1Gc2FXUlZiblJwYkNJNklqSXdNalF0TURRdE1ERlVNREE2TURBNk1EQmFJaXdpWTNKbFpHVnVkR2xoYkZOMVltcGxZM1FpT2x0N0lrQnBaQ0k2SW1oMGRIQnpPaTh2WlhoaGJYQnNaUzV2Y21jdmJHVm5ZV3hRWlhKemIyNUJRa01pTENKQWRIbHdaU0k2SW1kNE9teGxaMkZzVUdWeWMyOXVJaXdpWjNnNmJHVm5ZV3hPWVcxbElqb2lUR1ZuWVd3Z1VHVnljMjl1SUVGQ1F5SXNJbWQ0T214bFoyRnNVbVZuYVhOMGNtRjBhVzl1VG5WdFltVnlJanA3SWtCcFpDSTZJbWgwZEhCek9pOHZaMkZwWVMxNExtVjFMMnhsWjJGc1VtVm5hWE4wY21GMGFXOXVUblZ0WW1WeVgxWkRMbXB6YjI0aWZTd2laM2c2YUdWaFpIRjFZWEowWlhKQlpHUnlaWE56SWpwN0ltZDRPbU52ZFc1MGNubFRkV0prYVhacGMybHZia052WkdVaU9pSkdVaTFKUkVZaWZTd2laM2c2YkdWbllXeEJaR1J5WlhOeklqcDdJbWQ0T21OdmRXNTBjbmxUZFdKa2FYWnBjMmx2YmtOdlpHVWlPaUpHVWkxSlJFWWlmWDFkZlEuUklRS1l3S3NZRWhIOXAzbTl0Ykc2elFLYWUzQTdRejNvQUhYTUk5UndYWVZDTC1ldWFCRzdmV0dUUV9GNnlxV1NQZVE2dmVIcWt4S2t2dGRMSWtTU3B4WlJKQ3RRczJIaU9SUVgzdGMyMWRrcXR6aUtKSURKaG1JQklxLTJ6RFRvUGI1RDRZYl9yeVAwYVRnY25CYXZBdWlOQ2Y3eDNfZ1M2dEJ0WWRfWk5uaDNjaWZGaUxHTG9wNlBVaHFoYVRFWUJsdzFvdS0yOFhVQ0hQZWFhckdybXh5Wnp4aUJWXzNKNWhBZThYdmZuRm85WV9fTGNidU9qTk1zVTJrS2hJOW90dzlMbDRDOElaOVFzcWRxNTJRRkN2a2J2dGN2WF8zSUpwenl4U1M3VHhPWEFQUHdZYllWX3U3dGd5Z1BSdnZtUUc5OVE2NTF5NjJ0UUdBX0I2RXFnIiwidHlwZSI6IkVudmVsb3BlZFZlcmlmaWFibGVDcmVkZW50aWFsIn1dfQ.jnEqD2HH7eNnzRPwTjwsFigyENPozdDzmksXjevGNiH4hWJGLoM-765IP1mEE-tsLi2tMXQ6TeWIfw_6NkpY0vo_FUXWBBlj0IgMbxbt0gQwHRW9Ph3SVKQMCdIfp_pmdWPCEUrr_HxjkdiZpF1fa4qGSYBYl6tRSf1N0iCY0SzKvStI-EiudwHtlSygcqjxNq1jdpZtQyjYa_golZmyBdX7BYUUkcY30vypKTjMgBLHlZOzIljdiLKcm_MfDGEBt-Ha_qxpKpwRZoMFhsq89RXeExpeAw8Vg3ZR7yWsmP3T-7DDrZ5sadpNyCDXpryvm2UoDs__M4lEvkl3HIy9LQ",
  "type": "EnvelopedVerifiablePresentation"
}
```

## 5.6 발급자 요구사항[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#issuer-requirements "Permanent link")

`issuer` 속성은 검증 가능한 자격증명과 검증 가능한 프레젠테이션 모두에 반드시 존재해야 합니다(MUST). `issuer` 속성의 값은 해석 가능한 URI여야 합니다(MUST).

`issuer`의 URI에서 지원하는 스킴(scheme)은 다음과 같습니다:

- `https`
- `did`. 지원되는 [DID 메서드](https://w3c.github.io/did-spec-registries/#did-methods):
- `web`

Gaia-X 소프트웨어 릴리스별로 지원하는 DID 메서드 목록은 [아키텍처 문서](https://gaia-x.gitlab.io/technical-committee/architecture-working-group/architecture-document/)에서 확인할 수 있습니다.

참고

시간적 유효성:

validFrom 속성 - [`validFrom`](https://www.w3.org/TR/vc-data-model-2.0/#validity-period) 속성은 검증 가능한 자격증명과 검증 가능한 프레젠테이션 모두에서 필수입니다.

validUntil 속성 - [`validUntil`](https://www.w3.org/TR/vc-data-model-2.0/#validity-period) 속성은 검증 가능한 자격증명과 검증 가능한 프레젠테이션에서 권장됩니다.

## 5.7 추가 기능[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#additional-features "Permanent link")

### 5.7.1 관련 리소스의 무결성[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#integrity-of-related-resources "Permanent link")

동일한 발급자가 관리하지 않는 객체(검증 가능한 자격증명 또는 자격증명 주체)에 대한 참조를 가능하게 하기 위해, 참조된 객체의 무결성 검증을 위한 `@sri` [서브리소스 무결성(Subresource Integrity)](https://www.w3.org/TR/SRI/) 속성 지정을 권장합니다.

`sri` 속성은 참조된 정규화된(normalised) JSON 객체의 해시를 계산하여 생성합니다.  
JSON 객체는 [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785)에 정의된 JSON 정규화 스킴(JSON Canonicalization Scheme, JCS)에 따라 정규화됩니다.

`sri` 속성 예시

SRI 속성

```
{
  "@id": "https://example.com/ABC",
  "sri": "sha256-b9a822666c3569a8ae80c897a1984f68bbdffa1f8141cacdb3f168b1c0b9aa36"
}
```

### 5.7.2 자격증명 생명주기와 상태[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-lifecycle-and-status "Permanent link")

검증 가능한 자격증명은 안전한 데이터 및 신원 시스템의 핵심 구성요소로, 신뢰할 수 있고 변조 불가능한 자격증명의 발급 및 제시를 가능하게 합니다. 그러나 동적이고 변화하는 환경에서는 정보가 손상되거나 만료된 경우 해당 자격증명을 적시에 폐기(revocation)하거나 정지(suspension)할 수 있는 메커니즘을 마련하는 것이 중요합니다.

검증 가능한 자격증명은 다음 상태 중 하나를 가질 수 있습니다:

- **만료(expired)**: `validUntil` 속성이 현재 시각보다 과거인 경우, 또는 클레임 서명에 사용된 키가 포함된 인증서가 만료된 경우
- **폐기(revoked)**:
- 배열 서명에 사용된 키 쌍이 폐기된 경우
- **credentialStatus**의 **statusPurpose** 속성이 **"revocation"**으로 설정되어 있고 **credentialIndex** 위치의 상태 값이 **true**인 경우
- **정지(suspended)**: **credentialStatus**의 **statusPurpose** 속성이 **"suspension"**으로 설정되어 있고 **credentialIndex** 위치의 상태 값이 **true**인 경우
- **사용 중단(deprecated)**: 동일한 식별자와 동일한 서명 발급자를 가진 다른 검증 가능한 자격증명이 더 최신의 발급 일시를 가진 경우
- **활성(active)**: 위의 어떤 상태에도 해당하지 않는 경우

자격증명 상태 목록(Credential Status List, CSL), 특히 [W3C 검증 가능한 자격증명 비트스트링 상태 목록(Verifiable Credentials Bitstring Status List)](https://www.w3.org/TR/vc-bitstring-status-list/)을 활용하면 검증 가능한 자격증명의 폐기 상태를 관리하고 전달하는 표준화된 방법을 제공할 수 있습니다.

검증 가능한 자격증명을 발급할 때, 발급자는 해당 자격증명과 관련된 자격증명 상태 목록(CSL) 항목에 대한 참조를 자격증명에 포함할 수 있습니다. 이 참조는 일반적으로 URI 형태로 제공되며, 의존 당사자(relying party, 주로 검증자)가 자격증명의 현재 유효성 상태를 즉시 확인할 수 있게 합니다.

검증 가능한 자격증명을 검증하기 위해 의존 당사자는 제공된 URI를 사용하여 참조된 자격증명 상태 목록 항목을 조회합니다. 이 항목에는 자격증명의 상태 정보가 포함되어 있어, 자격증명이 여전히 유효한지, 폐기/정지되었는지, 또는 다른 관련 상태인지를 확인할 수 있습니다.

의존 당사자는 신뢰할 수 있는 출처로부터 자격증명 상태 목록의 로컬 복사본을 주기적으로 업데이트하여 최신 폐기 상태 정보를 보유할 수 있습니다. 이를 통해 오래되거나 잘못된 정보에 의존하는 상황을 방지하고 에코시스템 전반의 보안을 강화합니다.

| party\_credential\_revocation.json | |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 ``` | ``` {   "@context": [     "https://www.w3.org/ns/credentials/v2",     "https://w3id.org/gaia-x/development#"   ],   "id": "https://did.actor/alice/credentials/status/3",   "type": ["VerifiableCredential", "BitstringStatusListCredential"],   "issuer": "did:web:did.actor:alice",   "issued": "2021-04-05T14:27:40Z",   "credentialSubject": {     "id": "https://example.com/status/3#list",     "type": "BitstringStatusList",     "statusPurpose": "revocation",     "encodedList": "H4sIAAAAAAAAA-3BMQEAAADCoPVPbQwfoAAAAAAAAAAAAAAAAAAAAIC3AYbSVKsAQAAA"   } } ``` |

November 28, 2025


November 28, 2025
