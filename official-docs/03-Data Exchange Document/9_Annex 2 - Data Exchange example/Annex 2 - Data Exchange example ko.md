# 10. 부록 2 - 데이터 교환 예시: 개인 재무 관리(Personal Finance Management)[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/annex-2/#annex-2-data-exchange-example-the-personal-finance-management "Permanent link")

이 예시는 SaaS 방식의 개인 재무 관리(Personal Finance Management, PFM) 서비스의 오픈 뱅킹 시나리오를 통해 다양한 Gaia-X 개념을 설명합니다.

MyPFM이라는 회사가 여러 은행(Bank(1), Bank(2)…)에 계좌를 보유한 최종 사용자(End User) Jane에게 PFM 서비스를 제공한다고 가정합니다.
MyPFM은 각 은행(Bank(i))이 제공하는 서비스를 이용해 Jane의 은행 거래 내역을 수집하고, 이를 집계하여 Jane의 금융 대시보드를 생성합니다.

[![myPFM 예시 그림](images/Gaia-X_Data_Exchanges_Example_myPFM_informal1.svg)](./Annex 2 - Data Exchange example - Data Exchange Document - 25.07 Release_files/Gaia-X_Data_Exchanges_Example_myPFM_informal1.svg)

Jane은 최종 사용자(End User)이자 데이터 권리자(Data Rights Holder) (GDPR에 따른 정보주체)입니다.

Bank(i)는 은행 거래 내역을 전달하는 데이터 제품(Data Product) (서비스 오퍼링(Service Offering))을 정의하는 데이터 제공자(Data Provider)입니다. Bank(i)는 또한 데이터 제품을 구성하는 가상 리소스(Virtual Resource)인 은행 거래 명세서의 리소스 소유자(Resource Owner)이며, 동시에 데이터 생산자(Data Producer)이기도 합니다.
관련 리소스 정책(Resource Policy)은 유럽 의회의 PSD 지침에 의해 사전 정의됩니다. (참고: 이 방식은 현재 DSP2 서비스의 동의 관리 방식과 다르며, 아래에 설명된 프로세스는 2023년 6월에 발표된 *금융 및 보험 데이터 접근(Financial and Insurance Data Access, FIDA)* EU 규정 초안을 기반으로 조정된 것입니다.)

MyPFM은 Bank(i)가 제공하는 데이터(데이터 이용(Data Usage), 서비스 인스턴스(Service Instance))를 소비하여 금융 대시보드를 생성하고 Jane에게 제공하는 데이터 소비자(Data Consumer) (서비스 소비자(Service Consumer))입니다.

MyPFM은 또한 대시보드 생성 코드 실행 등을 위해 PaaS 제공자(PaaS Provider)로부터 서비스 인스턴스(Service Instance)를 소비할 수도 있습니다.

민감한 개인 정보가 포함되어 있기 때문에, Jane은 myPFM이 자신의 데이터를 어떻게 활용할 수 있는지를 정확하게 명시한 특정 "계약"에 서명해야 합니다 (예: 금융 대시보드 작성에만 사용 허용, 수취인 및 지출 카테고리 연결(예: 수취인 X는 식료품점, 수취인 Y는 주유소 등)을 제외한 제3자 전달 금지).

우선 Jane은 자신의 다양한 은행 계좌 번호(IBAN)를 myPFM에 제공합니다. myPFM은 데이터 제품 카탈로그(Data Product Catalogue)를 통해 각 은행의 적절한 서비스를 검색합니다. 편의상 이 서비스들은 모두 GetTransactionFromIBAN으로 명명된 것으로 가정합니다. myPFM은 각 데이터 제품 설명서(Data Product Description)를 검토하여 자신의 요구 사항과 부합하는지 확인합니다. 민감한 개인 정보가 포함되어 있으므로 Bank(i)는 Jane의 서명된 동의서를 요구합니다. 동의 양식 템플릿은 데이터 제품 설명서(Data Product Description)에 포함되어 있습니다. (참고: 에코시스템에서는 자동화되고 신속한 처리를 지원하기 위해 표준화된 동의 템플릿을 사전에 정의해 두는 것이 일반적입니다.) myPFM은 해당 템플릿을 작성한 후, Jane과 myPFM 및 Bank(i) 모두가 신뢰하는 디지털 신원 및 전자 서명 제공자를 통해 Jane에게 서명을 받습니다.
이후 myPFM과 각 Bank(i)는 Jane을 위해 GetTransactionFromIBAN 서비스를 구성하고 계약에 공동 서명합니다.
myPFM은 Jane의 거래 데이터를 요청(Jane의 서명된 데이터 이용 계약(Data Usage Agreement) 첨부)하고, 이를 처리하여 Jane에게 금융 대시보드를 제공합니다.

