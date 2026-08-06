# 4. 데이터 교환 서비스

## 4.1 데이터 교환 서비스[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-exchange-services/#data-exchange-services "Permanent link")

Gaia-X에서의 데이터 접근 및 데이터 이용은 관련 행위자들이 활용하는 일련의 서비스들에 의해 실현되며, 이 서비스들은 페더레이션 서비스(Federation Services)로 지원됩니다. 이 중 일부는 데이터 접근/이용에 특화되어 있거나 데이터 관련 특성을 포함하며, 이를 데이터 서비스(Data Services)라고 합니다.

아래에 목록이 나열되어 있으며, 이후 장에서 상세히 설명합니다:

Note

모든 데이터 교환 서비스(Data Exchange Services)가 필수는 아닙니다.

- **데이터 제품 카탈로그 서비스(Data Product Catalogue Services)** (필수)는 데이터 제품 설명서(Data Product Descriptions)(메타데이터 포함)를 게시하고 검색을 지원하는 메커니즘을 제공합니다. 데이터 제품 카탈로그 서비스는 데이터 제품(Data Product) 설명의 핵심 프로토콜로 DCAT를 사용한다는 점에서 특화된 서비스입니다. Gaia-X는 데이터 제품을 설명하기 위한 초기 어휘(Vocabularies) 집합을 제공합니다. Gaia-X 데이터 제품 카탈로그는 다양한 (비즈니스 또는 기술) 도메인의 어휘로 확장 가능해야 합니다.
- **데이터 이용 계약 서비스(Data Usage Agreement Services)** (필수)는 데이터 이용 계약(DUA)을 공증/철회하고, 계약의 상태, 유효성(즉, 서명자가 실제로 해당 데이터에 대한 권리를 보유하고 있는지 확인) 및 적용 가능성(즉, 데이터 접근 전제 조건(Data Access Prerequisites)이 충족되었는지 확인)을 검증하는 메커니즘을 제공합니다.
- **데이터 접근 프로토콜(Data Access Protocols)**은 참여자(Participants) 간 데이터를 교환하고 데이터 접근을 실현하기 위해 필요합니다. 데이터 교환은 P2P(peer-to-peer) 방식으로 이루어집니다. Gaia-X는 특정 기술 프로토콜을 강제하지 않으며, 실제 프로토콜은 계약 단계에서 당사자 간에 합의되어야 합니다.
- **데이터 접근 로깅 서비스(Data Access Logging Services)** (선택)는 (a) 데이터가 실제로 접근되었다(즉, 제공 및 수신되었다)는 증거와 (b) 접근 전 데이터 이용 계약(Data Usage Agreement)이 집행되었다는 증거를 제공합니다. 데이터 제공자(Data Providers)는 이 서비스를 활용하여 데이터 권리 보유자(Data Rights Holders) 및 에코시스템 거버넌스 기관(Ecosystem Governance Authority)에게 모든 데이터 접근이 요구 사항에 따라 수행되었음을 증명할 수 있습니다. 또한, 데이터 소비자(Data Consumers)는 SLA 분쟁 발생 시 이 서비스를 활용할 수 있습니다.

### 4.1.1 비특화 서비스[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-exchange-services/#non-specific-services "Permanent link")

데이터 접근/데이터 이용의 전체 생명주기를 실현하기 위해 다른 페더레이션 서비스(Federation Services)도 필요하지만, 이 서비스들은 데이터에 특화된 특성을 갖지 않습니다:

- **인증 및 디지털 서명 서비스(Authentication and Digital Signature Services)** (필수)는 참여자를 식별하고 신뢰할 수 있는 데이터 이용 계약을 기록하는 데 필수적입니다. [Gaia-X 신원, 자격증명 및 접근 관리 문서](https://docs.gaia-x.eu/)에 정의된 사양에 따라 제공됩니다.
- **협상 및 계약 서비스(Negotiation and Contracting Services)** (필수)는 데이터 이용 계약(Data Usage Contracts)을 포함한 서비스 계약(Service Contracts) 협상을 당사자들이 수행할 수 있도록 지원합니다.
- **계약 저장소 서비스(Contract Store Services)** (선택)는 당사자들이 계약(즉, 협상 단계의 결과물)을 공증할 수 있도록 합니다.

이 서비스들에 대한 추가 설명은 본 문서에서 다루지 않습니다.

September 18, 2025


September 18, 2025
