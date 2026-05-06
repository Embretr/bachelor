# Variability Modeling to Support Customization and Deployment of Multi-Tenant-Aware Software as a Service Applications (`mietzner2009variability`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The paper is 8 pages (pp. 18–25). All sections read in full. The single directly relevant claim (§5.1.3 ¶3 MUST CITE marker) is covered with verbatim quotes, framework detail, and application notes. Limits documented.
  - **Gaps not investigated:** None. The paper is short enough to read fully. Sections on deployment scripting (§7) and prototype implementation (§7.5) were read but contribute no additional claims for the thesis beyond what is documented below.

## Source metadata
- **BibTeX key:** `mietzner2009variability`
- **Reference (APA 7):** Mietzner, R., Metzger, A., Leymann, F., & Pohl, K. (2009). Variability modeling to support customization and deployment of multi-tenant-aware software as a service applications. In *2009 ICSE Workshop on Principles of Engineering Service Oriented Systems (PESOS)* (pp. 18–25). IEEE. https://doi.org/10.1109/PESOS.2009.5068815
- **Tilgang:** IEEE Xplore / NTNU Oria licence (confirmed by watermark: "Authorized licensed use limited to: Norges Teknisk-Naturvitenskapelige Universitet")
- **Raw source:** `../mietzner2009variability.pdf`
- **Coverage in raw:** Full paper, pp. 18–25 (8 pages). PDF pages 1–8 = printed pages 18–25 (offset: PDF page N = printed page N+17).

## Sammendrag (2–3 setninger)

Mietzner et al. (2009) propose applying variability modeling techniques from software product line engineering to multi-tenant SaaS applications, distinguishing customer-driven (external) variability — the configuration options exposed to tenants — from realization-driven (internal) variability — the deployment alternatives transparent only to the provider. The core argument is that SaaS providers face an inherent tension between offering tenant-specific customization and retaining the shared-infrastructure economies of scale that make SaaS economically viable; explicit variability models expressed in OVM notation resolve this tension by making both types of variability manageable. For the thesis, the paper's main contribution is providing a precise conceptual vocabulary — tenant, variation point, variant, binding, customer-driven variability — for the configurable soft-constraint weight mechanism that implements Tilpasningsdyktighet in Ressursplanlegger.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| §5.1.3 Tilpasningsdyktighet (¶3) — configurable constraint weights as technical mechanism | **Core claim** — directly cited in outline as MUST CITE |
| §2.3 TMS as software category — multi-tenant architecture | Partial — paper is about SaaS/multi-tenancy at an architectural level, not TMS as a domain category |
| §4.4 System description — multi-tenant data isolation | Background support — the paper's three deployment patterns (single instance, single configurable instance, multiple instances) are architectural precedent for the data-isolation choice |
| §3.5.8 Iterative development — configurable soft-constraint weights | Background support — paper motivates the design rationale for per-tenant weight configuration |

## Claims this source supports

### Claim 1: "SaaS providers face a dual obligation — offering tenant-specific customisation while maintaining shared-infrastructure economies of scale"

- **Suggested for:** §5.1.3 ¶3 (configurability mechanism rationale); §3.5.8 Learned bullet (Tilpasningsdyktighet motivation)
- **Direkte sitat:** "SaaS providers are faced with two goals, which need to be balanced. Firstly, in order to attract enough customers, they need to cater for the varying requirements of potential tenants by providing the tenant-specific adaptation and deployment of the SaaS application. Secondly, they need to make sure that the variants of their SaaS application retain enough commonalities to exploit the economies of scale." (p. 18)
- **Parafrase:** Multi-tenant SaaS requires simultaneously serving diverse tenant requirements and maintaining shared infrastructure — the tension that variability management addresses.
- **Forbehold:** The paper describes a generic SaaS architecture context; it does not address transport-sector software specifically. The "economies of scale" framing concerns infrastructure costs, not operational efficiency for transport companies.
- **Anvendelse på vårt case:** Ressursplanlegger's per-tenant configurable soft-constraint weights (§3.5.8) are the concrete mechanism resolving this dual obligation in the transport-planning domain: each company's assignment-criteria profile (workload balance, driver preferences, route transitions) is customised via weight bindings, while the solver infrastructure and constraint model remain shared across all tenants.

---

### Claim 2: "The 'single configurable instance' pattern enables per-tenant runtime adaptation through configuration metadata without deploying separate code"

