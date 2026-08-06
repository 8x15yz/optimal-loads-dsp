# 8. Policies

## 8.1 Policies for Data Exchange[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#policies-for-data-exchange "Permanent link")

Policies for data exchange shall reflect different aspects to specify terms and conditions for the data and the exchange of the data. Therefore, such policies have a different scope and concern.

1. Contract Policies that are interoperable to have a clear and unambiguous basis for a contract between the participants. This contract policies should be machine and human readable. They have to contain access and usage policies. [ODRL](https://www.w3.org/TR/odrl-model/) is used as a Policy Definition Language for this purpose.
2. Runtime Policies are derived from the Contract Policies and are used for the execution of the contract policies in the system of the participants. Options for Policy Definition Languages for execution are [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) or [XACML](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xacml).

For the Data Exchange, the focus is on the Contract Policies. The contract is negotiated between the participants of the data exchange by making use of a contract negotiation sequence. The result is a signed contract between the two parties, which is a Description of the data asset and the contract as verifiable credential.

The contract policies contain at least:

- General description of the data asset, the involved parties and the general terms
- Access policies describing the requirements and rules for access to the data at the Data Provider sides
- Usage policies as obligations for the data consumer sides
- Signatures

**Usage control** is an extension to traditional access control. It is about the specification and enforcement of restrictions regulating what must (not) happen to data.

Thus, usage control is concerned with requirements that pertain to data processing (obligations), rather than data access (provisions). Usage control is relevant in the context of intellectual property protection, compliance with regulations, and, more generally, digital rights management.

**Access control** restricts access to resources. The term authorization is the process of granting permission to resources.

Resource owners define attribute-based access control policies for their endpoints and define the attribute values a subject must attest in order to grant access to the resource.

In contrast to access control, the overall goal of usage control is to enforce usage restrictions for data after access is granted. Therefore, the purpose of usage control is to bind policies to exchanged data.
The following specifications ([extracted from IDSA Position Paper about Usage Control](https://internationaldataspaces.org/download/21053/)) are examples of policy classes:

- Allow the Usage of the Data (provides data usage without any restrictions).
- Interval-restricted Data Usage (provides data usage within a specified time interval).
- Duration-restricted Data Usage (allows data usage for a specified time period).
- Location Restricted Policy.
- Perpetual Data Sale (Payment once).
- Data Rental (Payment frequently).
- Role-restricted Data Usage.
- Purpose-restricted Data Usage Policy.
- Restricted Number of Usages (allow data usage for n times).
- Security Level Restricted Policy (allow data access with a specified security level).
- Use Data and Delete it After (allows data usage within a specified time interval with the restriction to delete it at a specified time stamp).
- Attach Policy when Distributed to a Third-party.
- Distribute only if Encrypted.

To express and execute the Contract Policies different information are required during runtime to evaluate the policies. To do so, at least three different information models are required:

- The generic Ecosystem/Gaia-X policy data models for basic discovery and trust negotiation policies.
- The per Ecosystem/Industry specific data model which needs to be understood by all participants of the Ecosystem.
- The per data contract/data asset specific data model which might be irrelevant for someone who does not receive the data but crucial for someone who has to understand the usage restrictions of a specific contract.

### 8.1.1 ODRL[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#odrl "Permanent link")

#### 8.1.1.1 Concepts[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#concepts "Permanent link")

Links:

- [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
- [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)
- [ODRL Implementation Best Practices](https://w3c.github.io/odrl/bp/)
- [ODRL Profile Best Practices](https://w3c.github.io/odrl/profile-bp/)

Open Digital Rights Language (ODRL) is a model for describing the usage of content, including authorized, prohibited, and mandatory actions, the resources on which the actions apply, the actors and participants involved in the actions, usage conditions, and additional information such as responsibilities and regulations.

It allows the implementation of usage control features that complement the access controls usually in place. These usage controls come from licenses and are applied before using data, so they are dependent on each data and its usage environment. Some examples of usage control include authorization of usage for a specific period, anonymization of data before processing, and prohibition of data transfer under certain conditions.

The main concepts are the following:

**Policy**: A policy is a group of rules (which can be permissions, prohibitions, or obligations). It has three child classes:

- **Set**: A generic collection of rules.
- **Offer**: A collection of rules that are offered by an actor designated by the `assigner` property.
- **Agreement**: A collection of rules that have been agreed upon by an actor designated as `assignee` and another actor designated as `assigner`.

[![Policy classes](images/Capture_d_écran_2023-04-21_à_08.48.20.png)](./Policies - Data Exchange Document - 25.07 Release_files/Capture_d_écran_2023-04-21_à_08.48.20.png)

*Figure 8.1.1.1a - Policy Classes*

**Rule**: Rule is the base class defining the rules of policies. It has the following properties:

- asset, which defines the target resource,
- action, which defines the operation to be performed on the resource,
- constraint, which defines the conditions for the rule’s validity (e.g., date > 2020), and
- party, which defines the actors involved in the rule.

It has three child classes:

- **Permission**: This rule grants permission for the assignee to perform the action.
- **Duty**: This rule obliges the assignee to perform the action.
- **Prohibition**: This rule prohibits the assignee from performing the action.

[![Rule classes](images/Capture_d_écran_2023-04-21_à_08.51.10.png)](./Policies - Data Exchange Document - 25.07 Release_files/Capture_d_écran_2023-04-21_à_08.51.10.png)

*Figure 8.1.1.1.b - Rule Classes*

The Duty class can also be used to specify a rule:

- In a permission, it specifies pre-conditions that must be met before granting permission.
- In an obligation, it specifies an action to be performed if the obligation is not fulfilled.
- In a prohibition, it specifies an action to be performed if the prohibition is not respected.

[![Duty uses](images/Capture_d_écran_2023-04-21_à_08.53.41.png)](./Policies - Data Exchange Document - 25.07 Release_files/Capture_d_écran_2023-04-21_à_08.53.41.png)

*Figure 8.1.1.1.c - Duty Uses*

- **Asset**: An asset is a resource or a collection of resources. An asset is the target of a rule to which it applies. A collection can have constraints that allow filtering of the elements of the collection to which a rule applies.

[![Asset definition](images/Capture_d_écran_2023-04-21_à_08.55.35.png)](./Policies - Data Exchange Document - 25.07 Release_files/Capture_d_écran_2023-04-21_à_08.55.35.png)

*Figure 8.1.1.1.d - Asset Definition*

- **Action**: An action is an operation that can be performed on an asset. ODRL defines, among others, the two main actions: “use” and “transfer”. Other actions can be defined in a specific vocabulary or profile.
- **Constraint**: Constraints are logical expressions that allow filtering of different collections. ODRL defines the following logical operators: `or`, `xone`, `and`, and `andSequence`. Comparison operators are defined in the ODRL vocabulary: [ODRL Vocabulary & Expression 2.2#Constraint Operators](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/ODRL%20Vocabulary%20&%20Expression%202.2#Constraint%20Operators.)

[![Capture_d_écran_2023-04-21_à_08.58.39](images/Capture_d_écran_2023-04-21_à_08.58.39.png)](./Policies - Data Exchange Document - 25.07 Release_files/Capture_d_écran_2023-04-21_à_08.58.39.png)

*Figure 8.1.1.1.e - Action and Constraint*

- **Party**: A party is an actor or collection of actors who have a functional role in a rule. The actor can have the role of `assignee` (recipient of the rule) or `assigner` (issuer of the rule). A collection can have constraints that allow filtering of the elements of the collection to which a rule refers.

[![Capture_d_écran_2023-04-21_à_09.00.02](images/Capture_d_écran_2023-04-21_à_09.00.02.png)](./Policies - Data Exchange Document - 25.07 Release_files/Capture_d_écran_2023-04-21_à_09.00.02.png)

*Figure 8.1.1.1.f - Party*

Additional metadata can be used to specify policies. Dublin Core Metadata is recommended for this purpose, for example:

- dc:creator: author of the rule
- dc:description: description of the rule
- dc:issued: publication date
- dc:modified: date of last update
- dc:replaces: identifier of a policy that is replaced
- dc:isReplacedBy: identifier of a policy that replaces the current policy

The policies can use inheritance to reuse existing rules. In case of conflict between the rules, the `conflict` property allows specifying the desired behavior. The vocabulary of ODRL can be extended by using profiles, for example: additional actions, roles of actors.

#### 8.1.1.2 Examples[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#examples "Permanent link")

**File exchange**:

The ODRL file uses the following terms:

- Utilization : https://www.w3.org/TR/odrl-vocab/#term-use
- File transfer : https://www.w3.org/TR/odrl-vocab/#term-distribute
- Payment : https://www.w3.org/TR/odrl-vocab/#term-compensate

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "duty": [
       {
         "assigner": "Data Provider",
         "assignee": "Data Consumer",
         "action": [
           {
             "value": "compensate",
             "refinement": [
               {
                 "leftOperand": "payAmount",
                 "operator": "eq",
                 "rightOperand": { "@value": "500.00", "@type": "xsd:decimal" },
                 "unit": "https://dbpedia.org/resource/Euro"
               }
             ]
           }
         ]
       }
     ]
   }
 ],
 "obligation": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assigner": "Data Consumer",
     "assignee": "Data Provider",
     "action": "distribute"
   }
 ]
}
```

**License Exclusivity**: The term `ensureExclusivity` allows to specify an exclusive license:
the aim of `ensureExclusivity` is to ensure that a rule applied to an asset maintains exclusivity. When used as a ‘Duty’ it explicitly designates the assignee responsible for upholding this exclusivity.

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "obligation": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Provider",
     "action": "ensureExclusivity"
   }
 ]
}
```

**Territories**: the term `odrl:spatial` is used to specify territories.
Restrict the use to the specified territories using the operator `isAnyOf`: in the bellow example `isAnyOf` indicating that a given value is any of the right operand of the Constraint.
Here, the right operand is defined as a list of values, specifically `fr` ( for French) and `es` ( for Spanish). The condition will evaluate to true if the `odrl:spatial` aspect matches any of these values.

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "odrl:spatial",
         "operator": "isAnyOf",
         "rightOperand": {
           "@list": [ "fr", "es" ]
         }
       }
     ]
   }
 ]
}
```

Restrict the use outside of the specified territories with the operator `isNoneOf`: Its purpose is to determine whether a given value is not part of the set defined by the right operand of a constraint. In the bellow example, `isNoneOf` indicating that the assigned data consumer is restricted from using the data in locations categorized as neither French (`fr`) nor Spanish (`es`).

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "odrl:spatial",
         "operator": "isNoneOf",
         "rightOperand": {
           "@list": [ "fr", "es" ]
         }
       }
     ]
   }
 ]
}
```

