# 6. ICAM Semantic Model[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#icam-semantic-model "Permanent link")

## 6.1 Trust Scope Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#trust-scope-credential "Permanent link")

The Trust Scope Credential is based on the [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) and has the purpose of providing a machine-readable representation of the accreditation of a Trust Service Provider for a specific scope. This credential enables the usage of Party Credentials, described later in this chapter, by defining their accredited issuers. Furthermore, the Trust Scope Credential supports the cooperation and interoperability between organisations/ecosystems/data spaces, by easing the use of external Trust Service Providers.

The **TrustScopeCredential** mainly defines:

- The **Scope** within which the Trust Service Provider is accredited (within which the issued credentials are considered valid).
- The **TrustedIssuers**  entitled to issue **Credentials** in the above **Scope**
- The **Vocabularies** (expressed in SHACL) that semantically define the **Credentials** which can be issued by the **TrustedIssuer** in the defined **Scope**.
- The **Trusted List** used to check DIDs issued by the Trust Service Provider.

The `Trust Scope Credential` is defined by the following attributes:

| Attribute | Type.Value/Voc | Mandatory | Comment |
| --- | --- | --- | --- |
| `gx:scopeDescription` | String | No | A description of the scope of the Trust Service Provider |
| `gx:trustIssuers` | DID[] | Yes | A list of resolvable link(s) to the issuer verificationMethod to be used to uniquely identify ONE and ONLY key pair |
| `gx:vocabularies` | URI[] | No | A list of URIs pointing to the vocabularies/schemas (SHACL) semantically describing the Trust Service Provider’s scope |
| `gx:trustedListKind` | KindOfTrustedList | No | Which kind of implementation of the trusted list is used to check DID issued by Trust Anchors |
| `gx:trustedListEndpoint` | URI | No | The address of the above trusted list |

The **KindOfTrustedList** type defines the list of the identified implementations of Trusted Lists:

- Gaia-X Trusted List Generic REST API Specification
- Gaia-X IPFS (with ETSI TS 119 612 format)
- TRAIN
- EBSI
- (other possible implementations)

**Important Note**
The *Gaia-X Trusted List Generic REST API Specification* is meant to be a simple API contract that for a given DID can return “true” if it is still valid. This will be very useful to enable integration of any custom trusted list not included in the defined list.

### 6.1.1 Trust Scope Credential specialisation examples[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#trust-scope-credential-specialisation-examples "Permanent link")

Several specialisations of the **TrustScopeCredential** can be easily defined, for example:

#### 6.1.1.1 **Organization Trust Scope**[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#organization-trust-scope "Permanent link")

This specialisation is a self-issued credential that entitles the issuing organization to define its *Roles/Identity Attributes* to be used by identify and authorise its parties:

- **scope** - *Organization Credential Management* (OCM).
- **trusted issuers** - the organisation itself.
- **vocabularies** - defines the semantics of *Roles/Identity Attributes* and **Domain Specific Credentials** that are valid in the defined scope.
- **trusted list** - to assign and revoke *Roles/Identity Attributes* and **Domain Specific Credentials** to its parties (users, natural persons, endpoint services, etc) by issuing **PartyCredentials**.

#### 6.1.1.2 **Gaia-X Compliance Trust Scope**[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#gaia-x-compliance-trust-scope "Permanent link")

This credential is issued by Gaia-X and entitles an organisation to issue attestations about specific claims in the context of Gaia-X Compliance.

- **scope** - issue attestations used to attest Gaia-X Compliance.
- **trusted issuers** - the organisation accredited by Gaia-X to issue attestations in the defined scope.
- **vocabularies** - defines the semantic applicable to issue attestations in the defined scope.
- **trusted list** - to assign and revoke attestations issued to Gaia-X Providers. Trust Anchor Credential specialisation examples

#### 6.1.1.3 **Ecosystem Trust Scope**[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#ecosystem-trust-scope "Permanent link")

This specialisation is a self-issued credential that entitles an Ecosystem operator to define:

