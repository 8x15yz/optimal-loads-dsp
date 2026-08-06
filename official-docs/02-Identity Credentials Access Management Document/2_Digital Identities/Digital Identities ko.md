# 4. 디지털 신원 (Digital Identities)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#digital-identities "Permanent link")

## 4.1 개요[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#overview "Permanent link")

디지털 신원(Digital Identity)은 사람, 조직, 서비스 등의 엔티티(Entity)가 리소스에 대한 인증(Authentication), 권한 부여(Authorisation), 그리고 신뢰 기반 접근을 위해 사용하는 디지털 속성과 자격증명의 집합입니다.
디지털 신원은 신뢰할 수 있는 당사자가 발급하고 신원 주체에 대한 클레임(Claim)을 인코딩한 하나 이상의 검증 가능한 자격증명(Verifiable Credential)으로 표현될 수 있습니다.
각 디지털 신원은 암호화 키 쌍(Key Pair)에 고정됩니다. 개인 키(Private Key)는 보유자(Holder)가 관리하며, 이에 대응하는 공개 키(Public Key)는 DID 문서(DID Document) 내 검증 방법(Verification Method)을 통해 공개되어 서명 검증 및 발급자 인증에 활용됩니다.

에코시스템(Ecosystem) 내에서 발급되는 모든 자격증명은 발급자(Issuer)의 신원을 주체의 고유 신원과 연결해야 합니다. 에코시스템 거버넌스 기관(Ecosystem Governance Authority)은 신뢰 프레임워크(Trust Framework) 내에서 허가된 자격증명 유형, 신원 범주, 허용 가능한 작업을 정의합니다.

다음 섹션에서는 에코시스템 내에서 신원 및 자격증명 작업을 지원하기 위해 다양한 키 쌍 유형과 신뢰 수준이 어떻게 적용되는지 설명합니다.

## 4.2 디지털 신원의 운영 역할 및 키 쌍 활용[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#operational-roles-of-digital-identities-and-key-pair-usage "Permanent link")

에코시스템 내에서 디지털 신원은 각기 다른 목적을 수행합니다. 에코시스템 거버넌스 기관이 온보딩 과정에서 발급하는 신원은 식별·인증·권한 부여(IAA, Identification, Authentication, and Authorisation) 작업을 지원합니다. 이 작업에는 에이전트 간 보안 통신 및 정책 집행 등이 포함됩니다.
전자 신원 확인(eID) 및 전자 서명(eSignature)에 사용되는 신원은 신뢰할 수 있는 거래를 가능하게 하며, 보증 수준(Assurance Level)은 거버넌스 기관이 정의합니다. eID 서비스는 온보딩 과정에서의 참여자(Participant) 검증을 간소화하는 데에도 활용될 수 있습니다.

아래의 워크플로 다이어그램은 디지털 신원이 자격증명 서명에 어떻게 사용되는지, 신뢰 서비스 제공자(Trust Service Provider, TSP)와 어떻게 연결되는지, 그리고 에코시스템 아키텍처 전반에 걸쳐 검증 방법이 어떻게 연결되는지를 보여줍니다.

[![그림 1: 디지털 신원의 활용](images/DigitalIdentitiesClassification-Simpl-Open_Integration.png)](./Digital Identities - Identity, Credential and Access Management Document - local Release_files/DigitalIdentitiesClassification-Simpl-Open_Integration.png)
*그림 4.2 - 디지털 신원의 활용*

사용 사례에 따라 키 쌍은 자가 발급(Self-issued)되거나, 가명(Pseudonymous, 검증된 신원과 연결되지 않음)으로 사용되거나, 신뢰 서비스 제공자(TSP)의 인증을 받을 수 있습니다. 보증 또는 규제 요건에 따라 서로 다른 TSP를 활용할 수 있습니다.

### 4.2.1 자가 인증 식별자 (Self-certified Identifiers)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#self-certified-identifiers "Permanent link")

유효한 암호화 키 쌍은 인증서나 사람·엔티티의 명시적 식별자와 결합되지 않아도 존재할 수 있습니다. 예를 들어, DID Key는 검증 방법으로 사용될 수 있습니다. DID Key는 공개 키와 알고리즘을 식별하며, 주체가 필요에 따라 해당 키에 연결된 클레임을 제시할 수 있도록 합니다.