**Industries**: The term `odrl:industry` is used to specify business sectors. This allows ODRL to apply actions within the specified industry context, such as publishing or the financial industry.
Restrict the use to specified business sectors using the `isAnyOf` operator:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "odrl:industry",
         "operator": "isAnyOf",
         "rightOperand": {
           "@list": [ "automotive" ]
         }
       }
     ]
   }
 ]
}
```

Restrict usage outside of the specified industries using the operator `isNoneOf`:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "odrl:industry",
         "operator": "isNoneOf",
         "rightOperand": {
           "@list": [ "automotive" ]
         }
       }
     ]
   }
 ]
}
```

**Usages**: the term `odrl:product` is used to specify uses to categorize or specify the type of product or service, providing context for the enforcement of a rule.
Restrict usage to the specified uses with the `isAnyOf` operator:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "odrl:product",
         "operator": "isAnyOf",
         "rightOperand": {
           "@list": [ "statistics" ]
         }
       }
     ]
   }
 ]
}
```

Restrict the use outside of the specified uses with the operator `isNoneOf`:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "odrl:product",
         "operator": "isNoneOf",
         "rightOperand": {
           "@list": [ "statistics" ]
         }
       }
     ]
   }
 ]
}
```

**Expiration**: The term `dateTime` The date (and optional time and timezone) of exercising the action of the Rule. Right operand value MUST be an `xsd:date` or `xsd:dateTime` as defined by xmlschema. This vocabulary here is used to specify an expiration date for the permission:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "constraint": [
       {
         "leftOperand": "dateTime",
         "operator": "lt",
         "rightOperand": {
           "@value": "2023-01-01",
           "@type": "xsd:date"
         }
       }
     ]
   }
 ]
}
```

**Sub licensing**: The term `grantUse` allows managing the possibilities of sub-licensing. The main aim of `grantUse` is to enable the assignee to grant the use of the asset to third parties. It allows the assignee to create policies that govern how the asset can be used by third parties. This action is often used when the owner of the asset wants to authorize others to use it under certain conditions or restrictions, and it may involve specifying additional policies or constraints for third-party use.

No sub-licensing right:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "prohibition": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "grantUse"
   }
 ]
}
```

