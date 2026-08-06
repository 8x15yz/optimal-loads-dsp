# 5. Gaia-X Credentials[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#gaia-x-credentials "Permanent link")

## 5.1 Overview[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#overview "Permanent link")

This chapter defines how Verifiable Credentials (VCs) are modelled, structured, and used within the Gaia-X trust framework, following the W3C VC Data Model 2.0. It details the encoding, required properties, and processing rules for issuing and verifying Gaia-X compliant credentials. The goal is to ensure semantic consistency and technical interoperability across participants in the Gaia-X ecosystem.

## 5.2 Core Data Model Foundations[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#core-data-model-foundations "Permanent link")

### 5.2.1 Namespace Bindings and Contexts[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#namespace-bindings-and-contexts "Permanent link")

Gaia-X credentials use JSON-LD contexts and namespace bindings as part of their credential/presentation representation (e.g. via @context).

On the level of the Verifiable Presentation and the Verifiable Credentials contained in the Verifiable Presentation, a
Gaia-X Credential MUST adhere to the vocabulary of the Verifiable Credentials Data Model, i.e., use terms from
the `https://www.w3.org/2018/credentials#` namespace.

To enable human authors of Gaia-X Credentials to write down these terms conveniently, they MAY, by using the `@context`
keyword at the level of the Verifiable Presentation, e.g.:

