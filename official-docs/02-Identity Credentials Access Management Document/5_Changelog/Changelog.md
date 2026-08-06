# 7. Changelog[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/changelog/#changelog "Permanent link")

## 7.1 2025 November Release (25.11)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/changelog/#2025-november-release-2511 "Permanent link")

The ICAM document is restructured with additional topics. Below are the ToCs from previous version and the newly refactored ICAM document to give a clarity on what has been removed or added/updated.

| **Previous version ToC** | **Current New ToC** |
| --- | --- |
| 1. Identity, Credential and Access Management Document | 1. Identity, Credential and Access Management Document |
| 1.1 Publisher | 1.1 Publisher |
| 1.2 Authors | 1.2 Authors |
| 1.3 Contact | 1.3 Contact |
| 1.4 Other Format | 1.4 Other Format |
| 1.5 Copyright Notice | 1.5 Copyright Notice |
| 2. Introduction and Scope of the Document | 2. Introduction to ICAM |
| 3. Credential Format | 3. Adopted Standards and Protocols |
| 3.1 Gaia-X Credential Format | 3.1 Standards for Credentials and Identifiers |
| 3.1.1 Gaia-X Credential Example | 3.1.1 JSON-LD |
| 3.2 Digital Signature Standard | 3.1.2 SHACL (Shapes Constraint Language) |
| 3.3 Decentralized Identifiers | 3.1.3 Decentralized Identifiers |
| 3.3.1 Verification Methods | 3.1.4 JSON Web Token (JWT)/JSON Web Signature (JWS) |
| 3.4 Use of Identifiers in Gaia-X Credentials | 3.1.5 JSON Web Key |
| 3.5 Verifiable Credential and Verifiable Presentation | 3.1.6 W3C Verifiable Credentials Data Model v2.0 |
| 3.5.1 namespace Bindings and Contexts | 3.1.7 W3C VC-Bitstring Status List |
| 3.5.2 Identifiers | 3.2 Protocols |
| 3.5.3 Integrity of Related Resources | 3.2.1 OpenID for Verfiable Credentials (OID4VC) |
| 3.5.4 Types | 3.2.2 OpenID Connect for Verifiable Credential Issuance (OIDC4VCI) |
| 3.5.5 Issuers | 3.2.3 OpenID Connect for Verifiable Presentations (OIDC4VCP) |
| 3.5.6 validFrom | 4. Digital Identities |
| 3.5.7 validUntil | 4.1 Overview |
| 3.5.8 Verifiable Credential | 4.2 Operational Roles of Digital Identities and Keypair Usage |
| 3.5.9 Enveloped Verifiable Credential | 4.2.1 Keypair not bound to a Certificate |
| 3.5.10 Verifiable Presentation | 4.2.2 Self-Issued Keypair |
| 3.5.11 Enveloped Verifiable Presentation | 4.2.3 Trust Service Provider (TSP) Keypair |
| 3.6 Gaia-X Compliance input/output | 4.3 Binding Digital Identities to Claims |
| 3.6.1 Input | 4.3.1 Different Requirement based on Use cases |
| 3.6.2 Output | 4.4 DID Resolution |
| 4.2.2 Policy description | 4.4.1 Verification Method |
| 4. TrustAnchor Credential | 4.5 eIDAS Integration |
| 5. Party Credential | 4.5.1 eID |
| 5.1 Private Party Credential | 4.5.2 eSignature |
| 5.1.1 Private Party Credential Example | 4.6 Implementing Interactions between Machines and Humans |
| 5.2 Public Party Credential | 4.6.1 Interactions with Human-in-the-Loop |
| 6. Party Credential Lifecycle | 4.6.2 Interactions with Machines |
| 7. Party Credential Status | 5. Gaia-X Credentials |
| 8. OpenID Connect for Verifiable Credentials | 5.1 Overview |
| 8.1 OpenID Connect for Verifiable Issuance | 5.2 Core Data Model Foundations |
| 8.2 OpenID Connect for Verifiable Presentations | 5.2.1 Namespace Bindings and Contexts |
| 8.3 Usage | 5.2.2 Usage |
| 8.4.Cloud/Enterprise Wallet | 5.2.3 Type Property |
| 9. Signature Credential | 5.3 Credential Format Specification |
| 9.1 Multiple Signatures using SignatureCredential specializations | 5.3.1 Encoding Requirements |
| 9.1.1 SignatureAgreementCredential | 5.3.2 Credential Structure |
| 9.1.2 Data Usage Agreement Example | 5.3.3 Credential Subject |
| 9.2 Multiple Signatures using Proof Set and Proof Chain | 5.4 Verifiable Credentials |
| 10. Trustframework Implementation | 5.4.1 Standard Verifiable Credential |
| 10.1 Trust Framework Implementation | 5.4.2 Enveloped Verifiable Credential |
| 10.2 Trust Anchor Credential specialization examples | 5.5 Verifiable Presentations |
| 10.3 Party Credential Specialization examples | 5.5.1 Standard Verifiable Presentation |
| 10.3.1 Natural Person Party Credential | 5.5.2 Enveloped Verifiable Presentation |
| 10.3.2 Legal Person Party Credential | 5.6 Issuer Requirements |
| 10.3.3 Service Part Credential | 5.7 Additional Features |
| 10.3.4 Membership Party Credential | 5.7.1 Integrity of Related Resources |
| 10.4 Access rights delegation example - Employee Authentication | 5.7.1 Credential Lifecycle Status |
| 10.4.1 Problem Statement | 6. ICAM Semantic Model |
| 10.4.2 Types of Credentials and Issuers involved | 6.1 Trust Scope Credential |
| 10.4.3 Access Entitlement Credentials | 6.1.1 Trust Scope Credential specialisation examples |
| 10.4.4 Authentication Process | 6.1.2 Federation using Trust Scope Credentials |
| 10.4.5 Revocation | 6.2 Party Credential |
| 10.4.6 Implementation Considerations | 6.2.1 Private Party Credential |
| 11. Changelog | 6.2.2 Public Party Credential |
|  | 6.2.3 Party Credential Specialisation examples |
|  | 6.3 Signature Credential |
|  | 6.4 Ecosystem Onboarding and Offboarding using ICAM Semantic Model |
|  | 6.5 Delegating Access Rights |
|  | 6.5.1 Types of Credentials and Issuers |
|  | 6.5.2 Implementation Factors |
|  | 7. Changelog |

## 7.2 2024 July release (24.07)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/changelog/#2024-july-release-2407 "Permanent link")

- Updated chapter “Credential Format”
- New chapter “Trust Anchor Credential and Party Credential”
- New chapter “OpenID Connect for Verifiable Credentials”
- New chapter “Signature Credential”
- New chapter “Trust Framework implementation”, containing Trust Anchor Credential specialisation examples and Party Credential specialisation examples and an access rights delegation example.

November 28, 2025


November 28, 2025