Right to sublicense without restriction:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "grantUse"
   }
 ]
}
```

Sub-licensing to subsidiaries: the `refinement` property is used to restrict the action:

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": [
       {
         "value": "grantUse",
         "refinement": [
           {
             "leftOperand": "recipient",
             "operator": "eq",
             "rightOperand": "subCompanies"
           }
         ]
       }
     ]
   }
 ]
}
```

Example with:

- Territorial restriction
- Restriction on industry sectors
- Usage restriction
- Time limit
- Right to sub-license to subsidiaries without sub-licensing

```
{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": "use",
     "duty": [
       {
         "assigner": "Data Provider",
         "assignee": "Data Consumer",
         "action": [
           {
             "value": "compensate",
             "refinement": [
               {
                 "leftOperand": "payAmount",
                 "operator": "eq",
                 "rightOperand": { "@value": "500.00", "@type": "xsd:decimal" },
                 "unit": "https://dbpedia.org/resource/Euro"
               }
             ]
           }
         ]
       },
       {
         "action": "nextPolicy",
         "target": "https://data-exchange.com/policy:1010"
       }
     ],
     "constraint": [
       {
         "leftOperand": "odrl:spatial",
         "operator": "isAnyOf",
         "rightOperand": {
           "@list": [ "fr", "es" ]
         }
       },
       {
         "leftOperand": "odrl:industry",
         "operator": "isAnyOf",
         "rightOperand": {
           "@list": [ "automotive" ]
         }
       },
       {
         "leftOperand": "odrl:product",
         "operator": "isAnyOf",
         "rightOperand": {
           "@list": [ "statistics" ]
         }
       },
       {
         "leftOperand": "dateTime",
         "operator": "lt",
         "rightOperand": {
           "@value": "2023-01-01",
           "@type": "xsd:date"
         }
       }
     ]
   }
 ],
 "obligation": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assigner": "Data Consumer",
     "assignee": "Data Provider",
     "action": "distribute"
   }
 ]
}


{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:1010",
 "permission": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "assignee": "Data Consumer",
     "action": [
       {
         "value": "grantUse",
         "refinement": [
           {
             "leftOperand": "recipient",
             "operator": "eq",
             "rightOperand": "subCompanies"
           }
         ]
       }
     ],
     "duty": [
       {
         "action": "nextPolicy",
         "target": "https://data-exchange.com/policy:nosublicence-123"
       }
     ]
   }
 ]
}


{
 "@context": "https://www.w3.org/ns/odrl.jsonld",
 "@type": "Set",
 "uid": "https://data-exchange.com/policy:nosublicence-123",
 "prohibition": [
   {
     "target": "https://data-exchange.com/dataset/123",
     "action": "grantUse"
   }
 ]
}
```