- reference the [JSON-LD context](https://www.w3.org/TR/json-ld11/#the-context) provided by the Verifiable Credentials
  Data Model (https://www.w3.org/ns/credentials/v2) as in the initial example listing, or
- define their own context, which:
- defines the above namespace as the default vocabulary using the `@vocab` keyword, or
- maps the above namespace to a designated prefix, e.g. `"cred"`.

Similarly, the claims about any credential subject MUST adhere to the vocabulary of the Gaia-X Credential Schemas
published in the [Gaia-X Ontology](https://w3id.org/gaia-x/).

### 5.2.2 Identifiers[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers "Permanent link")

The `@id` MUST be present and unique for a given `issuer`.

The `@id` keyword can be aliased to `id` (consequently we may also use this alias).

It is up to the `issuer` to decide if the `@id` is a resolvable [URL](https://url.spec.whatwg.org/) or not.

Each of the following MUST have a different identifier:

- a Verifiable Presentation
- a Verifiable Credential inside a Verifiable Presentation
- the subject of a Verifiable Credential, i.e. the Conceptual Model entity about which claims are made.

Gaia-X Credentials MAY reference other Gaia-X Credentials. Consider, for example, a *ServiceOffering* that:

- is provided by a *Provider*,
- is a composition of other *ServiceOffering*s, or
- has an aggregation of *Resources*.

### 5.2.3 Type Property[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#type-property "Permanent link")

The `@type` property MUST be present in Verifiable Presentation and Verifiable Credentials.
The expected values for the first `@type` property are:

- `"VerifiablePresentation"` for a Verifiable Presentation
- `"EnvelopedVerifiablePresentation"` for an Enveloped Verifiable Presentation encoded as a VC-JWT
- `"VerifiableCredential"` for a Verifiable Credential
- `"EnvelopedVerifiableCredential"` for an Enveloped Verifiable Credential encoded as a VC-JWT

This `@type` can be followed with one or more credential related types (
ie. `@type: ['Verifiable Credential', 'gx:LegalPerson']`).

The `@type` keyword can be aliased to `type` (consequently, we may also use this alias).

The expected values for the `@type` property of a credential subject are given by the taxonomy of classes defined in
the [Gaia-X Ontology](https://w3id.org/gaia-x/), having the
superclasses `Participant`, `ServiceOffering` and `Resource`.

An ecosystem MAY define additional subclasses of these by defining further shapes and hosting them in its Registry.

In the future, Gaia-X and other ecosystems may also define additional, more specific credential types.

The shapes of Gaia-X Credentials, to be used as the vocabulary of the claims about credential subjects, MUST be available
in the form of SHACL shapes (cf. the [W3C Shapes Constraint Language SHACL](https://www.w3.org/TR/shacl/)) in the Gaia-X
Registry or in the Catalogue of a Federation.  
At any point when Gaia-X Credentials are created or received, a certain set of SHACL shapes is known, which forms a
*shapes graph*.
A Gaia-X Credential forms a *data graph*. For compliance with Gaia-X and/or a different ecosystem, this *data graph* MUST
be validated against the given *shapes graph* according to the [SHACL specification](https://www.w3.org/TR/shacl/#validation-definition).

## 5.3 Credential Format Specification[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-format-specification "Permanent link")

**Gaia-X Credentials** conform to the [W3C Verifiable Credential Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/), and use the Gaia-X Ontology which is available via the Gaia-X Registry.

### 5.3.1 Encoding requirements[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#encoding-requirements "Permanent link")

Gaia-X mandates credential encoding via VC-JWT, with the cryptographic proof constructed using JSON Web Signature (JWS) so that the payload, header and signature can be verified for authenticity and integrity.

Below is an example showing a JSON document in its native form (e.g. document.json), and how it is encoded as a VC-JWT via JOSE-based signing (and optionally encryption). This demonstrates how a plain JSON Verifiable Credential can be transformed into a cryptographically verifiable form under the VC-JWT/JOSE/COSE framework.

Example Verifiable Credential

| document.json | |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` {   "@context": [     "https://www.w3.org/ns/credentials/v2",     "https://w3id.org/gaia-x/development#"   ],   "@type": [     "VerifiableCredential",     "LegalPerson"   ],   "@id": "https://example.org/legal-participant/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",   "issuer": "did:web:example.org",   "validFrom": "2024-01-01T12:26:22.601516+00:00",   "validUntil": "2024-04-01T12:26:22.601516+00:00",   "credentialSubject": {     "id": "https://example.org/legal-participant-json/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",     "type": "gx:LegalPerson",     "gx:legalName": "Example Org",     "gx:legalRegistrationNumber": {       "id": "https://example.org/gaiax-legal-registration-number/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json"     },     "gx:headquarterAddress": {       "gx:countrySubdivisionCode": "FR-75"     },     "gx:legalAddress": {       "gx:countrySubdivisionCode": "FR-75"     }   } } ``` |

Once it has been encoded using the [VC-JWT specification](https://www.w3.org/TR/vc-jose-cose/#securing-json-ld-verifiable-credentials-with-jose),
it will become the following Verifiable Credential:

```
eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA
```

This VC-JWT can be analysed and verified with tools such
as [JWT.io's debugger](https://jwt.io/#debugger-io?token=eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb\_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE\_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA).
The following private and public key have been used to sign this VC-JWT example and \*\*all the examples in the upcoming
chapters\*\*.
This key pair will have the following ID : `did:web:example.org#JWK-RSA`. You will notice it in the
`kid` header claim of the example JWT below.

```
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC7VJTUt9Us8cKj
MzEfYyjiWA4R4/M2bS1GB4t7NXp98C3SC6dVMvDuictGeurT8jNbvJZHtCSuYEvu
NMoSfm76oqFvAp8Gy0iz5sxjZmSnXyCdPEovGhLa0VzMaQ8s+CLOyS56YyCFGeJZ
qgtzJ6GR3eqoYSW9b9UMvkBpZODSctWSNGj3P7jRFDO5VoTwCQAWbFnOjDfH5Ulg
p2PKSQnSJP3AJLQNFNe7br1XbrhV//eO+t51mIpGSDCUv3E0DDFcWDTH9cXDTTlR
ZVEiR2BwpZOOkE/Z0/BVnhZYL71oZV34bKfWjQIt6V/isSMahdsAASACp4ZTGtwi
VuNd9tybAgMBAAECggEBAKTmjaS6tkK8BlPXClTQ2vpz/N6uxDeS35mXpqasqskV
laAidgg/sWqpjXDbXr93otIMLlWsM+X0CqMDgSXKejLS2jx4GDjI1ZTXg++0AMJ8
sJ74pWzVDOfmCEQ/7wXs3+cbnXhKriO8Z036q92Qc1+N87SI38nkGa0ABH9CN83H
mQqt4fB7UdHzuIRe/me2PGhIq5ZBzj6h3BpoPGzEP+x3l9YmK8t/1cN0pqI+dQwY
dgfGjackLu/2qH80MCF7IyQaseZUOJyKrCLtSD/Iixv/hzDEUPfOCjFDgTpzf3cw
ta8+oE4wHCo1iI1/4TlPkwmXx4qSXtmw4aQPz7IDQvECgYEA8KNThCO2gsC2I9PQ
DM/8Cw0O983WCDY+oi+7JPiNAJwv5DYBqEZB1QYdj06YD16XlC/HAZMsMku1na2T
N0driwenQQWzoev3g2S7gRDoS/FCJSI3jJ+kjgtaA7Qmzlgk1TxODN+G1H91HW7t
0l7VnL27IWyYo2qRRK3jzxqUiPUCgYEAx0oQs2reBQGMVZnApD1jeq7n4MvNLcPv
t8b/eU9iUv6Y4Mj0Suo/AU8lYZXm8ubbqAlwz2VSVunD2tOplHyMUrtCtObAfVDU
AhCndKaA9gApgfb3xw1IKbuQ1u4IF1FJl3VtumfQn//LiH1B3rXhcdyo3/vIttEk
48RakUKClU8CgYEAzV7W3COOlDDcQd935DdtKBFRAPRPAlspQUnzMi5eSHMD/ISL
DY5IiQHbIH83D4bvXq0X7qQoSBSNP7Dvv3HYuqMhf0DaegrlBuJllFVVq9qPVRnK
xt1Il2HgxOBvbhOT+9in1BzA+YJ99UzC85O0Qz06A+CmtHEy4aZ2kj5hHjECgYEA
mNS4+A8Fkss8Js1RieK2LniBxMgmYml3pfVLKGnzmng7H2+cwPLhPIzIuwytXywh
2bzbsYEfYx3EoEVgMEpPhoarQnYPukrJO4gwE2o5Te6T5mJSZGlQJQj9q4ZB2Dfz
et6INsK0oG8XVGXSpQvQh3RUYekCZQkBBFcpqWpbIEsCgYAnM3DQf3FJoSnXaMhr
VBIovic5l0xFkEHskAjFTevO86Fsz1C2aSeRKSqGFoOQ0tmJzBEs1R6KqnHInicD
TQrKhArgLXX4v3CddjfTRJkFWDbE/CkvKZNOrcf1nhaGCPspRJj2KUkj1Fhl9Cnc
dn/RsYEONbwQSjIfMPkvxF+8HQ==
-----END PRIVATE KEY-----

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu1SU1LfVLPHCozMxH2Mo
4lgOEePzNm0tRgeLezV6ffAt0gunVTLw7onLRnrq0/IzW7yWR7QkrmBL7jTKEn5u
+qKhbwKfBstIs+bMY2Zkp18gnTxKLxoS2tFczGkPLPgizskuemMghRniWaoLcyeh
kd3qqGElvW/VDL5AaWTg0nLVkjRo9z+40RQzuVaE8AkAFmxZzow3x+VJYKdjykkJ
0iT9wCS0DRTXu269V264Vf/3jvredZiKRkgwlL9xNAwxXFg0x/XFw005UWVRIkdg
cKWTjpBP2dPwVZ4WWC+9aGVd+Gyn1o0CLelf4rEjGoXbAAEgAqeGUxrcIlbjXfbc
mwIDAQAB
-----END PUBLIC KEY-----
```

### 5.3.2 Credential Structure[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-structure "Permanent link")

#### 5.3.2.1 Header[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#header "Permanent link")

The VC-JWT header MUST contain the following fields:

- `alg`, the signature algorithm (ie. `PS256`)
- `typ`, the media type of the JWT which MUST be set to `vc+jwt`
- `cty`, the content type of the payload which MUST be set to `vc`
- `kid`, the verification method using a `did:web` or URL reference to the [verification method in a DID document](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#json-web-key)
- `iss`, the issuer’s DID address

Additional headers that aren’t described in
the [VC-JWT](https://www.w3.org/TR/vc-jose-cose/), [JWT](https://datatracker.ietf.org/doc/html/rfc7519)
or [JWS](https://datatracker.ietf.org/doc/html/rfc7515) specifications SHOULD be ignored.

#### 5.3.2.2 VC-JWT Payload[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#vc-jwt-payload "Permanent link")

The payload of the VC-JWT is a standard verifiable credential with claims as described in
the [Verifiable Credential Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) specification.

Some payload claims from the [JWT specification](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) MUST be
replaced by the described verifiable credential fields such as:

- `jti` will be replaced by the verifiable credential’s `id` or `@id`
- `sub` will be replaced by the verifiable credential’s `credentialSubject.id` or `credentialSubject.@id`

The `vc` and `vp` payload claims MUST NOT be present.

> ℹ️ The `iat` and `exp` payload claims represent the JWT’s signature validity period whereas the `validFrom` and
> the `validUntil`
> verifiable credential payload claims represent the verifiable credential’s
> data [validity period](https://www.w3.org/TR/vc-data-model-2.0/#validity-period).
> Therefore these claims can cohabit in the payload.

If the `@type` is “VerifiableCredential”, the property `credentialSubject` MUST be defined. The value
of `credentialSubject` can be a Credential or an array of Credentials. A Verifiable Credential MUST have :

- an [`@id`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers),
- an [`issuer`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#issuers) matching the `iss` JWT header,
- a [`@type`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#types), and
- a [`credentialSubject`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-subject) object or a [`credentialSubject`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-subject) array.

> NB: The `@id` and `@type` keywords are aliased to `id` and `type` respectively. Consequently, we may also use these
> aliases.

#### 5.3.2.3 Signature[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#signature "Permanent link")

The last element of a VC-JWT is the signature which is cryptographically secured to ensure integrity hence making the
Verifiable Credential tamper-proof.

A JWS is signed using the issuer’s private key and can be verified by using the issuer’s public key which is obtainable
through the issuer’s DID document (referenced in the `kid` JWS header).

VC-JWT signatures are created following the [JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515)
specification. [Many libraries are available online](https://jwt.io/libraries) to manage JWS creation.

### 5.3.3 Credential Subject[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-subject "Permanent link")

The `credentialSubject` can be an object or array of objects, containing claims.

The claims about one Gaia-X entity may be spread over multiple Credentials and their subjects.

Each credential subject MUST have an [`@id`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers).

A credential subject MAY be described *by value*, i.e., by stating one or more claims about it in place.
In this case, it MUST have a [`@type`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#types) as specified below.

Alternatively, a credential subject MAY be described *by reference*.
In this case, the `@id` MUST be resolvable to an RDF resource that has the same `@id`, a `@type`, and one or more
claims. See [Identifiers](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#identifiers) section for more details.

The value of the `@type` property dictates the vocabulary available in
the [Gaia-X Ontology](https://w3id.org/gaia-x/) for the definition of
claims about the credential subject. E.g., `LegalPerson`, `ServiceOffering`, `DataResource`, …

Example of credentialSubject

```
{
  "@id": "https://example.com/legalPersonABC?vcid=c93b5075b3988eda4a529afce7e7c127f607b55dc08bb12e8c9adc9e33fe814f",
  "@type": "gx:legalPerson",
  "gx:legalName": "Legal Person ABC",
  "gx:legalRegistrationNumber": {
    "@id": "https://gaia-x.eu/legalRegistrationNumber_VC.json"
  },
  "gx:headquarterAddress": {
    "gx:countrySubdivisionCode": "FR-IDF"
  },
  "gx:legalAddress": {
    "gx:countrySubdivisionCode": "FR-IDF"
  }
}
```

## 5.4 Verifiable Credentials[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-credentials "Permanent link")

### 5.4.1 Standard Verifiable Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#standard-verifiable-credential "Permanent link")

Verifiable Credentials are encoded as [Json Web Tokens](https://datatracker.ietf.org/doc/html/rfc7519) as described in
the [VC-JWT specification](https://www.w3.org/TR/vc-jose-cose/). This type of proof is
an [enveloping proof](https://www.w3.org/TR/vc-data-model-2.0/#securing-mechanisms).

A JWT consists of a header, a payload and a signature, each element being separated by a dot (`.`).

Example Verifiable Credential
If we use the following credential:

```
{
  "@context": [
    "https://www.w3.org/2018/credentials/v2",
    "https://w3id.org/gaia-x/development#"
  ],
  "@type": [
    "VerifiableCredential",
    "LegalParticipant"
  ],
  "@id": "https://example.org/legal-participant/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",
  "issuer": "did:web:example.org",
  "validFrom": "2024-04-01T12:26:22.601516+00:00",
  "validUntil": "2024-01-01T12:26:22.601516+00:00",
  "credentialSubject": {
    "id": "https://example.org/legal-participant-json/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json",
    "type": "gx:LegalPerson",
    "gx:legalName": "Example Org",
    "gx:legalRegistrationNumber": {
      "id": "https://example.org/gaiax-legal-registration-number/68a5bbea9518e7e2ac1cc75bcc8819a7edd5c4711e073ffa4bb260034dc6423c/data.json"
    },
    "gx:headquarterAddress": {
      "gx:countrySubdivisionCode": "FR-75"
    },
    "gx:legalAddress": {
      "gx:countrySubdivisionCode": "FR-75"
    }
  }
}
```

The VC-JWT representation as a Verifiable Credential would be:

```
eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA
```

To view the header, payload and signature of this example on
JWT.io [click here](https://jwt.io/#debugger-io?token=eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmcjSldLMjAyMC1SU0EifQ.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MiJdLCJAdHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkxlZ2FsUGFydGljaXBhbnQiXSwiQGlkIjoiaHR0cHM6Ly9leGFtcGxlLm9yZy9sZWdhbC1wYXJ0aWNpcGFudC82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsImlzc3VlciI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmciLCJ2YWxpZEZyb20iOiIyMDI0LTA0LTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsInZhbGlkVW50aWwiOiIyMDI0LTAxLTAxVDEyOjI2OjIyLjYwMTUxNiswMDowMCIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7IkBjb250ZXh0IjpbImh0dHBzOi8vcmVnaXN0cnkubGFiLmdhaWEteC5ldS92MS9hcGkvdHJ1c3RlZC1zaGFwZS1yZWdpc3RyeS92MS9zaGFwZXMvanNvbmxkL3RydXN0ZnJhbWV3b3JrIyJdLCJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWwtcGFydGljaXBhbnQtanNvbi82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiIsInR5cGUiOiJneDpMZWdhbFBhcnRpY2lwYW50IiwiZ3g6bGVnYWxOYW1lIjoiRXhhbXBsZSBPcmciLCJneDpsZWdhbFJlZ2lzdHJhdGlvbk51bWJlciI6eyJpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvZ2FpYXgtbGVnYWwtcmVnaXN0cmF0aW9uLW51bWJlci82OGE1YmJlYTk1MThlN2UyYWMxY2M3NWJjYzg4MTlhN2VkZDVjNDcxMWUwNzNmZmE0YmIyNjAwMzRkYzY0MjNjL2RhdGEuanNvbiJ9LCJneDpoZWFkcXVhcnRlckFkZHJlc3MiOnsiZ3g6Y291bnRyeVN1YmRpdmlzaW9uQ29kZSI6IkZSLTc1In0sImd4OmxlZ2FsQWRkcmVzcyI6eyJneDpjb3VudHJ5U3ViZGl2aXNpb25Db2RlIjoiRlItNzUifX19.NxVb\_3t8WE0XWelPZsaKAcME8E28Vi5H0utVvJeYCr6cGKfj9Snl2C7buSpJIz-ZoPAKQJLKK1gWHsMh5Ge1I99vhZZ61vsGBfjLO0gFhLBwpriLMW7YkJnKD4QoTv-RxBX3JCakUCE\_vkSceUOeRUfJKfEEfbyAAMjBnRZsbeH7xt5MLrs482TxYx2HhSdNkxVZU4UHK0hGSauoGfZrHV5e7XT4N2q4vXIRfN3iihYbw4-27sSDgNwOkuY34lWwRZSQsP3PoBneJcH0KDvEPgKvOt8V9ZM78wbyH9NIae8qAEKwVNF61cs3XQx6-0bqI6h0n9I4C93ShXxrqmjgTA).

### 5.4.2 Enveloped Verifiable Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-credential "Permanent link")

An Enveloped Verifiable Credential is a convenient way of describing a Verifiable Credential that has been encoded with
an enveloping proof such as VC-JWT.

It is represented as a basic JSON object with three fields:

- `@context` which is usually set to `https://www.w3.org/ns/credentials/v2`
- `id` containing the data of the VC-JWT in the form of
  an `application/vc+jwt` [data URL](https://www.rfc-editor.org/rfc/rfc2397)
- `type` which MUST be set to `EnvelopedVerifiableCredential`

This type of Verifiable Credential is very useful in the context of
a [Verifiable Presentation](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-presentation)
to embed multiple Verifiable Credentials.

Example Enveloped Verifiable Credential
Below is an example representing the [Verifiable Credential example](#verifiable-credential) as an Enveloped Verifiable
Credential.

```
{
  "@context": "https://www.w3.org/ns/credentials/v2",
  "id": "data:application/vc+jwt;eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmc6bGVnYWxQZXJzb25BQkMja2V5In0.eyJAaWQiOiJkaWQ6d2ViOmV4YW1wbGUub3JnOmxlZ2FsUGVyc29uQUJDIiwiQHR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiXSwiaXNzdWVyIjoiZGlkOndlYjpleGFtcGxlLm9yZzpsZWdhbFBlcnNvbkFCQyIsInZhbGlkRnJvbSI6IjIwMjQtMDEtMDFUMDA6MDA6MDBaIiwidmFsaWRVbnRpbCI6IjIwMjQtMDQtMDFUMDA6MDA6MDBaIiwiY3JlZGVudGlhbFN1YmplY3QiOlt7IkBpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWxQZXJzb25BQkMiLCJAdHlwZSI6Imd4OmxlZ2FsUGVyc29uIiwiZ3g6bGVnYWxOYW1lIjoiTGVnYWwgUGVyc29uIEFCQyIsImd4OmxlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyIjp7IkBpZCI6Imh0dHBzOi8vZ2FpYS14LmV1L2xlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyX1ZDLmpzb24ifSwiZ3g6aGVhZHF1YXJ0ZXJBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifSwiZ3g6bGVnYWxBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifX1dfQ.RIQKYwKsYEhH9p3m9tbG6zQKae3A7Qz3oAHXMI9RwXYVCL-euaBG7fWGTQ_F6yqWSPeQ6veHqkxKkvtdLIkSSpxZRJCtQs2HiORQX3tc21dkqtziKJIDJhmIBIq-2zDToPb5D4Yb_ryP0aTgcnBavAuiNCf7x3_gS6tBtYd_ZNnh3cifFiLGLop6PUhqhaTEYBlw1ou-28XUCHPeaarGrmxyZzxiBV_3J5hAe8XvfnFo9Y__LcbuOjNMsU2kKhI9otw9Ll4C8IZ9Qsqdq52QFCvkbvtcvX_3IJpzyxSS7TxOXAPPwYbYV_u7tgygPRvvmQG99Q651y62tQGA_B6Eqg",
  "type": "EnvelopedVerifiableCredential"
}
```

## 5.5 Verifiable Presentations[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-presentations "Permanent link")

### 5.5.1 Standard Verifiable Presentation[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#standard-verifiable-presentation "Permanent link")

If the `@type` is `VerifiablePresentation`, the property `verifiableCredential` MUST be defined.
The value of `verifiableCredential` property MUST be an array of one or more
[Enveloped Verifiable Credentials](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-credential).
A Verifiable Presentation MUST have:

- a [`@type`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#types),
- a [`verifiableCredential`](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-credential) array of `EnvelopedVerifiableCredential`,

Example Verifiable Presentation
Below is an example of a Verifiable Presentation containing the example from
the [Enveloped Verifiable Credential](#enveloped-verifiable-credential)
chapter.

```
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2"
  ],
  "@id": "https://gaia-x.eu/verifiablePresentation/1",
  "type": [
    "VerifiablePresentation"
  ],
  "verifiableCredential": [
    {
      "@context": "https://www.w3.org/ns/credentials/v2",
      "id": "data:application/vc+jwt;eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmc6bGVnYWxQZXJzb25BQkMja2V5In0.eyJAaWQiOiJkaWQ6d2ViOmV4YW1wbGUub3JnOmxlZ2FsUGVyc29uQUJDIiwiQHR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiXSwiaXNzdWVyIjoiZGlkOndlYjpleGFtcGxlLm9yZzpsZWdhbFBlcnNvbkFCQyIsInZhbGlkRnJvbSI6IjIwMjQtMDEtMDFUMDA6MDA6MDBaIiwidmFsaWRVbnRpbCI6IjIwMjQtMDQtMDFUMDA6MDA6MDBaIiwiY3JlZGVudGlhbFN1YmplY3QiOlt7IkBpZCI6Imh0dHBzOi8vZXhhbXBsZS5vcmcvbGVnYWxQZXJzb25BQkMiLCJAdHlwZSI6Imd4OmxlZ2FsUGVyc29uIiwiZ3g6bGVnYWxOYW1lIjoiTGVnYWwgUGVyc29uIEFCQyIsImd4OmxlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyIjp7IkBpZCI6Imh0dHBzOi8vZ2FpYS14LmV1L2xlZ2FsUmVnaXN0cmF0aW9uTnVtYmVyX1ZDLmpzb24ifSwiZ3g6aGVhZHF1YXJ0ZXJBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifSwiZ3g6bGVnYWxBZGRyZXNzIjp7Imd4OmNvdW50cnlTdWJkaXZpc2lvbkNvZGUiOiJGUi1JREYifX1dfQ.RIQKYwKsYEhH9p3m9tbG6zQKae3A7Qz3oAHXMI9RwXYVCL-euaBG7fWGTQ_F6yqWSPeQ6veHqkxKkvtdLIkSSpxZRJCtQs2HiORQX3tc21dkqtziKJIDJhmIBIq-2zDToPb5D4Yb_ryP0aTgcnBavAuiNCf7x3_gS6tBtYd_ZNnh3cifFiLGLop6PUhqhaTEYBlw1ou-28XUCHPeaarGrmxyZzxiBV_3J5hAe8XvfnFo9Y__LcbuOjNMsU2kKhI9otw9Ll4C8IZ9Qsqdq52QFCvkbvtcvX_3IJpzyxSS7TxOXAPPwYbYV_u7tgygPRvvmQG99Q651y62tQGA_B6Eqg",
      "type": "EnvelopedVerifiableCredential"
    }
  ]
}
```

### 5.5.2 Enveloped Verifiable Presentation[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-presentation "Permanent link")

Just like an [Enveloped Verifiable Credential](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#enveloped-verifiable-credential), an Enveloped Verifiable Presentation
is a representation of a [Verifiable Presentation](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-presentation) in the form of a basic JSON object
containing
an `application/vp+jwt` [data URL](https://www.rfc-editor.org/rfc/rfc2397).

This data URL expresses a JWS secured Verifiable Presentation.
The same headers as [Verifiable Credentials](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#verifiable-credential) are used in a Verifiable Presentation VC-JWT
except:

- the `typ` header is set to `vp+jwt`
- the `cty` header is set to `vp`

Example Enveloped Verifiable Presentation
Below is a representation of the [Verifiable Presentation example](#verifiable-presentation) as an Enveloped Verifiable
Presentation.

```
{
  "@context": "https://www.w3.org/ns/credentials/v2",
  "id": "data:application/vp+jwt;eyJhbGciOiJQUzI1NiIsInR5cCI6InZjK2xkK2pzb24rand0IiwiY3R5IjoidmMrbGQranNvbiIsImtpZCI6ImRpZDp3ZWI6ZXhhbXBsZS5vcmc6bGVnYWxQZXJzb25BQkMja2V5In0.eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvbnMvY3JlZGVudGlhbHMvdjIiXSwiQGlkIjoiaHR0cHM6Ly9nYWlhLXguZXUvdmVyaWZpYWJsZVByZXNlbnRhdGlvbi8xIiwidHlwZSI6WyJWZXJpZmlhYmxlUHJlc2VudGF0aW9uIl0sInZlcmlmaWFibGVDcmVkZW50aWFsIjpbeyJAY29udGV4dCI6Imh0dHBzOi8vd3d3LnczLm9yZy9ucy9jcmVkZW50aWFscy92MiIsImlkIjoiZGF0YTphcHBsaWNhdGlvbi92YytsZCtqc29uK2p3dDtleUpoYkdjaU9pSlFVekkxTmlJc0luUjVjQ0k2SW5aaksyeGtLMnB6YjI0cmFuZDBJaXdpWTNSNUlqb2lkbU1yYkdRcmFuTnZiaUlzSW10cFpDSTZJbVJwWkRwM1pXSTZaWGhoYlhCc1pTNXZjbWM2YkdWbllXeFFaWEp6YjI1QlFrTWphMlY1SW4wLmV5SkFhV1FpT2lKa2FXUTZkMlZpT21WNFlXMXdiR1V1YjNKbk9teGxaMkZzVUdWeWMyOXVRVUpESWl3aVFIUjVjR1VpT2xzaVZtVnlhV1pwWVdKc1pVTnlaV1JsYm5ScFlXd2lYU3dpYVhOemRXVnlJam9pWkdsa09uZGxZanBsZUdGdGNHeGxMbTl5Wnpwc1pXZGhiRkJsY25OdmJrRkNReUlzSW5aaGJHbGtSbkp2YlNJNklqSXdNalF0TURFdE1ERlVNREE2TURBNk1EQmFJaXdpZG1Gc2FXUlZiblJwYkNJNklqSXdNalF0TURRdE1ERlVNREE2TURBNk1EQmFJaXdpWTNKbFpHVnVkR2xoYkZOMVltcGxZM1FpT2x0N0lrQnBaQ0k2SW1oMGRIQnpPaTh2WlhoaGJYQnNaUzV2Y21jdmJHVm5ZV3hRWlhKemIyNUJRa01pTENKQWRIbHdaU0k2SW1kNE9teGxaMkZzVUdWeWMyOXVJaXdpWjNnNmJHVm5ZV3hPWVcxbElqb2lUR1ZuWVd3Z1VHVnljMjl1SUVGQ1F5SXNJbWQ0T214bFoyRnNVbVZuYVhOMGNtRjBhVzl1VG5WdFltVnlJanA3SWtCcFpDSTZJbWgwZEhCek9pOHZaMkZwWVMxNExtVjFMMnhsWjJGc1VtVm5hWE4wY21GMGFXOXVUblZ0WW1WeVgxWkRMbXB6YjI0aWZTd2laM2c2YUdWaFpIRjFZWEowWlhKQlpHUnlaWE56SWpwN0ltZDRPbU52ZFc1MGNubFRkV0prYVhacGMybHZia052WkdVaU9pSkdVaTFKUkVZaWZTd2laM2c2YkdWbllXeEJaR1J5WlhOeklqcDdJbWQ0T21OdmRXNTBjbmxUZFdKa2FYWnBjMmx2YmtOdlpHVWlPaUpHVWkxSlJFWWlmWDFkZlEuUklRS1l3S3NZRWhIOXAzbTl0Ykc2elFLYWUzQTdRejNvQUhYTUk5UndYWVZDTC1ldWFCRzdmV0dUUV9GNnlxV1NQZVE2dmVIcWt4S2t2dGRMSWtTU3B4WlJKQ3RRczJIaU9SUVgzdGMyMWRrcXR6aUtKSURKaG1JQklxLTJ6RFRvUGI1RDRZYl9yeVAwYVRnY25CYXZBdWlOQ2Y3eDNfZ1M2dEJ0WWRfWk5uaDNjaWZGaUxHTG9wNlBVaHFoYVRFWUJsdzFvdS0yOFhVQ0hQZWFhckdybXh5Wnp4aUJWXzNKNWhBZThYdmZuRm85WV9fTGNidU9qTk1zVTJrS2hJOW90dzlMbDRDOElaOVFzcWRxNTJRRkN2a2J2dGN2WF8zSUpwenl4U1M3VHhPWEFQUHdZYllWX3U3dGd5Z1BSdnZtUUc5OVE2NTF5NjJ0UUdBX0I2RXFnIiwidHlwZSI6IkVudmVsb3BlZFZlcmlmaWFibGVDcmVkZW50aWFsIn1dfQ.jnEqD2HH7eNnzRPwTjwsFigyENPozdDzmksXjevGNiH4hWJGLoM-765IP1mEE-tsLi2tMXQ6TeWIfw_6NkpY0vo_FUXWBBlj0IgMbxbt0gQwHRW9Ph3SVKQMCdIfp_pmdWPCEUrr_HxjkdiZpF1fa4qGSYBYl6tRSf1N0iCY0SzKvStI-EiudwHtlSygcqjxNq1jdpZtQyjYa_golZmyBdX7BYUUkcY30vypKTjMgBLHlZOzIljdiLKcm_MfDGEBt-Ha_qxpKpwRZoMFhsq89RXeExpeAw8Vg3ZR7yWsmP3T-7DDrZ5sadpNyCDXpryvm2UoDs__M4lEvkl3HIy9LQ",
  "type": "EnvelopedVerifiablePresentation"
}
```

## 5.6 Issuer Requirements[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#issuer-requirements "Permanent link")

The `issuer` property MUST be present in a Verifiable Credential and a Verifiable Presentation. The value of the `issuer`
property MUST be a resolvable URI.

The supported schemes for `issuer`’s URI are:

- `https`
- `did`. The supported [DID methods](https://w3c.github.io/did-spec-registries/#did-methods) are:
- `web`

The DID Methods supported by the different Gaia-X software releases are listed in the [Architecture Document](https://gaia-x.gitlab.io/technical-committee/architecture-working-group/architecture-document/).

Note

Temporal Validity:

validFrom Property - The [`validFrom`](https://www.w3.org/TR/vc-data-model-2.0/#validity-period) property is mandatory in a Verifiable Credential and a Verifiable Presentation.

validUntil Property - The [`validUntil`](https://www.w3.org/TR/vc-data-model-2.0/#validity-period) property is recommended in a Verifiable Credential and a Verifiable Presentation.

## 5.7 Additional Features[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#additional-features "Permanent link")

### 5.7.1 Integrity of Related Resources[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#integrity-of-related-resources "Permanent link")

In order to enable reference to objects - Verifiable Credentials or credential subject - which are not under control of
the same issuers, it is recommended to specify an `@sri` [Subresource Integrity](https://www.w3.org/TR/SRI/) attribute
to enable the verification of the integrity of the referenced object.

The `sri` attribute is computed by taking the hash of the referenced normalised JSON object.  
The JSON object is normalised following the JSON Canonicalization Scheme (JCS) defined in
the [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785).

Example of `sri` attribute

SRI attribute

```
{
  "@id": "https://example.com/ABC",
  "sri": "sha256-b9a822666c3569a8ae80c897a1984f68bbdffa1f8141cacdb3f168b1c0b9aa36"
}
```

### 5.7.2 Credential Lifecycle and Status[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/gaia-x_credentials/#credential-lifecycle-and-status "Permanent link")

Verifiable Credentials are a fundamental component of secure data and identity systems, enabling the issuance and presentation of trustworthy and tamper-proof credentials. However, in dynamic and evolving environments, it is crucial to establish mechanisms for the timely revocation or suspension of these credentials in case of compromised or outdated information.

A Verifiable Credential can have one of the following statuses:

- **expired** if the `validUntil` attribute is older than the current datetime or the certificate containing the key used to sign the claim has expired.
- **revoked**
- if the keypair used to sign the array is revoked.
- if the **credentialStatus** has the **statusPurpose** property set to **“revocation”** and the value of status at position **credentialIndex** is **true**
- **suspended** if the **credentialStatus** has the **statusPurpose** property set to **“suspension”** and the value of status at position **credentialIndex** is **true**
- **deprecated** if another verifiable credential with the same identifier and the same signature issuer has a newer issuance datetime.
- **active** only if none of the above.

The use of Credential Status Lists (CSL), specifically the [W3C Verifiable Credentials Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/), addresses this need by providing a standardised approach to manage and communicate the revocation status of Verifiable Credentials.

When a Verifiable Credential is issued, the issuer has the option to embed a reference to the Credential Status List (CSL) entry associated with the credential. This reference, often in the form of a Uniform Resource Identifier (URI), enables relying parties (commonly verifiers) to promptly determine the current status of the credential’s validity.

To validate the Verifiable Credential, the relying party retrieves the referenced Credential Status List entry using the provided URI. This entry contains information about the status of the credential, allowing to check if the credential is still valid, has been revoked/suspended, or has any other relevant status.

Relying parties can periodically update their local copy of the Credential Status List from trusted sources to ensure they possess the most current revocation status information. This practice prevents reliance on outdated or incorrect information, enhancing the overall security of the ecosystem.

| party\_credential\_revocation.json | |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 ``` | ``` {   "@context": [     "https://www.w3.org/ns/credentials/v2",     "https://w3id.org/gaia-x/development#"   ],   "id": "https://did.actor/alice/credentials/status/3",   "type": ["VerifiableCredential", "BitstringStatusListCredential"],   "issuer": "did:web:did.actor:alice",   "issued": "2021-04-05T14:27:40Z",   "credentialSubject": {     "id": "https://example.com/status/3#list",     "type": "BitstringStatusList",     "statusPurpose": "revocation",     "encodedList": "H4sIAAAAAAAAA-3BMQEAAADCoPVPbQwfoAAAAAAAAAAAAAAAAAAAAIC3AYbSVKsAQAAA"   } } ``` |

November 28, 2025


November 28, 2025