### 4.2.2 자가 서명 인증서 (Self-signed Certificates)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#self-signed-certificates "Permanent link")

이 모델에서는 엔티티가 제3자 인증 기관(Certificate Authority)으로부터 인증서를 발급받는 대신 자체적으로 X.509 인증서를 생성하고 서명합니다. 이는 신뢰 서비스 제공자(TSP)가 발급한 인증서에 비해 외부 신뢰 보증 수준이 낮습니다. 에코시스템 거버넌스 기관은 신뢰 프레임워크 내에서 자가 서명 인증서를 사용할 수 있는 신원 유형과 맥락을 정의합니다.

### 4.2.3 신뢰 서비스 제공자(TSP) 키 쌍[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#trust-service-provider-tsp-keypair "Permanent link")

이 경우, 적격 신뢰 서비스 제공자(Qualified Trust Service Provider)가 인증서를 발급하고 적격 서명 생성 장치(QSCD, Qualified Signature Creation Device) 또는 하드웨어로 보호된 개인 키를 제공하여 개인 키에 직접 접근할 수 없도록 보장합니다. TSP는 고객 확인 절차(KYC, Know Your Customer) 및 기업 확인 절차(KYB, Know Your Business)를 수행하고 폐기 메커니즘을 유지하므로, 해당 인증서는 진본이며 유효한 것으로 간주됩니다. TSP 또는 발급 인증 기관은 검증자(Verifier)가 상태를 조회할 수 있도록 인증서 폐기 목록(CRL, Certificate Revocation List) 또는 온라인 인증서 상태 프로토콜(OCSP, Online Certificate Status Protocol) 엔드포인트를 공개합니다.

## 4.3 디지털 신원과 클레임의 결합[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#binding-digital-identities-to-claims "Permanent link")

발급자가 클레임을 제공할 때, 해당 클레임이 신뢰할 수 있고 권한이 있는 출처에서 비롯된 것임을 보장하기 위해 발급자의 디지털 신원을 반드시 검증해야 합니다(MUST).
검증된 디지털 신원을 사용하는 발급자는 에코시스템 거버넌스 프레임워크에서 정의한 적격성 및 보증 요건을 준수해야 합니다(SHOULD).
X.509 인증서가 법적으로 인정되고 검증된 법적 신원에 결합될 경우, 발급된 클레임에 대한 서명은 의존 당사자(Relying Party)에게 보증 및 법적 가치를 높여줍니다. 특히 발급자가 에코시스템 레지스트리(Registry)에 등록되어 있고 CRL/OCSP를 공개하는 경우 더욱 그러합니다.

예를 들어, 디지털 계약이 검증 가능한 자격증명으로 표현될 경우, 적격 디지털 신원(예: 법적으로 인정된 전자 서명)으로 서명하면 법적 집행력이 부여됩니다.

검증된 클레임은 이후 접근 제어 엔진(예: 정책 결정 포인트, Policy Decision Point)에 의해 평가되어 참여자의 행동 및 리소스 접근을 승인합니다.

### 4.3.1 사용 사례별 상이한 요건[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#different-requirements-based-on-use-cases "Permanent link")

디지털 신원에 대한 요건은 사용 사례 및 에코시스템 맥락에 따라 다릅니다.

**예시: 대학 시나리오**
대학 에코시스템에서 학생, 교수, 관리자 등의 참여자는 각기 다른 수준의 신원 보증 및 접근 권한을 필요로 합니다.
내부 접근 제어에는 단순한 키 쌍 기반 신원으로도 충분하지만, 학생 의사가 환자 정보에 접근하는 의과대학과 같이 민감한 맥락에서는 더 높은 보증 수준과 법적 적격 신원(예: eIDAS 준수 신뢰 서비스에서 발급된 인증서)이 요구됩니다.

## 4.4 DID 확인 (DID Resolution)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#did-resolution "Permanent link")

