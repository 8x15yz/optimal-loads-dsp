# 5. Data Products Catalogue

A **Data Products Catalogue** is a structured and standardized registry of data products that is made available within an ecosystem. It allows data providers to publish, describe, and manage their offerings, and enables data consumers to discover, assess, and access data products that meet their needs. It:

- Connects data providers and consumers within a trusted, interoperable network or participants;
- Enables trust-by-design via verifiable credentials;
- Facilitates cross-domain data exchange, e.g., between healthcare, manufacturing, and mobility ecosystems;
- Supports governance through integration with identity, access, and policy enforcement services.

Data Products Catalogue **entries** are described using Gaia-X descriptions (see Annex 1), including data usage policies and licensing terms.

These entries enable data product visibility and discoverability for potential users. The information about the data product serves to enable other parties to easily find the data product (cf. *Discovery/Research API* below) and assess its trustworthiness, applicability, quality and relevance. This information also includes the rights or limitations for the use of the data product for specific purposes, as well as specific conditions in the case of personal data.

The catalogue metadata of a data product shall:

1. Provide a description of the data product that enables the user to distinguish between the different data products and make an informed decision about the fitness for its intended use;
2. Be up-to-date (i.e. reflecting the current status of the data product).
3. Describe the policies regarding the visibility of the product metadata;
4. Provide information on the data access methods that are supported by the data product;
5. Describe the use restrictions and licence terms that apply to the data product;
6. Where applicable, reference the data collection methodology;
7. Where applicable, describe the data provenance and data lineage. In case the data product includes anonymized or pseudonymized data, data lineage includes information about the applied anonymization or pseudonymization method;
8. Where applicable, reference the data quality methodology that was applied, including information on related data quality dimensions and metrics.

Parties operating a data catalogue need to ensure the trustworthy publication of the catalogue metadata of data products.
The data catalogue ensures that only authorized users can publish or modify metadata in the catalogue. This includes mechanisms to control access to metadata and the data product itself / audit records of publication and access control changes.

The core components of the Data Products Catalogue are:

- **Data Product Metadata Repository**: Stores the descriptive information (metadata) about each data product.
- **Access**: Describes how metadata can be accessed and by whom (some ecosystems might need to restrict knowledge of a Data Product description on a per needed basis).
- **Discovery/Research API**: Allows external systems to search and filter data products.
- **Data License Analysis** (optional): Enables Catalogue users to check that they can fulfill the Data Access Prerequisites and the Data Usage Constraints listed in the Data License part of the Data Product Description.
- **Semantic Description Engine** (optional): Enables semantic search and understanding through ontologies and taxonomies - such a component is easier to implement for domain specific catalogues than for general purpose catalogues.

September 18, 2025


September 18, 2025