이제 myPFM이 대출 중개 서비스도 제공한다고 가정합니다. 이를 위해 myPFM은 대출 기관들에게 신용 프로필을 제공하여 대출 제안을 받고, 이를 순위화하여 Jane에게 전달합니다.

[![myPFM 대출 중개 예시 그림](images/Gaia-X_Data_Exchanges_Example_myPFM_informal2.svg)](./Annex 2 - Data Exchange example - Data Exchange Document - 25.07 Release_files/Gaia-X_Data_Exchanges_Example_myPFM_informal2.svg)

이 경우 myPFM은 Bank(i)로부터 데이터를 수신하는 데이터 소비자(Data Consumer)인 동시에, 대출 기관 Lender(i)에게 데이터를 제공하는 데이터 제공자(Data Provider)가 됩니다.
Jane이 이 서비스를 이용하려면, 먼저 myPFM이 일부 대출 기관에 자신의 신용 프로필(총 소득, 대출 한도, 대출 목적 등)을 전달할 수 있도록 새로운 데이터 이용 계약(Data Usage Agreement)에 서명해야 합니다. 이 신용 프로필은 익명으로 처리되어야 하며 Jane을 식별할 수 있어서는 안 됩니다.
이후 myPFM은 데이터 제품 카탈로그(Data Product Catalogue)를 조회하여 온라인 대출 서비스를 제공하는 대출 기관을 검색하고, 해당 데이터 제품 설명서(Data Product Description)를 검토하여 Jane의 데이터 이용 계약(Data Usage Agreement) 및 myPFM 정책과의 준수 여부를 확인합니다.

myPFM은 각 선택된 Lender(i)와 서비스 계약을 협상·구성·서명합니다. 이용 약관에는 Jane의 데이터 이용 계약(Data Usage Agreement)이 포함되지 않습니다. 이는 Lender(i)에게 전달되는 데이터가 이미 익명화되어 있기 때문입니다. 이용 약관에는 myPFM과 Lender(i) 간의 비즈니스에 특화된 조건이 포함됩니다. 예를 들어, myPFM은 일정 기간 동안 대출 제안을 다른 금융 기관에 전달하지 않을 의무가 있으며, myPFM은 Jane이 데이터 수집 업체가 아닌 실제 고객임을 보증합니다. Lender(i)는 x시간 이내에 제안서를 준비할 것을 약속하고, 제안이 채택될 경우 Lender(i)는 myPFM에 일정 금액을 지급합니다.

이후 myPFM은 Lender(i)로부터 getLoanProposal 서비스를 호출합니다. 이 단계에서는 익명의 요청 식별자 외에는 어떠한 데이터도 전송되지 않습니다. Lender(i)는 신용 제안을 준비하기 위해 해당 식별자와 연결된 신용 프로필을 가져와야 합니다. 이를 위해 Lender(i)는 카탈로그에서 myPFM이 제공하는 getLoanRequestData 서비스의 설명서를 확인하고, 이를 구성한 후 공동 서명합니다. 이 단계의 이용 약관에도 Jane의 동의는 포함되지 않지만, Jane의 기본 데이터 이용 계약(Data Usage Agreement)과 동등하거나 더 강력한 조항이 포함되어야 합니다. 예를 들어, 데이터는 신용 제안 작성 목적으로만 사용되어야 하며, 제안이 활성화되지 않을 경우 30일 이내에 삭제되어야 합니다. 이후 Lender(i)는 getLoanRequestData 서비스를 활성화하여 myPFM으로부터 데이터를 가져옵니다. 이 단계에서 myPFM은 데이터 제공자(Data Provider) 역할을 수행하고, Lender(i)는 데이터 소비자(Data Consumer) 역할을 수행합니다. Lender(i)는 이후 대출 제안을 준비하여 myPFM에 제공합니다.

myPFM은 다양한 신용 제안을 수집하고 검토·순위화하여 Jane을 위한 추천 결과를 준비합니다.

공식 운영 모델은 아래와 같습니다:

[![myPFM 예시 운영 모델](images/Gaia-X_Data_Exchanges_Example_myPFM.svg)](./Annex 2 - Data Exchange example - Data Exchange Document - 25.07 Release_files/Gaia-X_Data_Exchanges_Example_myPFM.svg)

September 18, 2025


September 18, 2025
