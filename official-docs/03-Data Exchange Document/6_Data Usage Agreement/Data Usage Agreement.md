# 7. Data Usage Agreement[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/#data-usage-agreement "Permanent link")

Data Usage Agreement (DUA) is a core concept of the Gaia-X data sharing model. It enables Data Rights Holders to control by whom, how and when their data is used (data sovereignty) and it gives the Data Consumer the formal authorization to use the data in accordance with the constraints specified by the Data Rights Holder.

The Gaia-X Data Usage Agreement Protocol defines the DUA structure, the DUA life cycle and the primitives used by the data sharing participants to respect the Gaia-X data sharing model.

The Gaia-X DUA Protocol enables the various actors to participate in a trustfully data sharing transaction according to the Gaia-X model.

[![DUA Protocol Context](images/DUA_Protocol_Context.svg)](./Data Usage Agreement - Data Exchange Document - 25.07 Release_files/DUA_Protocol_Context.svg)

## 7.1 DUA structure[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/#dua-structure "Permanent link")

(DRH: Data Rights Holder, DP: Data Provider, DC: Data Consumer, DUA: Data Usage Agreement).

A DUA contains (the formal LinkML definition of DUA is given in the Gaia-X Ontology - see Annex 1):

1. The Data Consumer Identity.
2. The Data Rights Holder Identity.
3. The Data Provider Identity.
4. The Data Instance Description: a text that is understandable by the DRH and that the DP can map to a specific data set.
5. The Data Access Prerequisites: a set of conditions to be fulfilled by the DC and checked by the DP before providing data access for the DC.
6. The Data Usage Purpose: a text defining the specific purpose of the data usage as agreed between the DRH and the DC.
7. The Data Usage Constraints: a set of constraints to be fulfilled by the DC when using the data set from the Data Product.
8. The Legal Context: a textual version of the above field (it is assumed that the ecosystem provides a service to trustfully translate the above field into a textual format that is legally acceptable by a court).
9. An Expiration Date after which the data usage is not authorized anymore.

[![DUA Structure](images/DUA_Structure.jpg)](./Data Usage Agreement - Data Exchange Document - 25.07 Release_files/DUA_Structure.jpg)

A DUA can be created by anybody and signed through any TSP recognized by the ecosystem. Once signed, a DUA is non-mutable.

A DUA must be notarized through a DUA Notary recognized by the ecosystem. Anybody can request a DUA Notary to notarize a specific DUA. In practice, a DUA will usually be notarized by the DRH or the DC, but it is possible to imagine the emergence of data sovereignty advisers helping DRH in the DUA protocol (DUA templates, DUA dashboards, and so on).

Fields 5 and 6 can be considered confidential by the DRH and/or by the DC, and hence not to be communicated to the DP. Accordingly, there are 2 sets of signatures: one set for the DC and the DRH, which applies to the full DUA and one set which applies only to the fields communicated to the DP.

The digital identities used in the DC signature and in the DRH signature must correspond to the DC Identity and DRH Identity fields. The DC Id entity can be set to the ALL value to authorize data sharing to any DC that fulfills the Data Access Prerequisites and accepts the Data Usage Constraints – this is called a generic DUA.

The Expiration Date is not included in the Signed part of the DUA to enable DUA revocation at any time. The management of expiration dates (and hence the DUA status) is an ecosystem-level trusted service provided by the DUA Notary.

The Data Access Prerequisites field is a set of conditions expressed as,

- an optional ODRL profile, to define the vocabulary and to express ecosystem-level constraints
- an ODRL Policy, to define the specific conditions applicable to this specific data usage
- a set of Permissible Evidence to be produced by the DC to demonstrate that it fulfils the conditions.

A Permissible Evidence is a Verifiable Claim template and a set of Accepted Issuers.
The accepted issuers shall be part of an Issuers catalogue maintained by the ecosystem, with for each issuer the access method and the list of accepted VC templates are specified. Using issuers outside this catalogue would make the DUA applicability verification impossible.

## 7.2 DUA Life Cycle[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/#dua-life-cycle "Permanent link")

The DUA life cycle is quite simple, and the possible states are:

- Draft: during the negotiation between the DRH and the DC
- Signed: when signed by both DRH and DC
- Active: once notarized, and before suspension or revocation and before the expiration date
- Suspended: when the Expiration Date is before today - this status is reversible
- Revoked: used to cancel the validity of a DUA and hence block data access - this status is not reversible
- Deleted

[![DUA Life Cycle](images/DUA_Life_Cycle.jpg)](./Data Usage Agreement - Data Exchange Document - 25.07 Release_files/DUA_Life_Cycle.jpg)