- **Suggested for:** §4.4 ¶2 system description; §3.5.8 iterative development origin note; §5.1.3 ¶3
- **Direkte sitat:** "Single configurable instance: In this pattern, all tenants use the same instance of the SaaS application (or parts thereof). However the instance is configurable on a per-tenant basis. This means that whenever the SaaS application is invoked by the tenant, the instance is adapted during run-time (typically through configuration metadata, e.g., configuration files or configuration entries in a database)." (p. 19)
- **Parafrase:** A single shared codebase serves multiple tenants, each configured via per-tenant metadata records at runtime, preserving shared infrastructure while enabling customisation.
- **Forbehold:** The paper's example is a meeting-planning workflow application (MeetR). The configuration options it illustrates (logo, workflow choice, availability tier) are simpler than Ressursplanlegger's soft-constraint weight space. The paper does not discuss constraint-programming weights specifically.
- **Anvendelse på vårt case:** Ressursplanlegger implements the "single configurable instance" pattern: one deployment serves all transport companies, but each company's soft-constraint weights (workload balance, vehicle preference, transition penalties, overtime status) are stored as per-tenant database records and injected into the solver objective function at planning time — matching the paper's configuration-metadata mechanism precisely.

---

### Claim 3: "Customer-driven (external) variability must be distinguished from realization-driven (internal) variability; only the former is exposed to tenants"

- **Suggested for:** §5.1.3 ¶3; §3.5.8 Learned bullet
- **Direkte sitat:** "In simple terms, external variability is the variability that is communicated to the customer of the product line. In the SaaS context, the customer-driven variability nicely matches with this notion of external variability. [...] In contrast to external variability, internal variability is only visible to the developers of the product line. As such, this kind of variability clearly correlates with the realization-driven variability of a SaaS application." (p. 21)
- **Parafrase:** What the tenant configures (external) is distinct from the provider's internal implementation choices (internal); this separation allows variability to be offered without exposing architectural complexity.
- **Forbehold:** The distinction is used in the paper primarily to manage deployment scripting; the thesis uses it to theorise the boundary between what coordinators can configure and what remains implementation-fixed.
- **Anvendelse på vårt case:** In Ressursplanlegger, external (customer-driven) variability is the soft-constraint weight configuration exposed to the coordinator via the settings UI; internal (realization-driven) variability is the solver-engine selection, constraint model structure, and multi-tenant data isolation — invisible to the tenant. The distinction explains why §3.5.8 exposes weights but not hard-constraint definitions: hard constraints are realization-driven and remain provider-controlled.

---

### Claim 4: "Explicit variability models provide 'a balance between offering (enough) flexibility and managing that flexibility'"

