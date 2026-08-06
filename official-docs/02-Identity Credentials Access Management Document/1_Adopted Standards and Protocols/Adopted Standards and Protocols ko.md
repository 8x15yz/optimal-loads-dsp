# 3. 채택된 표준 및 프로토콜[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#adopted-standards-and-protocols "Permanent link")

이 섹션은 본 문서의 명세가 기반으로 삼는 핵심 참조 표준을 정의합니다.
Gaia-X의 설계 결정 사항(예: 포맷 또는 방식 선택)은 이 섹션에서 다루지 않으며, 해당 결정 사항, 프로파일, 제약 조건은 이후 챕터에서 소개됩니다.

## 3.1 자격증명 및 식별자 표준[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#standards-for-credentials-and-identifiers "Permanent link")

### 3.1.1 JSON-LD[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#json-ld "Permanent link")

[JSON-LD (연결 데이터를 위한 JavaScript 객체 표기법, JavaScript Object Notation for Linked Data)](https://json-ld.org/)는 익숙한 JSON 문법을 사용하여 연결 데이터(Linked Data)를 표현하는 W3C 표준입니다.   
JSON-LD는 컨텍스트(context)를 사용하여 JSON 속성을 IRI(국제화 리소스 식별자, Internationalized Resource Identifiers)에 매핑함으로써 용어를 명확하게 해석할 수 있게 하며, 시맨틱 의미를 부여하여 시스템 간 데이터 상호운용이 가능하도록 합니다.   
JSON-LD는 기존 JSON과 완전히 호환되므로, 기존 JSON 기반 시스템에 통합하기 쉬우면서도 더욱 풍부한 연결 데이터 시맨틱스를 지원합니다.

### 3.1.2 SHACL (Shapes Constraint Language)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#shacl-shapes-constraint-language "Permanent link")

[SHACL (셰이프 제약 언어, Shapes Constraint Language)](https://www.w3.org/TR/shacl/)은 RDF 그래프에 대한 셰이프(shape), 즉 제약 조건을 정의하고 데이터(RDF 그래프)가 해당 셰이프를 준수하는지 검증하기 위한 W3C 표준입니다.   
셰이프는 속성 경로(property path), 카디널리티(cardinality), 데이터 타입 제한, 논리 조합에 대한 제약 조건을 표현하며, SPARQL과 같은 확장 언어를 사용하여 더 복잡한 유효성 검증 규칙을 표현할 수도 있습니다.

### 3.1.3 분산 식별자 (Decentralized Identifiers)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#decentralized-identifiers "Permanent link")

[분산 식별자 (DID, Decentralized Identifiers)](https://www.w3.org/TR/did-1.0/)는 단일 중앙화 레지스트리나 기관 없이도 검증 가능한 자기 주권 디지털 신원(self-sovereign digital identity)을 구현하는 URI입니다. 단, 분산 또는 탈중앙화 레지스트리에 연결(anchored)될 수도 있습니다.
DID는 DID 문서(DID Document)로 결정(resolve)되며, 이 문서에는 일반적으로 하나 이상의 검증 방법(verification method)이 포함되고, 각 검증 방법은 암호화 키 자료(cryptographic key material)와 연결됩니다.   
검증 방법에는 일반적으로 비대칭 암호화 알고리즘을 통해 수학적으로 연결된 개인 키(private key)와 공개 키(public key) 쌍이 포함됩니다. 개인 키는 안전하게 생성되어 DID 제어자(DID controller)의 단독 통제 하에 보관되며, 대응하는 공개 키는 검증 방법의 일부로 DID 문서에 게시됩니다.  
검증 방법은 식별자에 대한 통제권을 증명하고, 검증 가능한 자격증명(Verifiable Credentials, VC) 및 기타 리소스의 공유·조회와 같은 신뢰할 수 있는 상호작용을 가능하게 합니다 (DID 명세는 [이 링크](https://www.w3.org/TR/did-1.0/#the-relationship-between-did-controllers-and-did-subjects) 참조).   
이러한 암호화 바인딩을 통해, 개인 키를 보유한 DID 제어자만이 디지털 서명을 생성할 수 있으며, 검증자는 DID 문서의 공개 키를 이용하여 해당 서명을 검증함으로써 Gaia-X 에코시스템 내에서 암호화적 통제권 증명과 진위 확인을 확립할 수 있습니다.

### 3.1.4 JSON 웹 토큰 (JWT)/JSON 웹 서명 (JWS)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#json-web-token-jwtjson-web-signature-jws "Permanent link")

[JSON 웹 토큰 (JWT, JSON Web Token)](https://www.rfc-editor.org/rfc/rfc7519.html)은 무결성 보호 또는 서명이 가능한 JSON 객체에 클레임(claim) 집합을 인코딩하기 위한 공개 표준(RFC 7519)입니다.
[JSON 웹 서명 (JWS, JSON Web Signature)](https://www.rfc-editor.org/rfc/rfc7515.html)(RFC 7515)은 JSON 기반 구조를 사용하여 페이로드(payload)에 디지털 서명을 적용하는 방법을 정의하며, 이를 통해 진위성과 무결성을 검증할 수 있습니다.

### 3.1.5 JSON 웹 키 (JSON Web Key)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#json-web-key "Permanent link")

[JSON 웹 키 (JWK, JSON Web Key)](https://datatracker.ietf.org/doc/html/rfc7517)는 [RFC 7517]에 정의된 표준으로, 암호화 키 및 키 세트(key set)를 JSON 기반으로 표현하는 방식입니다. 공개 키와 키 메타데이터를 게시하고 교환하는 표준화되고 상호운용 가능한 방법을 제공하며, 주로 신원 및 자격증명 시스템에서 JSON 웹 토큰(JWT) 및 기타 디지털 서명 검증에 활용됩니다.

### 3.1.6 W3C 검증 가능한 자격증명 데이터 모델 v2.0[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#w3c-verifiable-credentials-data-model-v20 "Permanent link")

[W3C 검증 가능한 자격증명 데이터 모델 v2.0 (W3C Verifiable Credentials Data Model v2.0)](https://www.w3.org/TR/vc-data-model-2.0/)에서 정의하는 검증 가능한 자격증명(Verifiable Credentials, VC)은 하나 이상의 주체(subject)에 대한 어설션(assertion, 클레임)을 암호화적으로 검증 가능한 기계 가독 형식으로 표현하는 데 사용됩니다.   
VC에는 클레임(claim), 발급자(issuer) 메타데이터, 유효성 제약 조건, 그리고 무결성과 진위성을 보장하기 위한 증명 메커니즘(proof mechanism)이 포함됩니다.   
VC는 직접 공유되거나, 보유자(holder)가 하나 이상의 자격증명을 제어된 방식으로 제시하는 데 사용하는 [검증 가능한 프레젠테이션 (VP, Verifiable Presentation)](https://www.w3.org/TR/vc-data-model-2.0/#presentations)에 내장되어 사용될 수 있습니다.   
검증 가능한 프레젠테이션을 통해 검증자(verifier)는 포함된 자격증명의 클레임이 해당 발급자로부터 비롯된 것임을 확인할 수 있습니다.

### 3.1.7 W3C VC-비트스트링 상태 목록 (VC-Bitstring Status List)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#w3c-vc-bitstring-status-list "Permanent link")

비트스트링 상태 목록 ([W3C VC-Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/))은 다수의 검증 가능한 자격증명(VC)의 폐기(revocation) 또는 정지(suspension) 상태를 단일 비트스트링(bitstring)에 공간 효율적이고 프라이버시를 보호하는 방식으로 인코딩하는 메커니즘을 정의합니다.   
각 자격증명은 특정 비트 인덱스와 연결되며, 값 1은 "폐기" 또는 "정지"를, 값 0은 "유효"를 의미합니다. 이 비트스트링은 (보통 압축되어) 검증 가능한 자격증명으로 게시되므로, 검증자는 각 발급자에게 개별적으로 문의하지 않고도 상태를 확인할 수 있습니다.

## 3.2 프로토콜[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#protocols "Permanent link")

### 3.2.1 검증 가능한 자격증명을 위한 OpenID (OID4VC)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#openid-for-verifiable-credentials-oid4vc "Permanent link")

"OID4VC"는 검증 가능한 자격증명(Verifiable Credentials) 및 검증 가능한 프레젠테이션(Verifiable Presentations)의 발급과 제시를 지원하는 OpenID/OAuth 기반 프로토콜 패밀리를 통칭하는 용어입니다.

### 3.2.2 검증 가능한 자격증명 발급을 위한 OpenID Connect (OIDC4VCI)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#openid-connect-for-verifiable-credential-issuance-oidc4vci "Permanent link")

[(OIDC4VCI)](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)는 [OAuth 2.0 명세](https://www.rfc-editor.org/info/rfc6749)를 기반으로 하며, 발급자(issuer)가 보유자(holder) 및 지갑(wallet)과 통신하여 검증 가능한 자격증명(VC)을 안전하게 발급할 수 있도록 합니다.

OID4VCI는 발급자가 보유자의 지갑에 검증 가능한 자격증명을 발급할 수 있는 OAuth 보호 API를 정의합니다.
이 명세는 자격증명 발급에 대한 인가(authorization)를 획득하기 위해 OAuth 2.0을 재정의하지 않고 그대로 활용합니다.

> ⚠️ OIDC4VCI는 구현자를 위한 안정적인 기준선으로서 버전 1.0 명세로 게시되었습니다.

### 3.2.3 검증 가능한 프레젠테이션을 위한 OpenID Connect (OIDC4VP)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#openid-connect-for-verifiable-presentations-oidc4vp "Permanent link")

[(OIDC4VP)](https://openid.github.io/OpenID4VP/openid-4-verifiable-presentations-wg-draft.html)는 OAuth 2.0 / OpenID Connect를 확장하여 보유자(holder)가 지갑(wallet)을 통해 하나 이상의 검증 가능한 자격증명(VC)을 검증 가능한 프레젠테이션(VP) 형태로 검증자(verifier)에게 제시할 수 있도록 합니다.

> ⚠️ OIDC4VP는 OpenID "버전 1.0" 초안 세트에 따라 게시되었습니다.

November 28, 2025


November 28, 2025