The fact that a DUA is **Active** does not imply that the agreement is valid, i.e. that the entity signing the DUA as DRH is really entitled to sign the DUA, as the data rights holder or as an authorized delegate. The DUA Notary does not check the validity of the agreement during notarization – the notarization action by the DUA Notary is just a third-party recording of an agreement between the DRH and the DC.

To adapt to the various use cases identified in the Gaia-X data sharing model, there are no constraints related to the way in which the DUA field is agreed upon by the DRH and DC and in what order the DUA is signed.

Note

A DUA is not deleted (nor revoked) when DP removes the corresponding Data Product from their catalogue. This is needed to enable the DRH to control how their data is used within the DC scope after the data access phase: the DRH can revoke the DUA in order to forbid further usage by the DC of data they already accessed.

| **DUA States** | **Conditions/Rules** |
| --- | --- |
| Active, Suspended & Revoked | Are handled ONLY by ecosystem-recognized DUA Notaries |
| Revoked | Both DRH and DC can revoke a DUA: the DRH can revoke to enforce their data sovereignty, and the DC to get proof that they did not access the data after a specific date (without having to activate access logs). |
| Deleted | Enables DRH to enforce their right of oblivion (DRH might not want a DUA Notary to remember the fact that they shared specific data with a specific DC). |

## 7.3 DUA Primitives[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/#dua-primitives "Permanent link")

Note: in addition to the specified returned values, all primitives can return a `Technical_Error` value, with optionally an explanation text.

The following primitives are mandatory for all DUA Notaries:

`Notarize_DUA (DUA) -> KO` or `DUA_URI`

- Accepted by anybody
- The DUA Notary checks the DUA syntax, the validity of the signatures (i.e the digital identity of the entities signing the DUA corresponds to the identity fields in the DUA)
- The DUA Notary does not check the validity of the agreement

`Suspend_DUA (DUA_URI) -> OK` or `KO`

- Return `KO` if the URI is not recognized
- Accepted only from the DRH, otherwise returns `KO`
- The DUA must be in the Active state, otherwise returns `KO`
- This primitive also sets the Expiration Date of the DUA to today

`Revoke_DUA (DUA_URI) -> OK` or `KO`

- Return `KO` if the URI is not recognized
- Accepted only from the DRH or the DC, otherwise returns `KO`
- The DUA must be in the Active state or in the Suspended state (i.e. not already revoked), otherwise returns `KO`
- This primitive also sets the Expiration Date of the DUA to today

`Extend_DUA (DUA_URI, End_Date) -> OK` or `KO`

- Return `KO` if the URI is not recognized
- Accepted only from the DRH, otherwise returns `KO`
- Applies to Active or Suspended DUA, otherwise returns `KO`
- Return `KO` if the `End_Date` is before today (i.e. it is not possible to retroactively expire a DUA)
- If the DUA is in the Suspended state, then it becomes Active again
- The primitive sets the Expiration Date of the DUA to the provided `End_Date`

`Delete_DUA (DUA_URI) -> OK` or `KO`

- Return `KO` if the URI is not recognized
- Accepted only from the DRH, otherwise returns `KO`
- Applies to revoked DUA only, otherwise returns `KO`
- The primitive removes the DUA from the DUA Notary database, and all the history log - only the `DUA_URI` will be kept to prevent reuse
- Any primitive call using this `DUA_URI` will result in a `KO` response

`Get_DUA_Content (DUA_URI) -> Signed_DUA` (signed by the DUA Notary)

- Return `KO` if the URI is not recognized or if the DUA is Deleted
- Accepted only from the DRH, the DC and the DP otherwise returns `KO`
- If received from the DP, only the part visible to the DP is returned
- Applies to Active, Suspended and Revoked DUA.
- Note: depending on the ecosystem rules, auditors mandated by the ecosystem authority might also have access to the DUA content, but they usually use specific means and not this primitive.

`Get_DUA_Status (DUA_URI) -> KO` or `Signed_Status` (signed by the DUA Notary)

- Return `KO` if the URI is not recognized or if the DUA is Deleted
- Accepted only from the DRH, the DC and the DP otherwise returns `KO`
- The status contains: the current date and either `Active` or `Suspended` or `Revoked` or `Deleted`

`Get_DUA_History (DUA_URI) -> KO` or `Signed_Log` (signed by the DUA Notary)

- Return `KO` if the URI is not recognized or if the DUA is Deleted
- Accepted only from the DRH, otherwise returns `KO`
- Return the logs of primitives calls on the `DUA_URI`, with for each call: the identity of the caller, the parameters and the responses

Note

Depending on the ecosystem rules, auditors mandated by the ecosystem authority might also have access to the DUA history, but they usually use specific means and not this primitive.

The following primitives are optional:

`Check_DUA_Validity (DUA_URI) -> KO` or `Signed_report` (signed by the DUA Notary)