- **Suggested for:** §5.1.3 ¶3 (honest acknowledgement of the limits of Ressursplanlegger's configurable-weight approach)
- **Direkte sitat:** "our approach provides a balance between offering (enough) flexibility and managing that flexibility." (p. 18)
- **Parafrase:** Pre-planned variability necessarily limits flexibility compared to fully open customisation; the value is making that trade-off explicit and manageable.
- **Forbehold:** The paper acknowledges this trade-off as a limitation of its approach rather than as a design virtue; the thesis should represent it accurately and use it to frame the honesty point in §5.1.3 ¶3 about what is not yet configurable.
- **Anvendelse på vårt case:** Ressursplanlegger's current Tilpasningsdyktighet realisation (§3.5.8) exposes soft-constraint weights but leaves hard constraints and status-workflow definitions fixed — an honest application of this balance: enough flexibility to serve materially different assignment-criteria profiles, but bounded by the implementation complexity of exposing hard-constraint configuration.

---

### Claim 5: "Variability of SaaS applications can be driven by customer requirements as well as by realization alternatives for the infrastructure"

- **Suggested for:** §5.1.3 ¶3; §4.4 system description
- **Direkte sitat:** "The variability of SaaS applications can be driven by several sources: Customer-driven Variability: Different customers have different requirements to the application. These differences in requirements require that the SaaS applications are configurable to cater for the varying requirements. [...] Realization-driven Variability: Alternatives for realizing the SaaS application introduce a further level of variation, which needs to be understood." (p. 21)
- **Parafrase:** Variability has two orthogonal origins — what tenants need (business/functional) and how the system can be built (technical/infrastructure).
- **Forbehold:** The paper discusses these as distinct categories to be modelled separately; the thesis need not reproduce the full OVM notation, but must correctly attribute the distinction.
- **Anvendelse på vårt case:** The interviews established that different Norwegian transport companies have different assignment-criteria profiles — this is customer-driven variability in Mietzner's terms. The choice of solver engine per instance size is realization-driven variability. Ressursplanlegger addresses customer-driven variability through configurable weights and realization-driven variability through the pluggable solver registry (§3.5.4).

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Tenant | Transport company (kunde av Ressursplanlegger) | One company = one tenant in the multi-tenant architecture |
| Customer-driven variability / external variability | Per-company soft-constraint weight configuration | What the coordinator configures in settings |
| Realization-driven variability / internal variability | Solver-engine selection, constraint model, data isolation | Implementation choices not exposed to the tenant |
| Variation point (VP) | A configurable soft-constraint dimension (e.g., "workload balance weight") | Each VP has a set of variants (weight values) the tenant can bind |
| Variant | A specific weight value or rule-set binding for a VP | E.g., "high workload-balance priority" vs "low" |
| Binding | Setting a specific weight value for a VP at tenant configuration time | Done via settings UI by the company admin |
| Single configurable instance | Ressursplanlegger's deployment model | One shared codebase, per-tenant metadata rows in DB |
| Configuration metadata | Per-tenant weight-configuration rows in PostgreSQL | Injected into solver objective function at planning time |
| Economies of scale | Shared solver infrastructure and codebase across all transport companies | Admmit mandate for multi-tenant architecture |
| SaaS provider | Admmit (Ressursplanlegger's developer/operator) | Hosts the platform for multiple transport companies |

## Forbehold og begrensninger

- **Domain gap:** The paper is written about generic SaaS architectural patterns using a meeting-planning application as the running example. It does not discuss transport planning, resource scheduling, or constraint programming. Every citation must bridge explicitly.
- **Configuration vs. weights:** The paper's customisation examples involve binary/choice options (logo, workflow type, high-availability), not continuous weight parameters or constraint programming objective functions. The claim that Ressursplanlegger's soft-constraint weights constitute "customer-driven variability" in Mietzner's sense is an application argument the thesis must make, not something the paper says directly.
- **Hard constraints:** The paper does not distinguish hard from soft constraints in the scheduling sense. Its "mandatory" VPs (must always be bound) are analogous to hard constraints in that they cannot be left unconfigured, but the analogy is loose. Do not over-extend.
- **Scale and complexity:** The paper's running example is a small meeting-planning workflow with 4–5 variation points. Ressursplanlegger's constraint model is substantially more complex. The applicability is conceptual, not quantitative.
- **Year:** 2009 paper. The SaaS/multi-tenancy landscape has evolved. However, the core variability-management conceptual framework (OVM, external/internal variability distinction) remains standard in the field and is still cited for these concepts.
- **Outline MUST CITE scope:** The outline marks this source only for §5.1.3 ¶3 ("configurable soft-constraint weights as the technical mechanism"). The paper does not speak to Tilpasningsdyktighet as a concept name, nor to its distinction from skalerbarhet — those arguments are the thesis's own contribution. The paper provides the architectural vocabulary to theorise the mechanism, not the concept itself.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Multi-tenant aware | "the software must appear to each tenant as if he was the sole tenant of the application (e.g., keeping confidential data private), while allowing multiple tenants to use the same instance of the application (in order to achieve economy of scale)" | p. 18 |
| Customer-driven Variability | "Different customers have different requirements to the application. These differences in requirements require that the SaaS applications are configurable to cater for the varying requirements." | p. 21 |
| Realization-driven Variability | "Alternatives for realizing the SaaS application introduce a further level of variation, which needs to be understood." | p. 21 |
| Variation point (VP) | "a variation point (VP) documents a variable item. A variant documents the possible instances of a variable item and is thus related to a VP." | p. 21 |
| External variability | "external variability is the variability that is communicated to the customer of the product line. In the SaaS context, the customer-driven variability nicely matches with this notion of external variability." | p. 21 |
| Internal variability | "internal variability is only visible to the developers of the product line. As such, this kind of variability clearly correlates with the realization-driven variability of a SaaS application." | p. 21 |

## Rammeverk og modeller

### Three SaaS deployment patterns (p. 19)

| Pattern | Description | Variability? |
|---|---|---|
| Single instance | All tenants share identical code and infrastructure; no per-tenant adaptation | No variability |
| Single configurable instance | All tenants share the same instance; adapted per-tenant at runtime via configuration metadata (config files, DB entries) | Customer-driven variability via metadata |
| Multiple instances | Each tenant has a separate deployed instance; maximum flexibility but no shared infrastructure | Full variability; loses economies of scale |

### OVM (Orthogonal Variability Model) key concepts (pp. 21–22)

| OVM Concept | Definition | Notes |
|---|---|---|
| Variation point (VP) | Documents a variable item | Can be optional or mandatory |
| Variant | Documents a possible instance of a VP | Can be optional or mandatory |
| Mandatory VP | Must always be bound — a variant must always be chosen | Analogous to a required configuration |
| Optional VP | Does not have to be bound | Can be left at default |
| Alternative choice | Aggregated optional variants with cardinality min..max | Constrains how many can be selected simultaneously |
| Exclude constraint | Mutual exclusion between a variant and a VP or another variant | Prevents incompatible combinations |
| Requires constraint | Implication: if variant A is chosen, variant B must also be chosen | Captures technical dependencies |

### Two categories of SaaS variability (p. 21)

| Category | Paper term | SaaS equivalent | Ressursplanlegger equivalent |
|---|---|---|---|
| External | Customer-driven variability | Functional/quality options the tenant chooses | Soft-constraint weights per company |
| Internal | Realization-driven variability | Deployment and infrastructure decisions | Solver-engine selection, DB isolation strategy |

## Key arguments / lines of reasoning

### Argument: Customization-vs-economy tension requires explicit variability management

- **Premiss 1:** SaaS providers must offer tenant-specific customisation to attract tenants.
- **Premiss 2:** SaaS providers must share infrastructure to achieve economies of scale.
- **Premiss 3:** These two goals are in tension — more customisation = less sharing.
- **Konklusjon:** Explicit variability models (OVM) resolve the tension by separating what tenants can configure (external) from what the provider controls internally (internal), enabling managed flexibility.
- **Sted:** (pp. 18, 21)
- **Hvilke claims dette støtter:** §5.1.3 ¶3 (why configurable weights are the right mechanism for Tilpasningsdyktighet in a multi-tenant SaaS)

### Argument: "Pre-planned" variability is a deliberate constraint, not a failure

- **Premiss 1:** Fully unlimited flexibility ("open world assumption") is unmanageable in SaaS.
- **Premiss 2:** Pre-planned variability restricts flexibility but makes it manageable.
- **Konklusjon:** "our approach provides a balance between offering (enough) flexibility and managing that flexibility."
- **Sted:** (p. 18)
- **Hvilke claims dette støtter:** §5.1.3 ¶3 honest acknowledgment that Ressursplanlegger's current weight space is bounded; §5.4 L12 (boundary cases described, not quantified)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| MeetR — meeting planning SaaS application | Running example used throughout; variation points: logo, title, workflow (short/long), data separation, high availability | pp. 21–23 |
| Salesforce.com / AppExchange | Industry example of SaaS with per-tenant configuration via metadata and tenant-extensible platform | p. 19 |
| Config 1 / Config 2 / Config 3 (Table 1) | Three different tenant configurations of MeetR showing how different binding choices produce different deployment outcomes | p. 23 |

## Data og statistikk

(Paper has no empirical data or statistics — it is a conceptual/architectural contribution with an illustrative example.)

## Forfatter-perspektiv / metodologi

Engineering paper from a software product line engineering background, applying established SPL techniques to the emergent SaaS context (2009). Approach is demonstrated via a running example (MeetR) rather than evaluated empirically. Authors are affiliated with University of Stuttgart and University of Duisburg-Essen. The paper was produced under the EU FP7 S-Cube project.

## Spot-check verification

1. Quote "SaaS providers are faced with two goals, which need to be balanced. Firstly, in order to attract enough customers, they need to cater for the varying requirements of potential tenants..." (p. 18) — verified via `pdftotext -f 1 -l 1` — **PASS**

2. Quote "Single configurable instance: In this pattern, all tenants use the same instance of the SaaS application (or parts thereof). However the instance is configurable on a per-tenant basis." (p. 19) — verified via `pdftotext -f 2 -l 2` — **PASS**

3. Quote "external variability is the variability that is communicated to the customer of the product line. In the SaaS context, the customer-driven variability nicely matches with this notion of external variability." (p. 21) — verified via `pdftotext -f 4 -l 4` — **PASS**

4. Quote "our approach provides a balance between offering (enough) flexibility and managing that flexibility." (p. 18) — verified via `pdftotext -f 1 -l 1` — **PASS** (line 97 in full-text extract)

**Result:** 4/4 quotes verified, 0 corrections made.

---

*Note on page numbering:* PDF page N = printed page N+17. All page references in this file use printed page numbers (18–25). Dual reference not needed as both systems are consistently offset by 17 throughout the 8-page paper.