검증 가능한 자격증명이 검증을 위해 제출될 때(예: 디지털 클리어링 하우스(Digital Clearing House)에 제출 시), DID 확인(DID Resolution) 프로세스는 해당 자격증명 발급자의 DID 문서를 조회합니다.
이 프로세스를 통해 자격증명의 서명을 검증하고 발급자의 에코시스템 내 신뢰 관계를 확인하는 데 필요한 발급자의 검증 방법(공개 키 등) 및 서비스 엔드포인트가 공개됩니다.

자격증명이 X.509 인증서 체인에 의존하는 경우, 검증자는 해당 체인이 에코시스템 레지스트리에서 인정하는 루트 인증 기관(Root Certificate Authority)까지 연결되는지 반드시 확인해야 합니다(MUST).
비즈니스 또는 라이선스 시나리오에서 검증 가능한 자격증명에는 조직명, 법적 주소, 연락처 정보 등의 클레임이 포함될 수 있습니다. 이러한 속성은 일반적으로 법적 대리인을 대신하는 신뢰 서비스 제공자(TSP)에 의해 검증됩니다.

일부 프로세스에서는 추가적인 권한 부여 또는 보증 단계가 필요할 수 있으며, 검증자는 DID 문서에 참조된 암호화 자료(Cryptographic Material)를 사용하여 신원 제어권과 무결성을 확인합니다.

각 검증 가능한 자격증명은 단일 제어 디지털 신원을 참조해야 합니다(MUST). 이를 통해 DID가 확인될 때 해당 컨트롤러(Controller)가 관련 암호화 키를 관리함을 보장합니다. 확인 프로세스는 암호화 자료뿐만 아니라 DID 문서의 최종 업데이트 시간, 컨트롤러, 검증 방법 등 DID가 어디서 언제 확인되었는지에 관한 메타데이터도 함께 노출합니다. 이를 통해 에코시스템 내 모든 참여자가 다른 참여자에게 역할과 권한을 부여하거나 취소하는 데 활용할 수 있는 확인 가능한 신원 체인 전체와 포괄적인 감사 추적(Audit Trail) 및 신뢰 검증이 가능해집니다.

### 4.4.1 검증 방법 (JSON 웹 키, JSON Web Key)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#verification-method-json-web-key "Permanent link")

Gaia-X 에코시스템에서 디지털 신원의 지정 검증 방법은 RFC 7517에 정의된 JSON 웹 키(JWK, JSON Web Key) 형식입니다.
주체의 신원 레코드(DID 문서 또는 이에 상응하는 참조 등)는 반드시 `publicKeyJwk` 파라미터를 공개하거나, JSON 웹 키 셋(JWKS, JSON Web Key Set)으로 확인되는 `jwks_uri`를 참조해야 합니다(MUST).
검증 시, 검증자는 JWK 또는 JWKS 엔드포인트를 조회하고 키 식별자(`kid`)를 검증한 후, 공개 키 자료를 사용하여 자격증명의 서명을 확인합니다. 이를 통해 해당 키가 지정된 신원 컨트롤러에 의해 제어되며, 에코시스템의 신뢰 레지스트리(Trust Registry)와 일치하고, 자격증명의 진본성(Authenticity) 및 무결성(Integrity)의 암호화 증명에 적합함을 보장합니다.

구현 시, 검증자가 현재 키를 가져오고, 키 교체를 확인하며, 접근 승인 전 폐기 여부를 확인할 수 있도록 `jwks_uri` 및 상태 엔드포인트를 제공해야 합니다(SHOULD).

#### 4.4.1.1 보증 및 신뢰 메커니즘[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#assurance-and-trust-mechanisms "Permanent link")

**KYC/KYB 프로세스**: 신뢰 서비스 제공자(TSP)가 자연인(Natural Person) 및 법인(Legal Entity)의 신원을 확인하는 데 사용됩니다.

**인증서 체인 검증(Certificate Chain Validation)**: 포함된 X.509 인증서가 에코시스템 레지스트리에서 인정하는 루트 인증 기관(Root CA)까지의 신뢰 경로를 가지고 있는지 검증합니다.

**폐기 확인(Revocation Checking)**: 인증서 폐기 목록(CRL) 또는 온라인 인증서 상태 프로토콜(OCSP)과 같은 메커니즘을 사용하여 인증서 또는 키가 폐기되지 않았음을 확인합니다.