- **scope** - manage an *Ecosystem* (onboarding/offboarding/role assignment etc.).
- **trusted issuers** - the Ecosystem itself.
- **vocabularies** - defines the semantic of *Roles/Identity Attributes* and **Domain Specific Credentials** valid in the defined scope.
- **trusted list** - to assign and revoke *Roles/Identity Attributes* and **Domain Specific Credentials** to its members (other Participants) issuing **MembershipPartyCredentials**.

### 6.1.2 Federation using Trust Scope Credentials[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#federation-using-trust-scope-credentials "Permanent link")

The **TrustScopeCredential** is designed with interoperability in mind and easily enables implementation of selective, bidirectional and monodirectional trust, and a federation between two or more trusted scopes is the perfect use case. Below are some examples:

#### 6.1.2.1 Monodirectional selective federation between 2 Ecosystems[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#monodirectional-selective-federation-between-2-ecosystems "Permanent link")

Ecosystem A can enable federation with Ecosystem B by simply trusting the **trusted issuers** of the **EcosystemTrustScope** issued by Ecosystem B and selecting which subset of its **Domain Specific Credentials** to trust.

#### 6.1.2.2 Bidirectional full federation between 2 Ecosystems[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#bidirectional-full-federation-between-2-ecosystems "Permanent link")

Ecosystem A enables federation with Ecosystem B by fully trusting the **EcosystemTrustScope** issued by Ecosystem B, and vice versa.

#### 6.1.2.3 Federation managed by an operator that selectively trusts multiple Ecosystems[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#federation-managed-by-an-operator-that-selectively-trusts-multiple-ecosystems "Permanent link")

An Ecosystem operator maintains the list of the **trusted issuers** and relative **Domain Specific Credentials** of the trusted **EcosystemTrustScope** issued by Ecosystems.