- Return `KO` if the URI is not recognized or if the DUA is Deleted
- Accepted only from the DRH, the DC and the DP otherwise returns `KO`
- The validity report contains: the current date, a validity index between 0 and 100 and optionally a report of the assessments performed to calculate the validity index.
- The rules to assess the validity are defined by the ecosystem:
  an index of 0 means that there is evidence that some mandatory rules are not fulfilled,
  an index of 100 means that the DUA Notary has been able to collect evidence that all mandatory rules are fulfilled, intermediate values are defined by the ecosystem rules.

`Check_DUA_Applicability (DUA_URI) -> KO` or `Signed_report` (signed by the DUA Notary)

- Return `KO` if the URI is not recognized or if the DUA is Deleted
- Accepted only from the DRH, the DC and the DP otherwise returns `KO`
- The applicability report contains: the current date, the applicability state and optionally a report of the assessments performed. The applicability state can be `Applicable`, `Not_Applicable` or `Unknown` (unable to check the validity of some of the provided Verifiable Claims, for instance, when all Accepted Issuers are (temporarily) unavailable).

## 7.4 Appendix: DUA Negotiation Cases[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/#appendix-dua-negotiation-cases "Permanent link")

This appendix describes the DUA negotiation corresponding to the 3 main cases identified in the Data Product operating models.

They are:

**In the first case** (generic DUA), the DRH want to express conditions on access and usage of their data but doesn’t want to “control” who is using their data. An example is the case of a person accepting that his/her medical data is used for research purposes by non-profit academics with an appropriate cybersecurity level.

In this case, the DUA is pre-filled and signed by the DRH, with the Data Consumer Id set to `ALL`. This pre-filled DUA is communicated to the DP who stores it with the Data Product. Data Consumers interested in the data retrieve the pre-filled DUA, check that the access and usage conditions are OK with them, countersign the DUA and send it to a DUA Notary for notarization.

[![DUA negotiation Case 1](images/DUA_Nego_1.jpg)](./Data Usage Agreement - Data Exchange Document - 25.07 Release_files/DUA_Nego_1.jpg)

**In the second case** (direct access), DRH wants to know and control who will use their data, and the DC has direct access to the DRH. An example is the case of a person wanting to give access to their connected watch data to their doctor.

In this case, the DC creates the DUA with all the fields, signs it and communicates it to the DRH. Then, the DRH signs it (there might be some negotiation to get a DUA accepted by both party). Finally, the DUA is sent to a DUA Notary for notarization.

[![DUA negotiation Case 2](images/DUA_Nego_2.jpg)](./Data Usage Agreement - Data Exchange Document - 25.07 Release_files/DUA_Nego_2.jpg)

**In the third case** (no direct access), DRH wants to know and control who will use their data and the DC has no direct access to the DRH. An example is the case of a person accepting that his/her medical data is used for research purposes by non-profit academics with appropriate cybersecurity level, but wants to validate which research laboratory will use their data.

In this case, the DUA is created by the DP (using the access prerequisites and usage constraints defined by the DRH beforehand). This pre-filled DUA is communicated to the DC who will fill the DC Identity and the purpose fields, generates the corresponding Legal Context, signs the DUA and sends it back to the DP. The DP communicates the DUA to the DRH, who signs it and sends it to a DUA Notary for notarization.

Note that, in this case, the DP will see the purpose of the data usage during this negotiation phase. DRHs who want to hide the purpose, have to authorize the DP to communicate their access address to the DC and then conduct the DUA negotiation as in the second case.

[![DUA negotiation Case 3](images/DUA_Nego_3.jpg)](./Data Usage Agreement - Data Exchange Document - 25.07 Release_files/DUA_Nego_3.jpg)

## 7.5 Appendix: Technical Implementation Recommendations for the Specifications[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/data-usage-agreement/#appendix-technical-implementation-recommendations-for-the-specifications "Permanent link")

The formal description in `LinkML` of the Data Usage Agreement can be found in the [Gaia-X Ontology](https://gaia-x.gitlab.io/technical-committee/service-characteristics-working-group/service-characteristics/classes/DataUsageAgreement/).

The following technical specification is being considered for implementation:

- [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) to handle the signature parts of the DUA
- [VC-JWT](https://www.w3.org/TR/vc-jose-cose/#securing-json-ld-verifiable-credentials-with-jose)
- [SD-JWT](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt) that might be useful to selectively disclose fields `5` and `6` as described above.
- [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/) to handle the state of the DUA
- [ODRL](https://www.w3.org/TR/odrl-model/) can be used in order to define `Data Access Prerequisites` and `Data Usage Constraints`
- [ODRL VC Profile](https://gitlab.com/gaia-x/lab/policy-reasoning/odrl-vc-profile) to have a clear link between the ODRL policies and the Verifiable Credentials

September 18, 2025


September 18, 2025
