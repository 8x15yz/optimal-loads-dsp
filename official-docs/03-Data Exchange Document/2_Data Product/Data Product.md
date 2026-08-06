# 3. Data Product[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#data-product "Permanent link")

Enabling digital transformation as well as developing innovative services requires the right data at the right time, aggregating from multiple sources to produce valuable insightful information.
However, within most organizations, data sharing is too often stalled by stakeholder resistance, data governance policies, lack of tools, and inability to address regulatory constraints:

- For a data producer, personal and non-personal data sharing is often associated with a legal risk (e.g. personal data, as per GDPR, shared without the person’s consent), with an industrial risk (e.g. data including some intellectual property or commercial secret communicated to competitors) or with a reputation and image risk (e.g. data privacy shaming if shared data is misused), while there are barely any established local benefits for sharing data.
- For a data consumer, appropriate use and corresponding usage restrictions are rarely clearly, nor formally, stated or are expressed in a legal form which is cumbersome to check and is difficult to enforce automatically.
- For an entity’s legal and compliance structures, data access and governance processes are often fragmented, and verifications of appropriate data usage are complex and labor intensive (i.e. checking that received data are used in a not-illegal way is complex).

This complexity often results in decisions that are overly risk averse, blocking data sharing with a “stop first and thoroughly assess” mechanism, preventing business opportunities from driving digital transformation and from grabbing competitive advantages.

Overcoming these resistances requires to establish reliable trust mechanisms throughout the data sharing process.
First, the original data rights holders need to be able to express how their data shall be used, and they need confidence that these constraints will be duly applied.
Then, the data consumers need evidence that the data is genuine, and that the usage authorization is legitimate (i.e. that they are not illegally using the data).
Respectively, the data providers need evidence that the data consumers have the authorization to receive the data (i.e. providing the data is legal).

The Gaia-X Data Product concept and its operational model provide such mechanisms and enable data rights holders to control how their data are used and by whom (this is called *data sovereignty*). In addition, they provide mechanisms to facilitate and demonstrate compliance with the European regulations regarding data (GDPR and Data Act).

## 3.1 Data Product Conceptual Model[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#data-product-conceptual-model "Permanent link")

[![Data Product Conceptual Model](images/Gaia-X_models_Data_Product_Conceptual.svg)](./Data Product - Data Exchange Document - 25.07 Release_files/Gaia-X_models_Data_Product_Conceptual.svg)

*Figure 3.1 - Data Product conceptual model*

Data are furnished by `Data Producers` to `Data Providers` who compose them into a `Data Product` to be used by `Data Consumers`. Data Producers can be *data owners* or *data controllers* in the GDPR sense, or *data holders* in the Data Act sense – other kinds of Data Producers can be defined by different ecosystems.