**Important Note**
In all the above examples, the *trusting* relationship can be concretely implemented by issuing a [verifiable credential](https://www.w3.org/TR/vc-data-model-2.0/) whose [credentialSubject](https://www.w3.org/TR/vc-data-model-2.0/#credential-subject) is the ID of the **EcosystemTrustScope**. Alternatively, a more fine-grained **TrustRelationCredential** could be designed for that purpose.

## 6.2 Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#party-credential "Permanent link")

The Party Credential is based upon the [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) and is the basis for all IAA Parties such as **Natural Persons** , **Services**, **Legal Persons**, etc.
The general purpose party credential is intended to be extended into specialized Credentials (see **Party Credential Specializations**)

The `Party Credential` is defined by the following attributes:

| Attribute | Type.Value/Voc | Mandatory | Comment |
| --- | --- | --- | --- |
| `gx:holder` | DID | Yes | A resolvable link to the holder verificationMethod to be used to uniquely identify ONE and ONLY key pair |
| `odrl:hasPolicy` | policy[] in ODRL | No | A list of `policy` expressed using ODRL |
| `gx:identityAttributes` | String[] | No | A list of literals representing Identity Attributes to be used in a ABAC context |
| `gx:identityRoles` | String[] | No | A list of literals representing Identity Roles to be used in a RBAC context |
| `gx:parentPartyCredential` | URI | Yes if delegated by another existing Party Credential | A resolvable link to the parent Party Credential where the gx:holder MUST be equal to the signer(issuer verificationMethod) of this credential |

**VERY IMPORTANT NOTE**

The **credentialSubject.id** MUST identify the **DID Document** that contains the **verificationMethod** (keypair) referenced by `gx:holder` property that *belong to/is controlled by* the **Credential Holder**.
With this solution, the PartyCredential VC can be either publicly published in case it contains no sensitive data or kept private in case it contains PII - Personal Identifiable Information.

### 6.2.1 Private Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#private-party-credential "Permanent link")

The **Party Credentials** containing PII are not considered to be published and reachable via their **id** to everybody, instead, they are intended to be stored in secure storage such as a wallet, secure storage device, secure vault storage, etc.
An example of this type of credential is the **NaturalPersonCredential**, issued by a Legal Participant to one of his users/employees, with the purpose to entitle a Natural Person to interact with Relying Parties(RP) in a certain context
This credential contains Name, Surname, identityAttributes, Roles, etc. and MUST NOT be published as Public Party Credentials (see later in this section) are. “Selective disclosure” during interaction with RP can be considered.

#### 6.2.1.1 Private Party Credential Example[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#private-party-credential-example "Permanent link")

The following **NaturalPersonPartyCredential** example represents the scenario where the Participant **did:web:did.actor:alice** is issuing a credential that  asserts several claims (givenName, surname, idRoles etc).
This Credential is not published (the **id** is not public) and MUST be stored in the wallet of the holder.

Note that the `gx:holder` property is a did:key referencing a keypair owned by the **Holder** that identifies the public key of the target wallet.

| party\_credential.json | |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` | ``` {   "@context": [     "https://www.w3.org/ns/credentials/v2",     "https://w3id.org/gaia-x/development#"   ],   "id": "did:web:did.actor:alice:credentials:private#1222331234",   "type": ["VerifiableCredential"],   "issuer": "did:web:did.actor:alice",   "validFrom": "2023-08-28T23:00:00Z",   "credentialSubject": {     "id": "did:key:z4MXj1wBzi9jUstyPMS4jQqB6KdJaiatPkAtVtGc6bQEQEEsKTic4G7Rou3iBf9vPmT5dbkm9qsZsuVNjq8HCuW1w24nhBFGkRE4cd2Uf2tfrB3N7h4mnyPp1BF3ZttHTYv3DLUPi1zMdkULiow3M1GfXkoC6DoxDUm1jmN6GBj22SjVsr6dxezRVQc7aj9TxE7JLbMH1wh5X3kA58H3DFW8rnYMakFGbca5CB2Jf6CnGQZmL7o5uJAdTwXfy2iiiyPxXEGerMhHwhjTA1mKYobyk2CpeEcmvynADfNZ5MBvcCS7m3XkFCMNUYBS9NQ3fze6vMSUPsNa6GVYmKx2x6JrdEjCk3qRMMmyjnjCMfR4pXbRMZa3i",     "type": "gx:NaturalPersonPartyCredential",     "odrl:hasPolicy": [],     "gx:holder": "did:key:z4MXj1wBzi9jUstyPMS4jQqB6KdJaiatPkAtVtGc6bQEQEEsKTic4G7Rou3iBf9vPmT5dbkm9qsZsuVNjq8HCuW1w24nhBFGkRE4cd2Uf2tfrB3N7h4mnyPp1BF3ZttHTYv3DLUPi1zMdkULiow3M1GfXkoC6DoxDUm1jmN6GBj22SjVsr6dxezRVQc7aj9TxE7JLbMH1wh5X3kA58H3DFW8rnYMakFGbca5CB2Jf6CnGQZmL7o5uJAdTwXfy2iiiyPxXEGerMhHwhjTA1mKYobyk2CpeEcmvynADfNZ5MBvcCS7m3XkFCMNUYBS9NQ3fze6vMSUPsNa6GVYmKx2x6JrdEjCk3qRMMmyjnjCMfR4pXbRMZa3i",     "gx:identityAttributes": ["IdAttributeOne","IdAttributeTwo"],     "gx:identityRoles": ["IdRoleOne","IdRoleTwo"],     "gx:givenName": "John",     "gx:surname": "Doe"   },   "credentialStatus": [{     "id": "https://did.actor/alice/credentials/status/3#94567",     "type": "BitstringStatusListEntry",     "statusPurpose": "revocation",     "statusListIndex": "94567",     "statusListCredential": "https://did.actor/alice/credentials/status/3"   },{     "id": "https://did.actor/alice/credentials/status/4#23452",     "type": "BitstringStatusListEntry",     "statusPurpose": "suspension",     "statusListIndex": "23452",     "statusListCredential": "https://did.actor/alice/credentials/status/4"   }],   "proof": {     "type": "JsonWebSignature2020",     "created": "2023-08-28T13:25:35.827Z",     "proofPurpose": "assertionMethod",     "verificationMethod": "did:web:did.actor:alice#JWK2020",     "jws": "eyJhbGciOiJQUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..Sq5VJHCFuIP-cC86EknRnB91WQxNI5X4QtI0mMR3Xzl8VY5bYfOAtpEsejYeDUbi3Oed0VwQBRCqd11HL7NFF-KH02D9I97nHBftBaXo8e0uWQTRk6TA8xq9oQRuNdnm15eR2zudOzKlH4ArXcBo-hUxUH6EH7YimT0Uu5NbsofN-5C2ovksogbugl-NkW3MKrGkAYzsyaEcgh-vSiRwSl4vwE55sDkn16QgMtsccwo9PR0kzECHp8KQZTM3Nwnv4jNN-F3zP-3Vn0B-cm-UgHPz1RYX6uKrc3A4TlJvk9rxQNfLbNot8ZaQBPoLMnd98bV6giNaGIbekVOUuBxUKg"   }   } ``` |

### 6.2.2 Public Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#public-party-credential "Permanent link")

A public party credential is a **Party Credential** containing data that can be publicly accessed and queried.

### 6.2.3 Party Credential Specialisation examples[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#party-credential-specialisation-examples "Permanent link")

Here, some of the possible Party Credential specialisations are defined.

#### 6.2.3.1 Natural Person Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#natural-person-party-credential "Permanent link")

This credential is issued by a Participant to entitle a natural person (usually one of his users/employees) to interact with other Relying Parties belonging to other Participants.

This is how `Natural Person Party Credential` will be defined by the following attributes in addition to Party Credential attributes:

| Attribute | Type.Value/Voc | Mandatory | Comment |
| --- | --- | --- | --- |
| `gx:givenName` | String | Yes | Name of the natural person |
| `gx:surname` | String | Yes | Surname of the natural person |

#### 6.2.3.2 Legal Person Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#legal-person-party-credential "Permanent link")

This credential is issued by a Legal Person Participant to entitle another legal person (usually one of his users  ) to interact with other Relying Parties belonging to other Participants on its behalf.

This is how `Legal Person Party Credential` will be defined by the following attributes in addition to Party Credential attributes:

| Attribute | Type.Value/Voc | Mandatory | Comment |
| --- | --- | --- | --- |
| `gx:organizationIdentifier` | String | Yes | Organization Identifier used in the eIDAS rules |

#### 6.2.3.3 Service Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#service-party-credential "Permanent link")

This credential is issued by a Participant to entitle an automated service (usually an automated process) to interact with other Relying Parties belonging to other Participants.

This is how `Service Party Credential` will be defined by the following attributes in addition to Party Credential attributes

| Attribute | Type.Value/Voc | Mandatory | Comment |
| --- | --- | --- | --- |
| `gx:baseURL` | URI | Yes | The base URL endpoint where the service is accessible |

#### 6.2.3.4 Membership Party Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#membership-party-credential "Permanent link")

This credential is issued by a LegalParticipant that runs an  ecosystem to another Participant in order to attest his Membership status.

## 6.3 Signature Credential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#signature-credential "Permanent link")

The Signature Credential is a Verifiable Credential introduced to express digital signatures in a machine-readable and interoperable form enabling several scenarios ranging from data transaction permissions to agreement signing. It allows participants to cryptographically sign digital resources and bind the signature to the identity of the signer with verifiable integrity.

By using a verification method associated with a certificate issued under a recognized legal trust framework (e.g. eIDAS), the Signature Credential may achieve legal equivalence with handwritten signatures, depending on the assurance level (e.g., Qualified Electronic Signature).

A specialization of this credential, Signed Agreement Credential, introduces revocability to model agreements whose validity may be rescinded over time. These credentials can be issued independently by each participant and later aggregated into a Verifiable Presentation, thus enabling decentralized signature workflows for contracts such as data usage agreements.

Important note: the issuance of a signature credential from a digital identity bound to a human-controlled device/wallet, can be used to realise the “human-in-the-loop” interaction.

This approach promotes semantic clarity, cryptographic assurance, and interoperability across use cases involving legally binding actions, whether initiated by humans or automated agents. It also enables trust anchors and policies defined in the Gaia-X Trust Framework to validate each Signature Credential independently.

### 6.3.1 Multiple Signatures using SignatureCredential specializations[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#multiple-signatures-using-signaturecredential-specializations "Permanent link")

The **SignatureCredential** in the trust model defined by the ICAM Document, represents a general purpose and machine readable *signature* that Participants are asked to provide in several contexts, one of the most important of these contexts is represented by the [Data Transaction](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/...) section of the Data Exchange Document(version…) where this credential will be used to sign **[Data Usage Agreement](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/...)** and **Data Product Usage Contract**.

The concept behind this credential is the same as the credentials issued by the compliance service, to issue Participant Credentials and Service Offering Credentials (using the “credentialSubject” claim), where the **credentialSubject** consists in:

| Attribute | Type.Value/Voc | Mandatory | Comment |
| --- | --- | --- | --- |
| `type` | string | Yes | Indicating the *type* of the subject to be Signed |
| `id` | URI | Yes | A resolvable single URI as defined in the [VC Specification](https://www.w3.org/TR/vc-data-model-2.0/#identifiers) identifying the subject to be Signed |
| `digestSRI` | String | Yes | Integrity of related Resources as defined in [W3C VC Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/#integrity-of-related-resources) to ensure that referenced resource is not changed/modified/tampered(still identical in time) |

Another important factor is represented by the fact that, issuing and signing this credential with a **verificationMethod** bound to a certificate that has legal relevance (e.g eIDAS) gives it the same level of trust, enabling the possibility to check the `gx:legalValidity` property of the **Signature Check Type** (see `gx:signers` property).

#### 6.3.1.1 SignedAgreementCredential[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#signedagreementcredential "Permanent link")

The **SignedAgreementCredential** is a specialization of **SignatureCredential** that represents a *Revocable Signed Agreement* given by a participant to a specific subject (e.g. Data Usage Agreement, GDPR Agreement, etc.) and the only difference is that it can be revoked.

#### 6.3.1.2 Data Usage Agreement Example[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#data-usage-agreement-example "Permanent link")

In a Data Transaction the **Data Provider**(did:web:provider.com) and a **Data Consumer**(did:web:consumer.com) must agree to a **Data Usage Agreement** (**id** “https://provider.com/data-usage-contract.654321”) and this is done treating “Signatures” as a **Verifiable Credential** that each Participant can issue and sign.
In this way, when all Participants have issued their SignatureCredential referencing the contract it will be possible to create Verifiable Presentations that contain all the Signatures.

Here is an example of how CredentialSignature can be used:

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

## 6.4 Ecosystem Onboarding and Offboarding using ICAM Semantic Model[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#ecosystem-onboarding-and-offboarding-using-icam-semantic-model "Permanent link")

The ICAM Semantic Model enables onboarding and offboarding of participants in an ecosystem, ensuring consistent trust and interoperability across federations.  
Defining a Trust Scope establishes the boundaries of mutual recognition within an ecosystem by specifying the types of credentials, policies, and trusted issuers relevant for participation.  
A Trusted Issuer is a recognized entity authorized to issue verifiable credentials that conform to the defined Trust Scope, such as Party Credentials and Onboarding Credentials.  
During onboarding, an entity receives an Onboarding Credential, a specialization of the Party Credential, which attests that the entity has successfully met all policy, identity, and compliance requirements defined by the ecosystem. This credential enables the entity to operate as a trusted participant, interoperable with other data space actors under the same trust framework.  
Conversely, offboarding is achieved through the revocation of the Onboarding Credential, thereby terminating the entity’s ability to participate in trust-based interactions. The revocation event is registered within the trust infrastructure, ensuring that all dependent systems can verify the updated status through verifiable credential mechanisms.

## 6.5 Delegating Access Rights[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#delegating-access-rights "Permanent link")

The ecosystem uses decentralized identity and access management based on Self-Sovereign Identity (SSI) to enhance security, privacy, and flexibility. An organization can provide secure access to their employees for various clouds (e.g., email, document storage, collaboration tools) without relying on a central identity provider. The HR department or respective manager is able to revoke or change roles for an employee if an employee is no longer working for the organization or changes designations.

### 6.5.1 Types of Credentials and Issuers[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#types-of-credentials-and-issuers "Permanent link")

**Employee Credential (specialised PartyCredential)**

The company HR department issues an Employee Credential to each employee. The employee credential contains the employee’s unique identifier, role, department and unique company ID (unique identifier used in the onboarding phase of the company to the ecosystem). The Employee Credential is used to verify the employee’s identity and affiliation with the company. The Company ID MUST be registered in the membership trustlist of the ecosystem and in parallel used in the separate issued membership credential. The HR department MUST revoke the employee’s credential in case he/she leaves the company, and the employee SHOULD NOT be able to access any cloud services on behalf of the company.

Note

The Employee Credential type and the attributes MUST be standardised. The `EmployeeCredential` is a prerequisite for receiving `AccessEntitlementCredentials` and is used to establish the employee’s identity within the organization.

- **Type**: `EmployeeCredential (Specialised Party-Credential)`
- **Issuer**: HR Department
- **Subject**: Employee
- **Company ID**: Global unique identifier for the company or organization (eg. GLEIF ID, VAT,), same across all employees. The Company ID should be used in the membership trustlist and membership credential used to verify the authenticity of the credential.
- **Emp Attributes**: Like, Employee ID, Name, Role, Department

**Access Entitlement Credentials**

The Manager issues AccessEntitlementCredential to grant access to specific cloud services based on the employee’s role and responsibilities. The manager can revoke these credentials to dynamically manage access rights.
The EmployeeCredential is a prerequisite for receiving AccessEntitlementCredentials. The manager MUST be entitled to issue such a credential; therefore, the manager MUST adhere to the following conditions:

- MUST have a valid ManagerCredential issued by the HR department
- MUST be a managing member of the ecosystem
- Company ID MUST be part of the credential to ensure the manager is a valid member of the company.

Therefore, the manager is registered in the membership trustlist of the specific ecosystem services and in parallel he/she holds a valid issued membership credential.

- **Type**: `AccessEntitlementCredential` (for each access right individual credentials MUST be issued)
- **Issuer**: Employee Manager
- **Attributes**: Employee ID, Access Rights (specific cloud services the employee can access)
- **Purpose**: Specifies the services the employee is entitled to access.
- **Scope**: Issued by the respective manager to grant access to specific services based on the employee’s role and responsibilities.
- **Revocation**: Manager who can revoke the credential to dynamically manage access rights. <!–could they differ from the Issuer/Employee manager?>
- **Employee ID**: The employee’s `EmployeeCredential` is a prerequisite for receiving `AccessEntitlementCredentials`.

**Authentication Process**

1. **Employee Presents Credentials**: When accessing a service, the employee presents their `EmployeeCredential` and `AccessEntitlementCredential`.
2. **Verification**: The service verifies:
3. The authenticity of the credentials (ensuring they are issued by the HR department and the respective manager).
4. The validity of the credentials (not revoked).
5. The attributes match the access control policies (e.g., the employee’s role and entitlements align with the service being accessed).

**Revocation Process**

**Revocation List or Registry**: The HR department and managers can revoke credentials by adding them to a revocation list or registry that the services check during the authentication process.

- **Issuer**: HR Department for `EmployeeCredential`, Manager for `AccessEntitlementCredential`.
- **Mechanism**: Could use a decentralized identifier (DID) revocation mechanism or a centralised revocation service, depending on the architecture.

### 6.5.2 Implementation Factors[¶](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/semantic_model/#implementation-factors "Permanent link")

- **Decentralized Identifiers (DIDs)**: Use DIDs for employees, HR, and managers to ensure a decentralized and self-sovereign identity system.
- **Verifiable Data Registry**: Implement a verifiable data registry to store DIDs for validation.
- **Privacy**: Ensure that the system only reveals the minimum necessary information for authentication and access control to protect employee privacy.
- **Interoperability**: Design the credential schema to be interoperable with W3C Verifiable Credentials standards and compatible with the cloud services’ access control mechanisms.
- **Trust** An ecosystem may have many trustlists (Gaia-X , XFCS Ecosystem Member, Service Manager).

November 28, 2025


November 28, 2025
