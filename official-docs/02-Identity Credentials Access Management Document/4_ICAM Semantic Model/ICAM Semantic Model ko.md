# 6. ICAM 시맨틱 모델[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#icam-semantic-model "Permanent link")

## 6.1 신뢰 범위 크리덴셜(Trust Scope Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#trust-scope-credential "Permanent link")

신뢰 범위 크리덴셜(Trust Scope Credential)은 [W3C 검증 가능한 크리덴셜 데이터 모델 v2.0](https://www.w3.org/TR/vc-data-model-2.0/)을 기반으로 하며, 특정 범위에 대한 신뢰 서비스 제공자(Trust Service Provider)의 인증(accreditation)을 기계가 읽을 수 있는 형태로 표현하는 데 목적이 있습니다. 이 크리덴셜은 인증된 발급자(accredited issuer)를 정의함으로써, 본 장에서 이후에 설명할 당사자 크리덴셜(Party Credential)의 활용을 가능하게 합니다. 또한 신뢰 범위 크리덴셜은 외부 신뢰 서비스 제공자의 활용을 용이하게 함으로써, 조직·에코시스템(ecosystem)·데이터 스페이스(data space) 간의 협력과 상호운용성을 지원합니다.

**TrustScopeCredential**의 주요 정의 항목은 다음과 같습니다:

- **Scope(범위)**: 신뢰 서비스 제공자가 인증된 범위(발급된 크리덴셜이 유효한 것으로 인정되는 범위).
- **TrustedIssuers(신뢰 발급자)**: 해당 **Scope** 내에서 **크리덴셜**을 발급할 권한을 부여받은 주체.
- **Vocabularies(어휘)**: **TrustedIssuer**가 정의된 **Scope** 내에서 발급할 수 있는 **크리덴셜**을 시맨틱적으로 정의하는 SHACL 기반 어휘 명세.
- **Trusted List(신뢰 목록)**: 신뢰 서비스 제공자가 발급한 DID의 유효성을 검증하는 데 사용되는 신뢰 목록.

`Trust Scope Credential`은 다음 속성으로 정의됩니다:

| 속성 | 타입.값/어휘 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| `gx:scopeDescription` | String | 아니오 | 신뢰 서비스 제공자의 범위(scope)에 대한 설명 |
| `gx:trustIssuers` | DID[] | 예 | 하나의 키 쌍(key pair)만을 고유하게 식별하는 발급자 검증 수단(verificationMethod)에 대한 확인 가능한 링크 목록 |
| `gx:vocabularies` | URI[] | 아니오 | 신뢰 서비스 제공자의 범위를 시맨틱적으로 기술하는 어휘/스키마(SHACL)를 가리키는 URI 목록 |
| `gx:trustedListKind` | KindOfTrustedList | 아니오 | 트러스트 앵커(Trust Anchor)가 발급한 DID를 검증하는 데 사용되는 신뢰 목록 구현 방식 |
| `gx:trustedListEndpoint` | URI | 아니오 | 위 신뢰 목록의 주소 |

**KindOfTrustedList** 타입은 신뢰 목록의 식별된 구현 방식 목록을 정의합니다:

- Gaia-X Trusted List Generic REST API 명세
- Gaia-X IPFS (ETSI TS 119 612 형식)
- TRAIN
- EBSI
- (기타 가능한 구현 방식)

**중요 사항**
*Gaia-X Trusted List Generic REST API 명세*는 특정 DID에 대해 유효 여부를 "true"로 반환할 수 있는 단순한 API 계약으로 설계되었습니다. 이를 통해 정의된 목록에 포함되지 않은 커스텀 신뢰 목록도 쉽게 통합할 수 있습니다.

### 6.1.1 신뢰 범위 크리덴셜 특화 예시[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#trust-scope-credential-specialisation-examples "Permanent link")

**TrustScopeCredential**의 특화(specialisation) 사례는 다음과 같이 쉽게 정의할 수 있습니다:

#### 6.1.1.1 **조직 신뢰 범위(Organization Trust Scope)**[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#organization-trust-scope "Permanent link")

이 특화 크리덴셜은 자가 발급(self-issued) 크리덴셜로, 발급 조직이 자신의 당사자(party)를 식별하고 권한을 부여하는 데 사용할 *역할/신원 속성(Roles/Identity Attributes)*을 정의할 수 있도록 합니다:

- **scope(범위)** - *조직 크리덴셜 관리(Organization Credential Management, OCM)*.
- **trusted issuers(신뢰 발급자)** - 조직 자신.
- **vocabularies(어휘)** - 정의된 범위 내에서 유효한 *역할/신원 속성* 및 **도메인 특화 크리덴셜(Domain Specific Credentials)**의 시맨틱을 정의.
- **trusted list(신뢰 목록)** - **PartyCredential**을 발급하여 당사자(사용자, 자연인, 엔드포인트 서비스 등)에게 *역할/신원 속성* 및 **도메인 특화 크리덴셜**을 할당하거나 폐기(revoke).

#### 6.1.1.2 **Gaia-X 컴플라이언스 신뢰 범위(Gaia-X Compliance Trust Scope)**[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#gaia-x-compliance-trust-scope "Permanent link")

이 크리덴셜은 Gaia-X가 발급하며, 특정 조직이 Gaia-X 컴플라이언스(Compliance) 맥락에서 특정 클레임(claim)에 대한 어테스테이션(attestation)을 발급할 수 있도록 권한을 부여합니다.

- **scope(범위)** - Gaia-X 컴플라이언스를 증명하는 어테스테이션 발급.
- **trusted issuers(신뢰 발급자)** - Gaia-X로부터 해당 범위에서 어테스테이션을 발급할 권한을 인증받은 조직.
- **vocabularies(어휘)** - 해당 범위에서 어테스테이션 발급에 적용 가능한 시맨틱을 정의.
- **trusted list(신뢰 목록)** - Gaia-X 제공자(Provider)에게 발급된 어테스테이션의 할당 및 폐기 관리. 트러스트 앵커 크리덴셜 특화 예시

#### 6.1.1.3 **에코시스템 신뢰 범위(Ecosystem Trust Scope)**[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#ecosystem-trust-scope "Permanent link")

이 특화 크리덴셜은 에코시스템 운영자가 자가 발급하는 크리덴셜로, 다음을 정의할 수 있습니다:

- **scope(범위)** - *에코시스템(Ecosystem)* 관리(온보딩/오프보딩/역할 할당 등).
- **trusted issuers(신뢰 발급자)** - 에코시스템 자신.
- **vocabularies(어휘)** - 정의된 범위 내에서 유효한 *역할/신원 속성* 및 **도메인 특화 크리덴셜**의 시맨틱을 정의.
- **trusted list(신뢰 목록)** - **MembershipPartyCredential**을 발급하여 구성원(다른 참여자)에게 *역할/신원 속성* 및 **도메인 특화 크리덴셜**을 할당하거나 폐기.

### 6.1.2 신뢰 범위 크리덴셜을 활용한 페더레이션(Federation)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#federation-using-trust-scope-credentials "Permanent link")

**TrustScopeCredential**은 상호운용성을 고려하여 설계되었으며, 선택적·양방향·단방향 신뢰를 손쉽게 구현할 수 있습니다. 두 개 이상의 신뢰 범위 간의 페더레이션(federation)은 이를 활용하는 대표적인 사례입니다. 다음은 몇 가지 예시입니다:

#### 6.1.2.1 두 에코시스템 간 단방향 선택적 페더레이션[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#monodirectional-selective-federation-between-2-ecosystems "Permanent link")

에코시스템 A는 에코시스템 B가 발급한 **EcosystemTrustScope**의 **신뢰 발급자(trusted issuers)**를 신뢰하고, 신뢰할 **도메인 특화 크리덴셜**의 부분집합을 선택함으로써 에코시스템 B와의 페더레이션을 설정할 수 있습니다.

#### 6.1.2.2 두 에코시스템 간 양방향 전체 페더레이션[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#bidirectional-full-federation-between-2-ecosystems "Permanent link")

에코시스템 A는 에코시스템 B가 발급한 **EcosystemTrustScope**를 완전히 신뢰하고, 에코시스템 B도 마찬가지로 에코시스템 A를 완전히 신뢰함으로써 양방향 페더레이션을 구성합니다.

#### 6.1.2.3 여러 에코시스템을 선택적으로 신뢰하는 운영자가 관리하는 페더레이션[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#federation-managed-by-an-operator-that-selectively-trusts-multiple-ecosystems "Permanent link")

에코시스템 운영자는 각 에코시스템이 발급한 신뢰된 **EcosystemTrustScope**의 **신뢰 발급자** 목록과 관련 **도메인 특화 크리덴셜**을 직접 관리합니다.

**중요 사항**
위의 모든 예시에서 *신뢰(trusting)* 관계는 [검증 가능한 크리덴셜(verifiable credential)](https://www.w3.org/TR/vc-data-model-2.0/)을 발급하는 방식으로 구체적으로 구현할 수 있습니다. 이 경우 해당 크리덴셜의 [credentialSubject](https://www.w3.org/TR/vc-data-model-2.0/#credential-subject)는 **EcosystemTrustScope**의 ID가 됩니다. 또는 이보다 세분화된 **TrustRelationCredential**을 별도로 설계하여 동일한 목적으로 활용할 수 있습니다.

## 6.2 당사자 크리덴셜(Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#party-credential "Permanent link")

당사자 크리덴셜(Party Credential)은 [W3C 검증 가능한 크리덴셜 데이터 모델 v2.0](https://www.w3.org/TR/vc-data-model-2.0/)을 기반으로 하며, **자연인(Natural Persons)**, **서비스(Services)**, **법인(Legal Persons)** 등 모든 IAA 당사자(Party)의 기본 크리덴셜입니다.
범용 당사자 크리덴셜은 특화된 크리덴셜(**당사자 크리덴셜 특화** 참조)로 확장되도록 설계되었습니다.

`Party Credential`은 다음 속성으로 정의됩니다:

| 속성 | 타입.값/어휘 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| `gx:holder` | DID | 예 | 하나의 키 쌍(key pair)만을 고유하게 식별하는 보유자(holder) 검증 수단(verificationMethod)에 대한 확인 가능한 링크 |
| `odrl:hasPolicy` | policy[] in ODRL | 아니오 | ODRL로 표현된 `policy` 목록 |
| `gx:identityAttributes` | String[] | 아니오 | ABAC(속성 기반 접근 제어) 맥락에서 사용할 신원 속성(Identity Attributes)을 나타내는 리터럴 목록 |
| `gx:identityRoles` | String[] | 아니오 | RBAC(역할 기반 접근 제어) 맥락에서 사용할 신원 역할(Identity Roles)을 나타내는 리터럴 목록 |
| `gx:parentPartyCredential` | URI | 다른 기존 당사자 크리덴셜로부터 위임된 경우 필수 | 상위 당사자 크리덴셜에 대한 확인 가능한 링크 (단, `gx:holder`는 해당 크리덴셜의 서명자(issuer verificationMethod)와 동일해야 함) |

**매우 중요한 사항**

**credentialSubject.id**는 반드시 **크리덴셜 보유자(Credential Holder)**가 소유하거나 제어하는 `gx:holder` 속성에 의해 참조된 **검증 수단(verificationMethod, 키 쌍)**을 포함하는 **DID 문서(DID Document)**를 식별해야 합니다.
이 방식을 통해, PartyCredential VC는 민감하지 않은 데이터를 포함하는 경우 공개적으로 게시하거나, PII(개인 식별 정보)가 포함된 경우 비공개로 유지할 수 있습니다.

### 6.2.1 비공개 당사자 크리덴셜(Private Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#private-party-credential "Permanent link")

PII를 포함하는 **당사자 크리덴셜**은 해당 **id**를 통해 누구나 접근·조회할 수 있도록 공개하지 않습니다. 대신 지갑(wallet), 보안 저장 장치, 보안 볼트(vault) 스토리지 등 안전한 저장소에 보관해야 합니다.
이 유형의 크리덴셜 예시로는 법인 참여자(Legal Participant)가 사용자/직원에게 발급하는 **NaturalPersonCredential**이 있으며, 이를 통해 자연인이 특정 맥락에서 신뢰 당사자(Relying Party, RP)와 상호작용할 수 있도록 권한을 부여합니다.
이 크리덴셜에는 이름(Name), 성(Surname), 신원 속성(identityAttributes), 역할(Roles) 등이 포함되며, 이후에 설명하는 공개 당사자 크리덴셜(Public Party Credential)과 달리 반드시 공개 게시해서는 안 됩니다. 신뢰 당사자(RP)와의 상호작용 시 "선택적 공개(selective disclosure)"를 적용할 수 있습니다.

#### 6.2.1.1 비공개 당사자 크리덴셜 예시[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#private-party-credential-example "Permanent link")

다음 **NaturalPersonPartyCredential** 예시는 참여자 **did:web:did.actor:alice**가 여러 클레임(givenName, surname, idRoles 등)을 주장하는 크리덴셜을 발급하는 시나리오를 보여줍니다.
이 크리덴셜은 공개 게시되지 않으므로(**id**가 공개되지 않음) 보유자의 지갑에 반드시 보관해야 합니다.

`gx:holder` 속성은 **보유자(Holder)**가 소유한 키 쌍을 참조하는 did:key이며, 대상 지갑의 공개 키(public key)를 식별합니다.

| party\_credential.json | |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` | ``` {   "@context": [     "https://www.w3.org/ns/credentials/v2",     "https://w3id.org/gaia-x/development#"   ],   "id": "did:web:did.actor:alice:credentials:private#1222331234",   "type": ["VerifiableCredential"],   "issuer": "did:web:did.actor:alice",   "validFrom": "2023-08-28T23:00:00Z",   "credentialSubject": {     "id": "did:key:z4MXj1wBzi9jUstyPMS4jQqB6KdJaiatPkAtVtGc6bQEQEEsKTic4G7Rou3iBf9vPmT5dbkm9qsZsuVNjq8HCuW1w24nhBFGkRE4cd2Uf2tfrB3N7h4mnyPp1BF3ZttHTYv3DLUPi1zMdkULiow3M1GfXkoC6DoxDUm1jmN6GBj22SjVsr6dxezRVQc7aj9TxE7JLbMH1wh5X3kA58H3DFW8rnYMakFGbca5CB2Jf6CnGQZmL7o5uJAdTwXfy2iiiyPxXEGerMhHwhjTA1mKYobyk2CpeEcmvynADfNZ5MBvcCS7m3XkFCMNUYBS9NQ3fze6vMSUPsNa6GVYmKx2x6JrdEjCk3qRMMmyjnjCMfR4pXbRMZa3i",     "type": "gx:NaturalPersonPartyCredential",     "odrl:hasPolicy": [],     "gx:holder": "did:key:z4MXj1wBzi9jUstyPMS4jQqB6KdJaiatPkAtVtGc6bQEQEEsKTic4G7Rou3iBf9vPmT5dbkm9qsZsuVNjq8HCuW1w24nhBFGkRE4cd2Uf2tfrB3N7h4mnyPp1BF3ZttHTYv3DLUPi1zMdkULiow3M1GfXkoC6DoxDUm1jmN6GBj22SjVsr6dxezRVQc7aj9TxE7JLbMH1wh5X3kA58H3DFW8rnYMakFGbca5CB2Jf6CnGQZmL7o5uJAdTwXfy2iiiyPxXEGerMhHwhjTA1mKYobyk2CpeEcmvynADfNZ5MBvcCS7m3XkFCMNUYBS9NQ3fze6vMSUPsNa6GVYmKx2x6JrdEjCk3qRMMmyjnjCMfR4pXbRMZa3i",     "gx:identityAttributes": ["IdAttributeOne","IdAttributeTwo"],     "gx:identityRoles": ["IdRoleOne","IdRoleTwo"],     "gx:givenName": "John",     "gx:surname": "Doe"   },   "credentialStatus": [{     "id": "https://did.actor/alice/credentials/status/3#94567",     "type": "BitstringStatusListEntry",     "statusPurpose": "revocation",     "statusListIndex": "94567",     "statusListCredential": "https://did.actor/alice/credentials/status/3"   },{     "id": "https://did.actor/alice/credentials/status/4#23452",     "type": "BitstringStatusListEntry",     "statusPurpose": "suspension",     "statusListIndex": "23452",     "statusListCredential": "https://did.actor/alice/credentials/status/4"   }],   "proof": {     "type": "JsonWebSignature2020",     "created": "2023-08-28T13:25:35.827Z",     "proofPurpose": "assertionMethod",     "verificationMethod": "did:web:did.actor:alice#JWK2020",     "jws": "eyJhbGciOiJQUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..Sq5VJHCFuIP-cC86EknRnB91WQxNI5X4QtI0mMR3Xzl8VY5bYfOAtpEsejYeDUbi3Oed0VwQBRCqd11HL7NFF-KH02D9I97nHBftBaXo8e0uWQTRk6TA8xq9oQRuNdnm15eR2zudOzKlH4ArXcBo-hUxUH6EH7YimT0Uu5NbsofN-5C2ovksogbugl-NkW3MKrGkAYzsyaEcgh-vSiRwSl4vwE55sDkn16QgMtsccwo9PR0kzECHp8KQZTM3Nwnv4jNN-F3zP-3Vn0B-cm-UgHPz1RYX6uKrc3A4TlJvk9rxQNfLbNot8ZaQBPoLMnd98bV6giNaGIbekVOUuBxUKg"   }   } ``` |

### 6.2.2 공개 당사자 크리덴셜(Public Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#public-party-credential "Permanent link")

공개 당사자 크리덴셜은 누구나 공개적으로 접근하고 조회할 수 있는 데이터를 포함하는 **당사자 크리덴셜**입니다.

### 6.2.3 당사자 크리덴셜 특화 예시[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#party-credential-specialisation-examples "Permanent link")

다음은 가능한 당사자 크리덴셜 특화 유형의 일부입니다.

#### 6.2.3.1 자연인 당사자 크리덴셜(Natural Person Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#natural-person-party-credential "Permanent link")

이 크리덴셜은 참여자(Participant)가 자연인(일반적으로 자신의 사용자/직원)에게 발급하여, 해당 자연인이 다른 참여자에 속한 신뢰 당사자(Relying Party)와 상호작용할 수 있도록 권한을 부여합니다.

`Natural Person Party Credential`은 당사자 크리덴셜 속성에 더해 다음 속성으로 정의됩니다:

| 속성 | 타입.값/어휘 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| `gx:givenName` | String | 예 | 자연인의 이름 |
| `gx:surname` | String | 예 | 자연인의 성 |

#### 6.2.3.2 법인 당사자 크리덴셜(Legal Person Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#legal-person-party-credential "Permanent link")

이 크리덴셜은 법인 참여자(Legal Person Participant)가 다른 법인(일반적으로 자신의 사용자)에게 발급하여, 해당 법인이 다른 참여자에 속한 신뢰 당사자(Relying Party)와 자신을 대신하여 상호작용할 수 있도록 권한을 부여합니다.

`Legal Person Party Credential`은 당사자 크리덴셜 속성에 더해 다음 속성으로 정의됩니다:

| 속성 | 타입.값/어휘 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| `gx:organizationIdentifier` | String | 예 | eIDAS 규정에서 사용되는 조직 식별자 |

#### 6.2.3.3 서비스 당사자 크리덴셜(Service Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#service-party-credential "Permanent link")

이 크리덴셜은 참여자(Participant)가 자동화된 서비스(일반적으로 자동화된 프로세스)에게 발급하여, 해당 서비스가 다른 참여자에 속한 신뢰 당사자(Relying Party)와 상호작용할 수 있도록 권한을 부여합니다.

`Service Party Credential`은 당사자 크리덴셜 속성에 더해 다음 속성으로 정의됩니다:

| 속성 | 타입.값/어휘 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| `gx:baseURL` | URI | 예 | 서비스에 접근 가능한 기본 URL 엔드포인트 |

#### 6.2.3.4 멤버십 당사자 크리덴셜(Membership Party Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#membership-party-credential "Permanent link")

이 크리덴셜은 에코시스템을 운영하는 법인 참여자(LegalParticipant)가 다른 참여자에게 발급하여 해당 참여자의 멤버십(Membership) 상태를 증명합니다.

## 6.3 서명 크리덴셜(Signature Credential)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#signature-credential "Permanent link")

서명 크리덴셜(Signature Credential)은 디지털 서명을 기계 판독 가능하고 상호운용 가능한 형태로 표현하기 위해 도입된 검증 가능한 크리덴셜(Verifiable Credential)입니다. 데이터 트랜잭션 허가부터 계약 서명까지 다양한 시나리오를 지원합니다. 이를 통해 참여자는 디지털 리소스에 암호학적 서명을 적용하고, 해당 서명을 서명자의 신원에 검증 가능한 무결성과 함께 결합할 수 있습니다.

인정된 법적 신뢰 프레임워크(예: eIDAS)에서 발급된 인증서와 연결된 검증 수단(verification method)을 사용하면, 보증 수준(예: 공인 전자서명(Qualified Electronic Signature))에 따라 서명 크리덴셜이 자필 서명과 동등한 법적 효력을 가질 수 있습니다.

이 크리덴셜의 특화 유형인 서명 계약 크리덴셜(Signed Agreement Credential)은 시간이 지남에 따라 유효성이 취소될 수 있는 계약을 모델링하기 위해 폐기(revocability) 기능을 도입합니다. 이러한 크리덴셜은 각 참여자가 독립적으로 발급한 뒤 검증 가능한 프레젠테이션(Verifiable Presentation)에 집계할 수 있어, 데이터 이용 계약(Data Usage Agreement)과 같은 계약에 대한 탈중앙화된 서명 워크플로를 구현할 수 있습니다.

중요 사항: 사람이 제어하는 장치/지갑에 결합된 디지털 신원으로 서명 크리덴셜을 발급하는 방식을 통해 "인간 개입(human-in-the-loop)" 상호작용을 구현할 수 있습니다.

이 접근 방식은 시맨틱 명확성, 암호학적 보증, 그리고 법적 구속력이 있는 행위(인간 또는 자동화 에이전트에 의해 개시되는 경우 모두)를 포함하는 사용 사례 전반의 상호운용성을 증진합니다. 또한 Gaia-X 신뢰 프레임워크(Trust Framework)에서 정의된 트러스트 앵커(Trust Anchor)와 정책이 각 서명 크리덴셜을 독립적으로 검증할 수 있게 합니다.

### 6.3.1 SignatureCredential 특화를 활용한 다중 서명[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#multiple-signatures-using-signaturecredential-specializations "Permanent link")

ICAM 문서에서 정의한 신뢰 모델의 **SignatureCredential**은 참여자들이 다양한 맥락에서 제공해야 하는 범용적이고 기계 판독 가능한 *서명*을 나타냅니다. 가장 중요한 맥락 중 하나는 데이터 교환 문서(Data Exchange Document)(버전…)의 [데이터 트랜잭션(Data Transaction)](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/...) 섹션으로, 이 크리덴셜은 **[데이터 이용 계약(Data Usage Agreement)](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/...)**과 **데이터 제품 이용 계약(Data Product Usage Contract)**에 서명하는 데 사용됩니다.

이 크리덴셜의 개념은 컴플라이언스 서비스가 참여자 크리덴셜(Participant Credential) 및 서비스 제공 크리덴셜(Service Offering Credential)을 발급하는 방식("credentialSubject" 클레임 사용)과 동일하며, **credentialSubject**는 다음으로 구성됩니다:

| 속성 | 타입.값/어휘 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| `type` | string | 예 | 서명할 주체의 *유형*을 나타냄 |
| `id` | URI | 예 | 서명할 주체를 식별하는 [VC 명세](https://www.w3.org/TR/vc-data-model-2.0/#identifiers)에서 정의한 단일 확인 가능한 URI |
| `digestSRI` | String | 예 | [W3C VC 데이터 모델 v2.0](https://www.w3.org/TR/vc-data-model-2.0/#integrity-of-related-resources)에서 정의한 관련 리소스의 무결성(digestSRI) - 참조된 리소스가 변경·수정·위조되지 않았음(시간이 지나도 동일함)을 보장 |

또 다른 중요한 요소는, 이 크리덴셜을 법적 효력이 있는 인증서(예: eIDAS)에 결합된 **검증 수단(verificationMethod)**으로 발급하고 서명하면 동일한 수준의 신뢰를 확보할 수 있으며, **서명 확인 유형(Signature Check Type)**의 `gx:legalValidity` 속성(gx:signers 속성 참조)을 검증할 수 있게 됩니다.

#### 6.3.1.1 SignedAgreementCredential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#signedagreementcredential "Permanent link")

**SignedAgreementCredential**은 **SignatureCredential**의 특화 유형으로, 참여자가 특정 주체(예: 데이터 이용 계약, GDPR 계약 등)에 대해 제공하는 *취소 가능한 서명 계약(Revocable Signed Agreement)*을 나타냅니다. **SignatureCredential**과의 유일한 차이점은 폐기(revocation)가 가능하다는 점입니다.

#### 6.3.1.2 데이터 이용 계약 예시[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#data-usage-agreement-example "Permanent link")

데이터 트랜잭션(Data Transaction)에서 **데이터 제공자(Data Provider)**(did:web:provider.com)와 **데이터 소비자(Data Consumer)**(did:web:consumer.com)는 **데이터 이용 계약(Data Usage Agreement)**(**id**: "https://provider.com/data-usage-contract.654321")에 합의해야 하며, 각 참여자가 발급하고 서명할 수 있는 **검증 가능한 크리덴셜(Verifiable Credential)** 형태의 "서명"으로 이를 처리합니다.
이 방식을 통해 모든 참여자가 계약을 참조하는 SignatureCredential을 발급하면, 모든 서명이 포함된 검증 가능한 프레젠테이션(Verifiable Presentation)을 생성할 수 있습니다.

다음은 CredentialSignature 활용 예시입니다:

```
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://w3id.org/gaia-x/development#"
  ],
  "type": [
    "VerifiableCredential"
  ],
  "id": "https://consumer.com/data-usage-contract-signatures.123456",
  "issuer": "did:web:consumer.com",
  "validFrom": "2023-07-28T12:31:49.074Z",
  "validUntil": "2023-10-26T12:31:49.074Z",
  "credentialSubject": {
    "type": "gx:dataUsageAgreement",
    "id": "https://provider.com/data-usage-contract.654321",
    "digestSRI": "sha384-lHKDHh0msc6pRx8PhDOMkNtSI8bOfsp4giNbUrw71nXXLf13nTqNJoRp3Nx+ArVK"
  },
  "credentialStatus": {
    "id": "https://consumer.com/status/1#127",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "127",
    "statusListCredential": "https://consumer.com/credentials/status/1"
  }
}
```

```
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://w3id.org/gaia-x/development#"
  ],
  "type": [
    "VerifiableCredential"
  ],
  "id": "https://provider.com/data-usage-contract-signatures.987",
  "issuer": "did:web:provider.com",
  "validFrom": "2023-07-25T10:31:49.074Z",
  "validUntil": "2023-10-25T10:31:49.074Z",
  "credentialSubject": {
    "type": "gx:dataUsageAgreement",
    "id": "https://provider.com/data-usage-contract.654321",
    "digestSRI": "sha384-lHKDHh0msc6pRx8PhDOMkNtSI8bOfsp4giNbUrw71nXXLf13nTqNJoRp3Nx+ArVK"
  },
  "credentialStatus": {
    "id": "https://provider.com/status/3#125221",
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "125221",
    "statusListCredential": "https://provider.com/credentials/status/3"
  }
}
```

## 6.4 ICAM 시맨틱 모델을 활용한 에코시스템 온보딩 및 오프보딩[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#ecosystem-onboarding-and-offboarding-using-icam-semantic-model "Permanent link")

ICAM 시맨틱 모델은 에코시스템 내 참여자의 온보딩(onboarding) 및 오프보딩(offboarding)을 지원하며, 페더레이션 전반에 걸쳐 일관된 신뢰와 상호운용성을 보장합니다.  
신뢰 범위(Trust Scope)를 정의하면, 참여에 필요한 크리덴셜 유형, 정책, 신뢰 발급자(trusted issuer)를 명시함으로써 에코시스템 내 상호 인정(mutual recognition)의 경계를 확립합니다.  
신뢰 발급자(Trusted Issuer)는 정의된 신뢰 범위를 준수하는 검증 가능한 크리덴셜(당사자 크리덴셜 및 온보딩 크리덴셜 등)을 발급할 권한을 인정받은 주체입니다.  
온보딩 과정에서 엔티티는 당사자 크리덴셜의 특화 유형인 온보딩 크리덴셜(Onboarding Credential)을 받습니다. 이 크리덴셜은 해당 엔티티가 에코시스템이 정의한 모든 정책·신원·컴플라이언스 요건을 성공적으로 충족했음을 증명합니다. 이 크리덴셜을 통해 엔티티는 동일한 신뢰 프레임워크 하에서 다른 데이터 스페이스 참여자들과 상호운용 가능한 신뢰 참여자(trusted participant)로 활동할 수 있습니다.  
반대로, 오프보딩은 온보딩 크리덴셜의 폐기(revocation)를 통해 이루어지며, 이를 통해 해당 엔티티의 신뢰 기반 상호작용 참여가 종료됩니다. 폐기 이벤트는 신뢰 인프라에 등록되어, 모든 연관 시스템이 검증 가능한 크리덴셜 메커니즘을 통해 업데이트된 상태를 확인할 수 있습니다.

## 6.5 접근 권한 위임(Delegating Access Rights)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#delegating-access-rights "Permanent link")

에코시스템은 자기주권 신원(Self-Sovereign Identity, SSI) 기반의 탈중앙화 신원 및 접근 관리를 활용하여 보안성, 프라이버시, 유연성을 강화합니다. 조직은 중앙 신원 제공자(central identity provider)에 의존하지 않고 직원들에게 다양한 클라우드(예: 이메일, 문서 스토리지, 협업 도구)에 대한 안전한 접근 권한을 부여할 수 있습니다. HR 부서 또는 담당 관리자는 직원이 조직을 떠나거나 직책이 변경될 경우 해당 직원의 역할을 폐기하거나 변경할 수 있습니다.

### 6.5.1 크리덴셜 유형 및 발급자[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#types-of-credentials-and-issuers "Permanent link")

**직원 크리덴셜(Employee Credential, 특화된 PartyCredential)**

회사 HR 부서는 각 직원에게 직원 크리덴셜(Employee Credential)을 발급합니다. 이 크리덴셜에는 직원의 고유 식별자, 역할, 부서, 그리고 회사의 고유 ID(에코시스템 온보딩 단계에서 사용된 고유 식별자)가 포함됩니다. 직원 크리덴셜은 직원의 신원과 회사 소속을 검증하는 데 사용됩니다. 회사 ID는 에코시스템의 멤버십 신뢰 목록(membership trustlist)에 등록되어야 하며, 별도로 발급된 멤버십 크리덴셜에도 동일하게 사용됩니다. HR 부서는 직원이 퇴직하는 경우 해당 직원의 크리덴셜을 반드시 폐기해야 하며, 해당 직원은 회사를 대신하여 어떤 클라우드 서비스에도 접근해서는 안 됩니다.

참고사항

직원 크리덴셜의 유형과 속성은 표준화되어야 합니다. `EmployeeCredential`은 `AccessEntitlementCredential`을 받기 위한 전제 조건이며, 조직 내 직원의 신원을 확립하는 데 사용됩니다.

- **유형**: `EmployeeCredential (특화된 Party-Credential)`
- **발급자**: HR 부서
- **주체**: 직원
- **회사 ID**: 회사 또는 조직의 전역 고유 식별자(예: GLEIF ID, 부가가치세 번호 등), 모든 직원에게 동일하게 적용. 회사 ID는 멤버십 신뢰 목록과 크리덴셜의 진위 검증에 사용되는 멤버십 크리덴셜에 활용되어야 합니다.
- **직원 속성**: 직원 ID, 이름, 역할, 부서 등

**접근 권한 크리덴셜(Access Entitlement Credentials)**

관리자(Manager)는 직원의 역할과 책임에 따라 특정 클라우드 서비스에 대한 접근 권한을 부여하기 위해 AccessEntitlementCredential을 발급합니다. 관리자는 이 크리덴셜을 폐기하여 접근 권한을 동적으로 관리할 수 있습니다.
EmployeeCredential은 AccessEntitlementCredential을 받기 위한 전제 조건입니다. 관리자는 해당 크리덴셜을 발급할 권한이 있어야 하며, 다음 조건을 반드시 준수해야 합니다:

- HR 부서가 발급한 유효한 ManagerCredential을 보유해야 합니다.
- 에코시스템의 구성원 관리자(managing member)여야 합니다.
- 크리덴셜에 회사 ID가 포함되어 해당 관리자가 회사의 유효한 구성원임을 보장해야 합니다.

따라서 관리자는 특정 에코시스템 서비스의 멤버십 신뢰 목록에 등록되고, 동시에 유효한 멤버십 크리덴셜을 보유해야 합니다.

- **유형**: `AccessEntitlementCredential` (각 접근 권한별로 개별 크리덴셜을 발급해야 합니다)
- **발급자**: 직원 관리자(Employee Manager)
- **속성**: 직원 ID, 접근 권한(직원이 접근할 수 있는 특정 클라우드 서비스)
- **목적**: 직원이 접근 권한을 갖는 서비스를 명시합니다.
- **범위**: 담당 관리자가 직원의 역할과 책임에 따라 특정 서비스에 대한 접근 권한을 부여하기 위해 발급합니다.
- **폐기(Revocation)**: 관리자가 크리덴셜을 폐기하여 접근 권한을 동적으로 관리할 수 있습니다. <!–발급자/직원 관리자와 다를 수 있음?>
- **직원 ID**: 직원의 `EmployeeCredential`은 `AccessEntitlementCredential`을 받기 위한 전제 조건입니다.

**인증 프로세스(Authentication Process)**

1. **직원의 크리덴셜 제시**: 서비스에 접근할 때 직원은 `EmployeeCredential`과 `AccessEntitlementCredential`을 제시합니다.
2. **검증**: 서비스는 다음을 검증합니다:
3. 크리덴셜의 진위(HR 부서 및 담당 관리자가 발급했는지 확인).
4. 크리덴셜의 유효성(폐기되지 않았는지 확인).
5. 속성이 접근 제어 정책과 일치하는지(예: 직원의 역할 및 권한이 접근하려는 서비스에 부합하는지).

**폐기 프로세스(Revocation Process)**

**폐기 목록 또는 레지스트리**: HR 부서와 관리자는 인증 프로세스 중 서비스가 확인하는 폐기 목록 또는 레지스트리에 크리덴셜을 추가하여 폐기할 수 있습니다.

- **발급자**: `EmployeeCredential`의 경우 HR 부서, `AccessEntitlementCredential`의 경우 관리자.
- **메커니즘**: 아키텍처에 따라 분산 식별자(DID) 기반 폐기 메커니즘 또는 중앙화된 폐기 서비스를 활용할 수 있습니다.

### 6.5.2 구현 고려 사항[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#implementation-factors "Permanent link")

- **분산 식별자(Decentralized Identifiers, DIDs)**: 직원, HR, 관리자에게 DID를 활용하여 탈중앙화된 자기주권 신원(self-sovereign identity) 시스템을 구현합니다.
- **검증 가능한 데이터 레지스트리(Verifiable Data Registry)**: DID 검증을 위한 검증 가능한 데이터 레지스트리를 구현합니다.
- **프라이버시**: 직원 프라이버시를 보호하기 위해 인증 및 접근 제어에 필요한 최소한의 정보만 공개하도록 시스템을 설계합니다.
- **상호운용성**: 크리덴셜 스키마를 W3C 검증 가능한 크리덴셜(Verifiable Credentials) 표준과 호환되고 클라우드 서비스의 접근 제어 메커니즘과 연동 가능하도록 설계합니다.
- **신뢰**: 에코시스템은 다수의 신뢰 목록(Gaia-X, XFCS 에코시스템 구성원, 서비스 관리자)을 보유할 수 있습니다.

November 28, 2025


November 28, 2025