#### 8.1.1.3 ODRL Profile for Attribute based access/usage control using Verifiable Credential claims[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#odrl-profile-for-attribute-based-accessusage-control-using-verifiable-credential-claims "Permanent link")

To bridge the gap between ODRL and [Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/) in a useful and interoperable manner,
Gaia-X is working on an ODRL Profile which defines a clear way to refer to Verifiable Credentials in an ODRL Policy.
Specifically, this would give assignors of policies a way to enforce those policies using trustworthy and verifiable claims from an assignee, and in doing so having more trust and confidence in the enforcement of the policy.

This profile, [defined here](https://gitlab.com/gaia-x/lab/policy-reasoning/odrl-vc-profile), defines a few attributes:

- `ovc:constraint`: An ovc:constraint concerns a refinement using Verifiable Credentials, in which the assignee is the holder, consequently a constraint MUST be defined inside an odrl:assignee itself in an odrl:rule. It MUST contain an ovc:leftOperand, an ovc:credentialSubjectType, an odrl:operator and an odrl:rightOperand.
- `ovc:leftOperand`: An ovc:leftOperand MUST contain an attribute of a W3C Verifiable Credential to be evaluated and MUST be in the format of a [JSONPath](https://datatracker.ietf.org/wg/jsonpath/about/).
- `ovc:credentialSubjectType`: An ovc:credentialSubjectType MUST contain the type of the intended W3C Verifiable Credential to evaluate, a relevant context MUST be included for namespacing concerns. An ovc:credentialSubjectType MUST contain the type of the intended W3C Verifiable Credential to evaluate, a relevant context MUST be included for namespacing concerns.

###### 8.1.1.3.0.1 Examples[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#examples_1 "Permanent link")

- An example for adding a restriction on locations using a Gaia-X Legal Participant Verifiable Credential

  ```
  {
    "@context": [
      "http://www.w3.org/ns/odrl.jsonld",
      { "gx" :"https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#" },
      { "ovc": "https://w3id.org/gaia-x/ovc/1/" }
    ],
    "@type": "Offer",
    "uid": "http://example.com/policy/123",
    "profile": "https://w3id.org/gaia-x/ovc/1/",
    "permission": [
      {
        "@type": "Permission",
        "target": "http://example.com/asset/456",
        "action": "http://www.w3.org/ns/odrl/2/play",
        "assigner": "http://example.com/provider",
        "assignee": {
          "ovc:constraint": [
            {
              "ovc:leftOperand": "$.credentialSubject.gx:legalAddress.gx:countrySubdivisionCode",
              "operator": "http://www.w3.org/ns/odrl/2/isAnyOf",
              "rightOperand": [
                "FR-HDF",
                "BE-BRU"
              ],
              "ovc:credentialSubjectType": "gx:LegalParticipant"
            }
          ]
        }
      }
    ]
  }
  ```
- An example for requesting a set vat ID Number using a Gaia-X Legal Registration Number Verifiable Credential

  ```
  {
     "@context": [
        "http://www.w3.org/ns/odrl.jsonld",
        { "gx" :"https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#" },
        { "ovc": "https://w3id.org/gaia-x/ovc/1/" }
     ],
     "@type": "Offer",
     "uid": "http://example.com/policy/124",
     "profile": "https://w3id.org/gaia-x/ovc/1/",
     "permission": [
        {
           "@type": "Permission",
           "target": "http://example.com/asset/456",
           "action": "http://www.w3.org/ns/odrl/2/display",
           "assigner": "http://example.com/provider",
           "assignee": {
              "ovc:constraint": [
                 {
                    "ovc:leftOperand": "$.credentialSubject.gx:vatID",
                    "operator": "http://www.w3.org/ns/odrl/2/eq",
                    "rightOperand": "BE0762747721",
                    "ovc:credentialSubjectType": "gx:legalRegistrationNumber"
                 }
              ]
           }
        }
     ]
  }
  ```
- An example for restriction to a certain license holder such as a jobs that require a license (Truck Driver, Doctor, Lawyer…)

  ```
  {
     "@context": [
        "http://www.w3.org/ns/odrl.jsonld",
        { "ovc": "https://w3id.org/gaia-x/ovc/1/" },
        { "vdl": "https://w3id.org/vdl/v1"}
     ],
     "@type": "Offer",
     "uid": "http://example.com/policy/125",
     "profile": "https://w3id.org/gaia-x/ovc/1/",
     "permission": [
        {
           "@type": "Permission",
           "target": "http://example.com/asset/457",
           "action": "http://www.w3.org/ns/odrl/2/use",
           "assigner": "http://example.com/provider",
           "assignee": {
              "ovc:constraint": [
                 {
                    "ovc:leftOperand": "$.credentialSubject.driversLicense.driving_privileges.vehicle_category_code",
                    "operator": "http://www.w3.org/ns/odrl/2/eq",
                    "rightOperand": "C",
                    "ovc:credentialSubjectType": "vdl:Iso18013DriversLicense"
                 },
                 {
                    "ovc:leftOperand": "$.credentialSubject.driversLicense.driving_privileges.expiry_date",
                    "operator": "http://www.w3.org/ns/odrl/2/lt",
                    "rightOperand": {
                       "@value": "2025-01-01",
                       "@type": "xsd:date"
                    },
                    "ovc:credentialSubjectType": "vdl:Iso18013DriversLicense"
                 }
              ]
           }
        }
     ]
  }
  ```

The ODRL Profile also defines a [Reference Implementation](https://gitlab.com/gaia-x/lab/policy-reasoning/odrl-vc-profile#reference-implementation) with more technical details.

#### 8.1.1.4 Other ODRL Profiles[¶](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/policies/#other-odrl-profiles "Permanent link")

For reference, to be able to extend ODRL even more, additional ODRL Profiles may be found [in this W3C community wiki](https://www.w3.org/community/odrl/wiki/ODRL_Profiles).

September 18, 2025


September 18, 2025
