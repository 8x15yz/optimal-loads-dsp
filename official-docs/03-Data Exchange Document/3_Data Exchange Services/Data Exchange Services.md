# 4. Data Exchange Services

## 4.1 Data Exchange Services[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-exchange-services/#data-exchange-services "Permanent link")

Data access and data usage in Gaia-X are enabled by a set of services that are used by the involved actors and are supported as Federation Services. Some of these services are specific to data access/usage or include data-related specificities - these are referred as Data Services.

They are listed below and fully described in the following chapters:

Note

Not all Data Exchange Services are mandatory.

- **Data Product Catalogue Services** (mandatory) provide mechanisms to publish Data Product Descriptions (inc. metadata) and to support search. Data Product Catalogue Services are specific in the sense that they use DCAT as the core protocol for Data Product description. Gaia-X provides an initial set of Vocabularies to describe Data Product. Gaia-X Data Product Catalogues must be extensible with vocabularies from different (business or technical) domains.
- **Data Usage Agreement Services** (mandatory) provide mechanisms to notarize/revoke Data Usage Agreements (DUA), to check their status, their validity (i.e. check that the signatory is really holding rights on the data) and their applicability (i.e. that the Data Access Prerequisites are fulfilled).
- **Data Access Protocols** are required to exchange data between Participants and hence to enable Data Access. Data exchanges are realized on a peer-to-peer basis. Gaia-X does not promote any technical protocol - the actual protocol must be agreed between the parties during the contracting phase.
- **Data Access Logging Services** (optional) provide evidence that data has been (a) actually accessed (i.e. provided and received) and (b) that the Data Usage Agreement was enforced before access. Data Providers can use these services to demonstrate to Data Rights Holders (and to the Ecosystem Governance Authority) that all data accesses were performed according to their requirements. Additionally, Data Consumers can use these services in case of SLA dispute.

### 4.1.1 Non-specific Services[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-exchange-services/#non-specific-services "Permanent link")

Other Federation Services are needed to realize the complete life cycle of Data Access / Data Usage, but don’t carry specificities related to data:

- **Authentication and Digital Signature Services** (mandatory) are essential to identify participants and to record trustworthy data usage agreements. They are provided according to the specifications defined in the [Gaia-X Identity, Credential and Access Management Document](https://docs.gaia-x.eu/).
- **Negotiation and Contracting Services** (mandatory) enable parties to negotiate Service Contracts, including Data Usage Contracts.
- **Contract Store Services** (optional) enable parties to notarize a contract (i.e. the result of the negotiation phase).

These services are not described further here.

September 18, 2025


September 18, 2025