**DID 확인(DID Resolution)**: 암호화 검증에 필요한 검증 방법(JWK), 공개 키, 서비스 엔드포인트가 포함된 DID 문서를 조회합니다.

##### 4.4.1.1.1 자기 주권 신원 (SSI, Self-Sovereign Identity) 구현[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#self-sovereign-identity-ssi-implementation "Permanent link")

SSI(자기 주권 신원)가 지원되는 에코시스템에서 참여자는 당사자 자격증명 특수화(Party Credential Specialization)를 통해 거버넌스 기관으로부터 수신한 클레임의 일부를 위임할 수 있습니다. 단일 키 쌍이 인증과 서명 작업 모두를 위한 이중 기능을 수행할 수 있습니다. 참여자는 공개적으로 검증 가능한 클레임을 신원 확인에 활용하여 의존 당사자(Relying Party)에 접근하기 위한 액세스 토큰(Access Token)을 발급받습니다. 검증 가능한 자격증명으로 SSI를 구현할 때, 암호화 무결성과 명확한 책임 추적을 유지하기 위해 모든 클레임은 여러 키 쌍이 아닌 단일 키 쌍에 결합되어야 합니다(MUST).

## 4.5 eIDAS 통합[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#eidas-integration "Permanent link")

Gaia-X에서 디지털 신원은 (i) 검증 가능한 자격증명(VC)으로서 클레임을 검증하거나 (ii) 아티팩트(Artefact) 또는 트랜잭션에 서명하는 데 사용될 수 있으며, 에코시스템은 각 작업에 요구되는 보증 수준을 지정합니다.

