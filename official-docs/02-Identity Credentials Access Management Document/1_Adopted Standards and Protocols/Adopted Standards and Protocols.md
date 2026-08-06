# 3. Adopted Standards and Protocols[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#adopted-standards-and-protocols "Permanent link")

This section defines the key reference standards upon which the specifications in this document are built.
It does not impose Gaia-X design decisions (e.g. format or method selections). Those decisions, profiles, and constraints will be introduced in subsequent chapters.

## 3.1 Standards for Credentials and Identifiers[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#standards-for-credentials-and-identifiers "Permanent link")

### 3.1.1 JSON-LD[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#json-ld "Permanent link")

[JSON-LD (JavaScript Object Notation for Linked Data)](https://json-ld.org/) is a W3C standard for expressing Linked Data using familiar JSON syntax.   
It uses a context to map JSON properties to IRIs (Internationalized Resource Identifiers), enabling unambiguous interpretation of terms, and allows data to interoperate across systems by providing semantic meaning.   
JSON-LD is fully compatible with JSON, making it easier to integrate into existing JSON-based systems while supporting richer linked-data semantics.

### 3.1.2 SHACL (Shapes Constraint Language)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#shacl-shapes-constraint-language "Permanent link")

[SHACL (Shapes Constraint Language)](https://www.w3.org/TR/shacl/) is a W3C standard for defining shapes, i.e., constraints on RDF graphs, and validating that data (RDF graphs) conform to those shapes.   
Shapes express constraints on property paths, cardinalities, datatype restrictions, and logical combinations, and may use extension languages like SPARQL to express more complex validation rules.

### 3.1.3 Decentralized Identifiers[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#decentralized-identifiers "Permanent link")

[Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-1.0/) are URIs that enable verifiable, self-sovereign digital identity without requiring a single centralised registry or authority, although they may be anchored in distributed or decentralised registries.
A DID resolves to a DID Document that typically contains one or more verification methods, each associated with cryptographic key material.   
These verification methods commonly include key pairs consisting of a private key and a public key, mathematically linked through asymmetric cryptographic algorithms. The private key is securely generated and kept under the sole control of the DID controller, while the corresponding public key is published in the DID Document as part of the verification method.  
The verification methods are used to prove control over the identifier and to enable trustworthy interactions such as the sharing and retrieval of Verifiable Credentials (VCs) and other resources (see DID specifications [here](https://www.w3.org/TR/did-1.0/#the-relationship-between-did-controllers-and-did-subjects)).   
This cryptographic binding ensures that only the DID controller holding the private key can create digital signatures that verifiers can validate using the public key from the DID Document, thus establishing the cryptographic proof of control and authenticity within the Gaia-X ecosystem.

### 3.1.4 JSON Web Token (JWT)/JSON Web Signature (JWS)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#json-web-token-jwtjson-web-signature-jws "Permanent link")

[JSON Web Token (JWT)](https://www.rfc-editor.org/rfc/rfc7519.html) is an open standard (RFC 7519) for encoding a set of claims in a JSON object that can be integrity-protected or signed.
[JSON Web Signature (JWS)](https://www.rfc-editor.org/rfc/rfc7515.html) (RFC 7515) defines how to apply a digital signature over a payload using JSON-based structures, making it possible to verify authenticity and integrity.

### 3.1.5 JSON Web Key[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#json-web-key "Permanent link")

[JSON Web Key (JWK)](https://datatracker.ietf.org/doc/html/rfc7517), defined in [RFC 7517], is a JSON-based standard for representing cryptographic keys and key sets. It provides a standardised and interoperable way to publish and exchange public keys and key metadata, typically used to verify JSON Web Tokens (JWTs) and other digital signatures within identity and credential systems.

### 3.1.6 W3C Verifiable Credentials Data Model v2.0[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#w3c-verifiable-credentials-data-model-v20 "Permanent link")

Verifiable Credentials (VCs) as defined in the ([W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)) are used to express assertions (claims) about one or more subjects in a cryptographically verifiable, machine-readable form.   
VCs include claims, issuer metadata, validity constraints, and proof mechanisms to ensure integrity and authenticity.   
A VC can be shared directly or embedded in a [Verifiable Presentation (VP)](https://www.w3.org/TR/vc-data-model-2.0/#presentations), which a holder uses to present one or more credentials in a controlled manner.   
A Verifiable Presentation enables a verifier to confirm that the claims in its enclosed credentials originate from the asserted issuer(s).

### 3.1.7 W3C VC-Bitstring Status List[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#w3c-vc-bitstring-status-list "Permanent link")

The Bitstring Status List ([W3C VC-Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)) defines a privacy-preserving, space-efficient mechanism to encode the revocation or suspension status of many Verifiable Credentials in a single bitstring.   
Each credential is associated with a specific bit index: a value of 1 denotes “revoked” or “suspended”, and 0 denotes “valid”; the bitstring (often compressed) is published as a Verifiable Credential so verifiers can check status without contacting each issuer individually.

## 3.2 Protocols[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#protocols "Permanent link")

### 3.2.1 OpenID for Verifiable Credentials (OID4VC)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#openid-for-verifiable-credentials-oid4vc "Permanent link")

The term “OID4VC” commonly refers to the family of OpenID/OAuth-based protocols that support the issuance and presentation of Verifiable Credentials and Verifiable Presentations.

### 3.2.2 OpenID Connect for Verifiable Credential Issuance (OIDC4VCI)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#openid-connect-for-verifiable-credential-issuance-oidc4vci "Permanent link")

[(OIDC4VCI)](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) is based on the [OAuth 2.0 specification](https://www.rfc-editor.org/info/rfc6749) and allows an issuer to communicate with a holder and their wallet in order to issue Verifiable Credentials in a secure manner.

OID4VCI defines an OAuth-protected API through which an issuer can issue Verifiable Credentials to a holder’s wallet.
The specification leverages OAuth 2.0 (rather than redefining it) to obtain authorisation for credential issuance.

> ⚠️ OIDC4VCI is published as a version 1.0 specification, intended as a stable baseline for implementers.

### 3.2.3 OpenID Connect for Verifiable Presentations (OIDC4VP)[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/standards/#openid-connect-for-verifiable-presentations-oidc4vp "Permanent link")

[(OIDC4VP)](https://openid.github.io/OpenID4VP/openid-4-verifiable-presentations-wg-draft.html) extends OAuth 2.0 / OpenID Connect to allow a holder (via a wallet) to present one or more Verifiable Credentials to a verifier as a Verifiable Presentation.

> ⚠️ OIDC4VP is published under the OpenID “version 1.0” set of drafts.

November 28, 2025


November 28, 2025