A Data Product is described by a `Data Product Description`, which must be a valid Data Product Description according to the [Data Product Ontology class](https://gaia-x.gitlab.io/technical-committee/service-characteristics-working-group/service-characteristics/classes/DataProduct/) and is stored in a (searchable) `Federated Data Catalogue`.

Data Product Descriptions contain the `Metadata` describing the data (scope, format, quality, etc.) using an ontology which is defined by the ecosystem and contain information describing the contractual and operational aspects of the Service Offering (cost and billing, technical means, service level agreement, etc.).

Before using a Data Product, the Data Consumer negotiates and co-signs a `Data Access Contract` (DAC) with the Data Provider.
This Data Access Contract is based on the Data Product Description and includes the service configuration elements and mutually agreed and enforceable `Terms of Usage`, resulting from potential negotiations. Hence, a Data Product Description constitutes a Data Access Contract template.

The Data Access Contract is a Ricardian contract: a contract at law that is both human-readable and machine-readable, cryptographically signed and rendered tamper-proof, and electronically linked to the subject of the contract, i.e. the data.
The parties can (optionally) request this contract to be notarized in a federated `Data Access Contract Store`.

Note

A Data Access Contract is often organized in several parts: (i) an ecosystem-level contract agreed/signed by all participants of the ecosystem (sometimes called ecosystem policy scheme), (ii) a frame contract between the Provider and the Consumer defining the overall terms and conditions governing the contractual relationship for a set of services and (iii) an application contract specific to the ordered service.

After such a contract is agreed and signed by both the parties, the Data Consumer can start accessing the data (`Data Access`) and then using the data (`Data Usage`), realizing the Data Product Access Contract.
The contract negotiation can lead to both parties agreeing on a `Data Access Logging Service` (these logs might also include information needed for billing, inc. service level details, even if billing is outside Gaia-X perimeter).

If a specific license is attached to some data in the Data Product, then the Data Product Description shall contain a `Data License` defining the usage policies for the data and, before Data Usage, the Data License shall be derived into a `Data Usage Agreement` (DUA) signed by the `Data Rights Holder` and by the `Data Consumer`. Data Usage Agreements are notarized by a `Data Usage Agreement Notary` (DUA Notary) and can be revoked at any time.

The signed Data Usage Agreement is communicated to the Data Provider, who must check that the DUA is not revoked (through the DUA Notary) and that the DUA constraints are fulfilled. This check must be done before each Data Usage delivery (i.e. each time the data access is requested by a Data Consumer, especially for recurrent data access).

This signed Data Usage Agreement gives (a) to the Data Consumer the legal authorization to use the data in accordance with the constraints specified by the Data Rights Holder and (b) gives to the Data Rights Holder the assurance that the Data Consumer commits to respect these constraints.

Note

The signature can be a digital signature (as for instance an eIDAS signature) or simply an electronic form (as a click on a “I agree” button in a specific screen provided by the DUA Notary).

The Data Usage Agreement concept is a general concept which addresses every kind of licensed data and hence encompasses also the concepts of *Consent* from GDPR and of *Permission* from the EU Data Act.
In case of data liable to legal regulation (e.g. GDPR or Data Act), the Data Usage Agreement must contain all information required by the regulation (in particular the purpose of usage).

If the Data Product contains data from several Data Rights Holders, then a Data Usage Agreement shall be signed by each Data Rights Holder and all these signed Data Usage Agreements shall be communicated to the Data Provider before Data Usage.

Note

Data Acces Contract (DAC) and Data Usage Agreement (DUA) are different in terms of objectives and actors.

A DAC is established between a Data Provider and a Data Consumer. It focuses on service delivery : technical configuration, billing, SLA, termination clauses, etc.

A DUA is established between a Data Rights Holder and a Data Consumer. It focuses on the usage conditions of the data contained in the Data Product.

## 3.2 Data License and Data Usage Agreement[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#data-license-and-data-usage-agreement "Permanent link")

Data Usage Agreements enable Data Rights Holders to control how their data are used and by whom (this is called *data sovereignty*).

Data Licenses contain a set of constraints related to the authorized or forbidden usage of the data in the Data Product. Data Usage Agreements are usually derived from the Data License but might differ according to the result of the negotiation between the Data Rights Holder and the Data Consumer. Data Usage Agreements also include additional information related to the identity of the Data Consumer, the detailed purpose of the data usage, the duration of the agreement, etc.

Data Usage Agreements contain two sets of constraints: the *Data Access Prerequisites*, which are enforced by the Data Provider before delivering access to the data, and the *Data Usage Constraints*, which are outside the scope of the Data Provider and shall be respected by the Data Consumer when using the data. For instance, restricting data access to research laboratories with a specific ISO certificate can be enforced by the Data Provider while restricting data usage to research related to a specific disease is enforceable only by the Data Consumer.

To enable automated processing, Gaia-X mandates the use of Open Digital Rights Language (ODRL) from W3C to express Data License constraints (cf. https://www.w3.org/TR/odrl-model/) – using an ontology which will usually be defined by the ecosystem.

A Data License can be generic, for instance “I agree that my data are used by any non-profit licensed health laboratory with XYZ security level” or specific “My data can be used only with a specific DUA signed by me and including the identity of the data consumer and the explicit consent of the data usage.”

In the first case (generic license), a DUA signed by the Data Rights Holder is pre-notarized and there is no need for further communication with the Data Rights Holder before Data Usage: the DUA identifier can be stored in the Data Product Description and the Data Consumer just needs to sign it, notarize it and communicate the identifier to the Data Provider.

In the second case (specific license), the Data Rights Holder must be contacted (either by the Data Consumer or by the Data Provider) in order to fill the DUA and sign it.

More details are provided in the [Data Usage Operating Models](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#data-usage-operating-model) section.

## 3.3 DUA verification process[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#dua-verification-process "Permanent link")

The actors involved in a specific Data Usage must check:

1. The **DUA validity**: is the entity signing the DUA really the Data Rights Holder (or a legal delegate of the Data Rights Holder)?
2. The **DUA applicability**: is the Data Consumer entitled to access the data (i.e. it fulfils the *Data Access Prerequisites* conditions expressed in the Agreement)?
3. The **DUA status**: is the DUA active (i.e. not expired and not revoked)?

To enable the DUA validity check, the DUA shall include Verifiable Credentials “proving” that the Data Rights Holder is legally entitled to sign the DUA (i.e. to authorize data usage). Such credentials might depend on business/legal logic and trusted sources specific to the business domain. For instance, a farmer can agree to share data related to a parcel only if it is a farmer and if it owns or rents the parcel.

To enable DUA applicability check, the Data Consumer must provide for each ORDL rule in the DUA, the verifiable credentials “proving” that it fulfils the constraints of the rule. To facilitate applicability check, it is recommended to specify in the Data Product Description the list of accepted Verifiable Credentials and the accepted issuers.

Data Providers must check the DUA validity, the DUA applicability and the DUA status before each Data Usage.
Data Consumers must check the DUA validity and the DUA status before using the data.

As such checks can require domain-specific logic and hence can be complex to implement, it is likely that most ecosystems will mandate DUA Notaries to provide services to check DUA validity and DUA applicability (hence acting as policy information points), in addition to basic notarization services.

## 3.4 Cascading Agreement and Right to Oblivion[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#cascading-agreement-and-right-to-oblivion "Permanent link")

The above conceptual model can be applied recursively: the Data Consumer can integrate the Data into a new Data Product that can be used by other Data Consumers, who can in turn create new Data Products.
It provides convenient mechanisms for Data Rights Holders to control who is using their data and to revoke usage agreements.

Indeed, the above model blocks subsequent data transmissions between the Data Provider and the Data Consumer when the Data Usage Agreement is revoked and hence it provides a more robust mechanism than the usual cascading mechanism where the chain of revocations will be broken if one of the participants in the usage chain is defective.

To support the right to oblivion, it is recommended that a general policy mandating each participant to check the Data Usage Agreement validity before reusing the data (even internally, when they don’t request new Data Usage from the Data Provider) is defined by the specific ecosystem.

How a participant implements this policy depends on its own internal data management procedures and is outside the scope of Gaia-X.

## 3.5 Data Usage Operating Model[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#data-usage-operating-model "Permanent link")

The overall Data Usage process in Gaia-X is voluntarily independent from technical means deployed by the Data Provider to enable data usage: it can be an on-off data transfer after an API call, it can be a continuous stream of data, it can be a call back each time the data changes, it can be the execution of the Consumer provided function in a provider environment (hence the Consumer never sees the data and just gets the result), etc.
Accordingly, the possible technical means enabling Data Usage are not further detailed here.

The most unique aspect of Gaia-X Data Usage process is related to the Data Usage Agreement signature.
Several cases are to be considered, depending on the kind of Data License and on the relationship between the Data Rights Holder, the Data Provider and the Data Consumer:

- Case 1: generic license, where the Data Rights Holder does not want to know who is using its data (open-data is a specific case of generic license with a DUA signed by the Data Rights Holder giving everybody unconstrained usage of the data),
- Case 2a: specific license where the Data Consumer has access to the Data Rights Holder (this is usually the case when the Data Consumer provides a service to the Data Rights Holder using the Data Rights Holder’s data, for instance when a sports training app uses historical monitoring data from a sports watch provider to provider sport coaching advice),
- Case 2b: specific license where the Data Provider has access to the Data Rights Holder, but the Data Consumer (for instance a Data Consumer wanting to use data for statistical purposes) does not have access.

The basic operating model for data usage with a generic license is quite simple:

[![Data Usage Operating model 1](images/Gaia-X_models_Data_Product_Operational_Case1.svg)](./Data Product - Data Exchange Document - 25.07 Release_files/Gaia-X_models_Data_Product_Operational_Case1.svg)

*Figure 3.5 Case 1 - Data usage operating model*

1. The Data Rights Holder signs a generic DUA and notarizes it through a DUA Notary. It then communicates the signed DUA to the Data Provider who stores it in the Data Product Description within the Catalogue (it replaces the generic Data License in that case).
2. The Data Consumer queries the Data Product Catalogue and reviews the Data Product Descriptions (including the Data License) to select a Data Product that corresponds to its needs.
3. The Data Consumer configures the Data Product in terms of data scope and operational characteristics and starts negotiating with the Data Provider.
4. When Data Consumer and Data Provider find an agreement, they sign a configured Data Product Description to create the Data Access Contract (DAC) and can optionally notarize it in a Federated Data Access Contract Store.
5. The Data Consumer countersigns the DUA (retrieved from the Data Product Description) and notarizes it through the DUA Notary.
6. The Data Consumer requests Data Access providing the DUA. The Data Provider checks the DUA’s validity, applicability and status. If everything is OK, it activates the instantiated Data Product resulting in actual Data Access enabling Data Usage.

The operating model is a bit more complex when the Data Product includes specific licensed data.

If the Data Consumer has access to the Data Rights Holder (Case 2a below), then it can directly request the Data Usage Agreement – this is usually the case when the Data Consumer is using the data to provide a service to the Data Rights Holder (for instance, when a sports training app get historical monitoring data from a sports watch provider to provide sports coaching) or when the Data Rights Holder accepts that its contact points are communicated to the Data Consumer by the Data Provider. Otherwise, the Data Usage Agreement has to be collected by the Data Provider.

[![Data Usage Operating model 2a](images/Gaia-X_models_Data_Product_Operational_Case2a.svg)](./Data Product - Data Exchange Document - 25.07 Release_files/Gaia-X_models_Data_Product_Operational_Case2a.svg)

*Figure 3.5 Case 2a - Data usage operating model*

1. The Data Consumer queries the Data Product Catalogue and reviews the Data Product Descriptions (including the Data License) to select a Data Product that corresponds to its needs.
2. The Data Consumer configures the Data Product in terms of data scope and operational characteristics and starts the negotiation with the Data Provider.
3. The Data Provider and the Data Consumer close the negotiation, and they sign the configured Data Product Description to create the Data Access Contract (DAC). They can optionally notarize the Data Access Contract in a Federated Data Access Store.
4. The Data Consumer extracts the Data Usage Agreement template from the Data Product license, fills it with its specific information (its identity, how the data will be used, for which purpose, and so on), and communicates it to the Data Rights Holder who signs it, notarizes it through a Data Usage Agreement Notary and gives it back to the Data Consumer. The Data Consumer checks the DUA validity (i.e. checks that the Data Rights Holder is really holding the rights on that data), countersigns it and notarizes it through the DUA Notary.
5. The Data Consumer requests Data Access providing the DUA. The Data Provider checks the DUA validity, applicability and status. If everything is OK, it activates the instantiated Data Product resulting in actual Data Access enabling Data Usage.

If the Data Consumer has no access to the Data Rights Holder (Case 2b below), then the operating model is similar except for step 4, where the Data Usage Agreement is requested through the Data Provider (directly or through the Data Producer).

[![Data Usage  Operating model 2b](images/Gaia-X_models_Data_Product_Operational_Case2b.svg)](./Data Product - Data Exchange Document - 25.07 Release_files/Gaia-X_models_Data_Product_Operational_Case2b.svg)

*Figure 3.5 Case 2b - Data usage operating model*

1. The Data Consumer queries the Data Product Catalogue and reviews the Data Product Descriptions (including the Data License) to select a Data Product that corresponds to its needs.
2. The Data Consumer configures the Data Product in terms of data scope and operational characteristics and starts the negotiation with the Data Provider.
3. The Data Provider and the Data Consumer close the negotiation, and they sign the configured Data Product Description to create the Data Access Contract (DAC). They can optionally notarize this Data Access Contract in a Data Access Contract Store.
4. The Data Consumer extracts the Data Usage Agreement template from the Data Product license, and fills it with its specific information (its identity, how the data will be used, for which purpose, and so on). The Data Consumer communicates this Data Usage Agreement to the Data Rights Holder through the Data Provider (possibly through the Data Producer in some cases). The Data Rights Holder signs it, notarizes it through a Data Usage Agreement Notary and gives it back to the Data Consumer, through the Data Provider. The Data Consumer checks the DUA validity, countersigns it and notarizes it through the DUA Notary.
5. The Data Consumer requests Data Access providing the DUA. The Data Provider checks the DUA’s validity, applicability and status. If everything is OK, it activates the instantiated Data Product resulting in Data Access enabling actual Data Usage.

Note

DUA Notaries might provide additional services to check DUA validity and applicability. This is not mandated by Gaia-X but this would provide convenient services to the various actors, especially for data usage across ecosystems as such checks can be domain-dependent and be complex to execute in some ecosystems. DUA Notaries can also provide additional services like analysis of usage licenses and usage purposes for Data Consumer, DUA statistics for Data Consumer control teams, DUA dashboard and data usage statistics for Data Rights Holders (e.g. signed DUAs which are not used anymore)

## 3.6 Mapping of Gaia-X Concepts with EU Data Regulation Concepts[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-product/#mapping-of-gaia-x-concepts-with-eu-data-regulation-concepts "Permanent link")

The following table maps the Gaia-X concepts with the concepts used within the different European regulations around data (GDPR and the EU acts on data - DxA):

| **European Regulations Concepts** | **Gaia-X Concepts** |
| --- | --- |
| data processor in GDPR | Data Provider |
| data subject in GDPR / user in DxA | Data Rights Holder |
| consent in GDPR / permission or authorization in DxA | Data Usage Agreement |
| recipient in GDPR / DxA | Data Consumer |

The following diagram details these relationships (European regulations concepts (black color), Gaia-X concepts (blue color)):

[![Concept mapping Gaia-X vs EU regulations](images/Gaia-X_models_Data_Product_vs_EU_Regulations_v4.drawio.png)](./Data Product - Data Exchange Document - 25.07 Release_files/Gaia-X_models_Data_Product_vs_EU_Regulations_v4.drawio.png)

*Figure 3.6 - Mapping of Gaia-X Concepts with EU Data Regulation Concepts*

September 18, 2025


September 18, 2025