[eIDAS 규정(eIDAS Regulation)](https://digital-strategy.ec.europa.eu/en/policies/discover-eidas)은 유럽연합(EU) 전역에서 전자 신원 확인과 신뢰 서비스를 위한 프레임워크를 수립합니다.
에코시스템 내에서 eIDAS 준수 메커니즘은 신원 및 서명 목적 모두에 활용될 수 있으며, 법적 인정과 국경 간(Cross-border) 상호 운용성을 보장합니다.

eIDAS 적격 인증서(Qualified Certificate)를 보유한 엔티티는 이를 사용하여 검증 가능한 자격증명(VC)에 서명할 수 있습니다. 해당 인증서가 EU 법에 따라 법적 구속력을 가질 경우, 결과 서명은 자격증명에 법적 가치를 부여합니다.
eIDAS를 지원하는 모든 신뢰 서비스 제공자(TSP)는 반드시 [EU 신뢰 목록(EUTL, EU Trusted List)](https://eidas.ec.europa.eu/efda/trust-services/browse/eidas/tls)에 적격(Qualified)으로 등재되어야 하며(MUST), 인증된 적격 서명 생성 장치(QSCD) 또는 보안 하드웨어 모듈 내에서 개인 키를 보호해야 합니다.

eIDAS는 두 가지 주요 서비스 도메인을 정의합니다:

**신뢰 서비스(Trust Services)**: 전자 서명, 봉인(Seal), 타임스탬프(Timestamp) 및 관련 서비스의 생성과 검증에 사용됩니다.

**전자 신원 확인 서비스(Electronic Identification Services, eID)**: EU 회원국 전반에서 자연인 또는 법인을 인증하고 식별하는 데 사용됩니다.

예를 들어, EU의 한 국가에 있는 개인은 자국에서 발급된 eID를 사용하여 다른 회원국의 공식 데이터(연금 또는 대학 기록 등)에 인증 및 접근할 수 있습니다.
이러한 서비스는 eIDAS 및 디지털 신원 툴박스(Digital Identity Toolbox)에서 제공하는 재사용 가능한 구성 요소(Building Block)를 적용하여 에코시스템 프레임워크에 통합할 수 있습니다.

### 4.5.1 eID[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#eid "Permanent link")

eID(전자 신원 확인)는 전자 서명(Electronic Signing)이 아닌 인증(Authentication) 및 신원 확인(Identification) 전용으로 사용됩니다.
예를 들어, 시민이 eID를 사용하여 공공 행정 포털에 로그인하고 법적으로 자신을 식별합니다.

eID 서비스를 제공하는 모든 신뢰 서비스 제공자(TSP)는 반드시 eIDAS에 따라 공식적으로 인정되어 EU 신뢰 목록에 등재되어야 하며(MUST), 이를 통해 회원국 간 디지털 신원의 상호 인정이 가능해집니다.
이로써 개인은 자국의 eID를 사용하여 다른 EU 국가의 온라인 서비스에 접근할 수 있습니다.
(자세한 내용은 [eID](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467109809/What+is+eID) 및 [eID FAQ](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467109253/eID)를 참조하세요.)

### 4.5.2 전자 서명 (eSignature)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#esignature "Permanent link")

전자 서명(eSignature)은 문서 또는 데이터셋의 내용에 동의하거나 승인하려는 사람의 의도를 나타냅니다. 수기 서명과 마찬가지로, 전자 서명은 서명자가 서명한 내용에 법적으로 구속될 의사를 표현합니다.
eIDAS 내에서 전자 서명은 검증 가능한 자격증명(VC) 또는 기타 디지털 증명에 대한 적격 전자 서명을 생성하고 검증하는 데 사용될 수 있습니다.

법적으로 유효한 서명을 위해서는 참여자가 eIDAS 적격 인증서와 적격 전자 서명(QES, Qualified Electronic Signature)을 발급하거나 관리하는 적격 신뢰 제공자를 사용해야 합니다.
eIDAS는 EU 프레임워크이지만, 다른 관할권의 적격 신뢰 제공자도 국경 간 사용 사례에 대한 동등한 메커니즘을 지원할 수 있습니다.

eIDAS에 따른 전자 서명 수준:

**단순 전자 서명(SES, Simple Electronic Signature)**: 동의를 나타내는 모든 전자 데이터 (예: 이메일에 이름 타이핑).

**고급 전자 서명(AdES, Advanced Electronic Signature)**: 서명자를 고유하게 식별하고 연결할 수 있으며, 서명된 데이터의 변조를 탐지할 수 있습니다.

**적격 전자 서명(QES, Qualified Electronic Signature)**: 적격 서명 생성 장치(QSCD)를 사용하여 생성되고 적격 인증서에 기반한 AdES입니다.

**원격 적격 서명(Remote Qualified Signature)**: 인증된 QSCD 서비스를 통해 적격 신뢰 서비스 제공자가 원격으로 관리하는 QES입니다.

전자 서명은 검증 가능한 자격증명과 결합하여 탈중앙화 신원(Decentralised Identity) 에코시스템 내에서 법적 구속력 있는 증명을 가능하게 합니다.
(자세한 내용은 [전자 서명 FAQ(eSignature FAQ)](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/880312429/eSignature+FAQ)를 참조하세요.)

## 4.6 머신과 사람 간의 상호작용 구현[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#implementing-interactions-between-machines-and-humans "Permanent link")

Gaia-X 디지털 신원 맥락에서 상호작용은 사람이 개입하는 방식(Human-in-the-Loop)과 완전히 자동화된 머신 간(Machine-to-Machine) 프로세스 모두를 포함할 수 있습니다. 사양은 두 가지 방식을 모두 지원하면서 강력한 디지털 신원 증명을 통한 법적 준수와 신뢰를 보장해야 합니다. 아래에서는 각 방식을 처리하는 방법을 설명합니다.

### 4.6.1 사람이 개입하는 상호작용 (Human-in-the-Loop)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#interactions-with-human-in-the-loop "Permanent link")

특정 신원 트랜잭션 또는 [데이터 이용 계약(DUA, Data Usage Agreement)](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/) 워크플로는 완료 전에 명시적인 사람의 승인이 필요합니다. 이러한 시나리오에서는 자동화가 일시 중단되어 사람의 동의 또는 서명을 받아야 합니다.

#### 4.6.1.1 사람의 서명에 대한 법적 요건[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#legal-requirements-for-human-sign-off "Permanent link")

EU eIDAS 프레임워크에 따라 일부 승인은 자연인이 직접 제공해야 합니다. 예를 들어, 수기 서명과 동등한 적격 전자 서명(QES)은 적격 인증서를 보유한 검증된 사람 서명자만이 생성할 수 있습니다. 법적 구속력 있는 서명이 필요한 경우(예: 계약서 서명 또는 동의), 워크플로는 반드시 일시 중단하고 사용자가 개인 자격증명으로 서명하도록 전달해야 합니다(MUST).

#### 4.6.1.2 암호화 방식으로 검증 가능한 사람 결합[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#cryptographically-verifiable-human-binding "Permanent link")

시스템은 개인의 신원을 서명에 연결하는 자격증명을 사용해야 합니다(SHOULD). 적격 인증서는 각 서명자에게 발급되어 높은 보증 수준을 보장합니다. 인증서의 개인 키는 사용자의 단독 제어 하에 있으며(예: 스마트카드 또는 하드웨어 토큰), 생성된 서명은 해당 인증서를 통해 검증될 수 있습니다. 이 연결은 특정 개인이 트랜잭션을 승인했음을 증명하는 부인 방지(Non-repudiation)를 제공합니다.

#### 4.6.1.3 적격 제공자 및 개인 지갑[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#qualified-providers-and-personal-wallets "Permanent link")

구현 시 적격 신뢰 서비스 제공자와 사용자 결합 신원 지갑(Identity Wallet)을 통합해야 합니다(SHOULD). Gaia-X는 eIDAS 적격 인증서 발급자를 프레임워크의 신뢰 앵커(Trust Anchor)로 인정합니다. 각 사용자는 EU 디지털 신원 지갑(EU Digital Identity Wallet) 등의 신원 지갑에 개인 자격증명과 키를 보관합니다. 민감한 작업(예: DUA 서명)에 사람의 개입이 필요한 경우, 시스템은 사용자의 지갑을 통해 세부 내용을 검토하고 적격 서명을 적용하도록 안내합니다. 워크플로는 유효한 사람의 서명 또는 동의가 확인된 후에만 재개되며, 이를 통해 법적 요건 준수를 보장합니다.

### 4.6.2 머신 간의 상호작용 (M2M)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#interactions-with-machines "Permanent link")

많은 Gaia-X 시나리오는 사람의 개입 없이 머신 또는 서비스 간의 완전히 자동화된 교환에 의존합니다. 이러한 상호작용은 탈중앙화 신원 자격증명(Decentralised Identity Credential), 디지털 서명, 신뢰 프레임워크를 활용하여 머신 간 상호 인증을 가능하게 합니다.

#### 4.6.2.1 자동화된 자격증명 교환[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#automated-credential-exchange "Permanent link")

Gaia-X는 머신 간 통신(M2M, Machine-to-Machine) 프로세스에서 사람의 확인 대신 검증 가능한 자격증명(Verifiable Credential)을 사용합니다. 서비스(보유자)가 서명된 자격증명을 다른 서비스(검증자)에게 전송하면, 검증자의 소프트웨어는 즉시 서명을 검증하고 발급자가 신뢰할 수 있는지 확인합니다. 이는 암호화 검증을 통해 이루어지므로 한 서비스가 수동 절차 없이 다른 서비스의 자격증명(준수 여부 또는 속성 등)을 즉시 확인할 수 있습니다.
자세한 내용은 "Gaia-X 자격증명(Gaia-X Credentials)" 챕터를 참조하세요.

#### 4.6.2.2 M2M 상호작용에서의 신뢰 수립[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/digital_identities/#establishing-trust-in-m2m-interactions "Permanent link")

사람의 감독 없이 머신은 신뢰 프레임워크와 암호화에 의존하여 자격증명의 유효성을 판단합니다. 검증자는 먼저 자격증명의 발급자가 인정된 기관인지(예: Gaia-X 신뢰 발급자 레지스트리에 등재되어 있는지) 확인합니다. Gaia-X 규칙에 따르면 각 발급자는 등록된 신뢰 앵커(Trust Anchor)이거나 신뢰 앵커에 연결(예: eIDAS 적격 CA 또는 알려진 DID를 통해)되어야 합니다. 머신은 발급자 신뢰가 수립되고 서명 유효성, 만료 여부 등의 기타 검사를 통과한 경우에만 자격증명을 수락합니다. 이러한 자동화된 집행은 머신 간 교환이 사람이 검토한 프로세스와 동일한 신뢰 수준을 유지하도록 보장합니다.

2025년 11월 28일


2025년 11월 28일
