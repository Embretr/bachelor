# Data-Driven Forwarding: A Typology of Digital Platforms for Road Freight Transport Management (`heinbach2022datadriven`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The article is fully read (abstract, introduction, domain background, research design, findings, discussion, conclusion). All three areas of interest (Ch 2.3) were investigated. The TMS definition, RFTM activity framework, and DP typology are fully captured. Limitations and inapplicability to our case are documented.
  - **Gaps not investigated:** Appendix 2 (expert profiles table) — not relevant to the claims this thesis needs.

## Source metadata
- **BibTeX key:** `heinbach2022datadriven`
- **Reference (APA 7):** Heinbach, C., Beinke, J., Kammler, F., & Thomas, O. (2022). Data-driven forwarding: A typology of digital platforms for road freight transport management. *Electronic Markets*, *32*, 807–828. https://doi.org/10.1007/s12525-022-00540-4
- **Tilgang:** open access (PDF)
- **Raw source:** `../heinbach2022datadriven.pdf`
- **Coverage in raw:** Full article, pp. 807–828. All sections present: abstract, introduction, domain background (digital platforms in freight logistics, TMS and RFTM activities), research design (grounded theory, expert interviews), findings (DP characteristics, typology of 8 DP types), discussion and implications, conclusions. No missing sections.

## Sammendrag (2–3 setninger)

Heinbach et al. (2022) explore digital platforms (DPs) for road freight transport management (RFTM) and develop a typology of eight DP types organised into four main categories (freight order coordination, freight resource handling, transport data connectivity, transport process support), grounded in expert interviews with 11 platform providers in the European market. The study uses the core process of transport management systems (TMSs) as its analytical frame, defining TMSs as software dealing with the planning and execution of the physical movement of goods across supply chains. Its main contribution to our thesis is a well-supported definition of TMS as a software category and a structured characterisation of what TMS applications do — providing the theoretical grounding for Ch 2.3's description of TMS and the planning gap Ressursplanlegger addresses.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.3 ¶1 (TMS definition and category) | Covered: explicit TMS definition cited from De Muynck et al. (2020) + source's own characterisation of TMS activities |
| Ch 2.3 ¶2 (TMS landscape — what TMS does well) | Partial: source describes TMS activities at general level (planning, execution, tracking, billing); no coverage of specific Norwegian vendors (Timpex, Trimtex, Opptur) |
| Ch 2.3 ¶3 (planning gap) | Partial: source identifies that DPs enrich TMS by covering operational processes TMS does not fully address; planning gap is implicit in the framework but not the paper's focus |
| Ch 1.5 (digital transformation in logistics) | Covered: source describes ongoing digitisation pressure in European road freight; useful scene-setting |
| Ch 5.3 (adoption barriers / digital transformation context) | Outside scope: source focuses on platform providers, not adoption by end-user transport companies |

## Claims this source supports

### Claim 1: TMS is defined as the category of software dealing with the planning and execution of the physical movement of goods across supply chains

- **Suggested for:** Ch 2.3 ¶1 (primary)
- **Direkte sitat:** "TMSs generically refer to the category of software that deals with the planning and execution of the physical movement of goods across supply chains." (p. 811)
- **Parafrase:** The source, citing De Muynck et al. (2020, p. 1), defines transport management systems as the class of software whose core function is to plan and execute how physical goods move through supply chains.
- **Forbehold:** This definition is cited by Heinbach et al. from a Gartner source (De Muynck et al., 2020). It is therefore a practitioner-origin definition adopted in an academic context. Page 811 is confirmed (line 405 in extracted text; page marker "811" at line 350, before the definition; page "812" appears at line 423, after the definition).
- **Anvendelse på vårt case:** In Ch 2.3 ¶1, this definition establishes that Ressursplanlegger — a platform for planning and executing driver/vehicle assignments — operates squarely within the TMS category as defined here, while existing Norwegian tools (Timpex, Trimtex) address the same category but with different feature coverage.

---

### Claim 2: TMSs have their origin in freight forwarder software to manage complex transport operations by assigning customer shipments to fleet resources

- **Suggested for:** Ch 2.3 ¶1 (secondary); Ch 2.3 ¶2
- **Direkte sitat:** "TMSs have their origin within the scope of freight forwarder software to manage complex transport operations by assigning customer shipments to fleet resources in the trucking business." (p. 811)
- **Parafrase:** The source traces TMS origins to the need to allocate customer shipments to carrier fleet resources — a matching/assignment function at the core of TMS.
- **Forbehold:** "Assigning customer shipments to fleet resources" is the classical TMS function; Ressursplanlegger specifically handles the intra-company assignment of drivers and vehicles, which is one level below the freight-forwarder-to-carrier matching the source describes.
- **Anvendelse på vårt case:** This historical framing is useful in Ch 2.3 ¶1 to establish that the assignment of jobs to transport resources is the foundational function of TMS software — directly analogous to what Ressursplanlegger does, except at the internal coordinator-to-driver/vehicle level rather than the forwarder-to-carrier level.

---

### Claim 3: TMSs address core business activities on a shipment level while digital platforms enrich operational processes for inbound/outbound logistics

- **Suggested for:** Ch 2.3 ¶1; Ch 2.3 ¶3 (the planning-gap bridge)
- **Direkte sitat:** "In essence, TMSs address the core business activities for freight transportation on a shipment level, while DPs enrich the operational processes particularly for inbound and outbound logistics." (p. 808)
- **Parafrase:** The paper characterises TMS as shipment-level and DPs as enriching operational processes beyond that core — indicating that TMS products leave gaps that external tools fill.
- **Forbehold:** "Inbound and outbound logistics" enrichment refers to digital platform services (visibility, optimisation, analytics) layered on top of TMS, not to internal planning tools like Ressursplanlegger. The "enrichment" gap the source describes is different from the planning gap Ressursplanlegger fills, but the structural logic (TMS has a core scope; operational processes beyond that scope need supplemental tools) is transferable.
- **Anvendelse på vårt case:** In Ch 2.3 ¶3, this framing supports the argument that TMS products have a defined scope — and that internal daily resource planning (assigning drivers and vehicles) falls outside that scope, exactly where Ressursplanlegger positions itself.

---

### Claim 4: Road freight transport management encompasses three stages — transport procurement and decision, transport service handling, and assisting functions — with ten activities

- **Suggested for:** Ch 2.3 ¶1 (background framing of what TMS covers)
- **Direkte sitat:** "Figure 1 summarizes three transport management stages encompassing 10 activities for RFTM that we have identified for the analysis of DPs related to our topic." (p. 812)
- **Note on page:** Line 426 in extracted text confirms "Figure 1 summarizes..." is on page 812 (marker at line 423).
- **Parafrase:** The source structures RFTM into: (1) procurement/contracting, (2) service handling (booking, execution, monitoring, billing), and (3) assisting functions (service support, reporting, quality/compliance).
- **Forbehold:** This framework is derived from Gartner's Magic Quadrant for TMS and the source's own grounded theory analysis, making it a practical industry model rather than a formal academic theory. The framework was designed for the B2B freight market (heavy trucks, Euro-pallets, freight forwarders), not for the internal daily dispatch operations of Norwegian transport companies.
- **Anvendelse på vårt case:** The three-stage RFTM framework helps in Ch 2.3 ¶1 to show that TMS products primarily support stages 1 and 2 at the shipment/booking level; the specific sub-activity of "transport execution — truck dispatching" in stage 2 is the gap Ressursplanlegger addresses through algorithm-driven driver/vehicle assignment.

---

### Claim 5: A typology of eight digital platform types exists for RFTM, organised into four main categories

- **Suggested for:** Ch 2.3 ¶1 (optional background on digital transport ecosystem)
- **Direkte sitat:** "From the analysis of the data, we conceptualized eight types of DPs and further clustered them into four main categories according to the scope of platform-enabled service offerings to support digital RFTM we have explored. These main categories are freight order coordination, freight resource handling, transport data connectivity, and transport process support." (p. 817)
- **Parafrase:** The paper identifies FPP, DFF, DFE, TOI, TSI, TWP, YMP, and TCP as the eight DP types, each supporting specific activities within RFTM.
- **Forbehold:** This typology was built for platform providers selling services in the open freight market — it does not classify internal TMS or planning tools. Ressursplanlegger does not fit neatly into any of these eight types; it is an internal planning tool, not a multi-sided platform.
- **Anvendelse på vårt case:** Low direct utility in thesis writing; primarily confirms that Ressursplanlegger occupies a distinct niche (internal algorithmic planning) not covered by any existing DP type in the typology. This supports Ch 2.3 ¶3's argument that no existing digital platform category covers the internal dispatcher–resource assignment function.

---

### Claim 6: Digital platforms offer three service dimensions — visibility, optimisation, and analytics — as the key value propositions for transport management

- **Suggested for:** Ch 2.3 ¶1–¶3 (background on what digital transport tools offer)
- **Direkte sitat:** "our study abstracts from these rather technical cloud service capabilities by the service dimensions of visibility, optimization, and analytics and their assignments to RFTM." (p. 822)
- **Parafrase:** The source categorises digital transport services into three value types: visibility (tracking, real-time information), optimisation (route planning, asset utilisation, invoicing), and analytics (AI-based performance measurement).
- **Forbehold:** The source frames these dimensions from the platform provider perspective, not the internal transport company perspective. Ressursplanlegger's algorithm-driven assignment is described in the source's vocabulary as an "optimisation service," but only in the context of open-market platforms, not internal dispatch tools.
- **Anvendelse på vårt case:** In Ch 2.3 ¶3, the optimisation dimension can be referenced to note that even in the broader DP ecosystem, optimisation services target route planning and asset utilisation — not the upstream driver/vehicle assignment step that Ressursplanlegger handles. This sharpens the planning gap argument.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Transport management system (TMS) | TMS / planleggingsverktøy | Direkte ekvivalent; Heinbach bruker "TMS" som kategori, vi bruker det om Timpex, Trimtex, Opptur |
| Road freight transport management (RFTM) | Ressursplanlegging i transportsektor | Bredere enn vår case: RFTM dekker B2B-fraktmarkedet; vår case er intern daglig sjåfør-/kjøretøytildeling |
| Fleet resources | Sjåfører og kjøretøy | Kilden bruker "fleet resources" for carrier-eide lastebiler; vi bruker det for sjåfør+kjøretøy-kombinasjoner hos transportselskapet |
| Transport execution / truck dispatching | Sjåfør-/kjøretøytildeling | Direkte ekvivalent for vår case (sub-aktivitet under RFTM stage 2) |
| Freight dispatcher | Trafikkoordinator | Kilden bruker "freight dispatcher" for personen som sender lastebiler; vår term er "trafikkoordinator" |
| Shipper | Oppdragsgiver / kunde | I kilden: selskapet som eier godset; ikke direkte ekvivalent i vår case (vi har oppdrag, ikke gods) |
| Carrier | Transportselskapet | I kilden: selskapet som eier og kjører lastebilene; tilsvarer transportselskapet som bruker Ressursplanlegger |
| Shipment | Oppdrag | Kilden bruker "shipment" for en godsforsendelse; vi bruker "oppdrag" for en transportjobb som tildeles sjåfør/kjøretøy |
| Digital platform (DP) | Ikke direkte ekvivalent | Ressursplanlegger er ikke en multi-sided DP i kildens forstand; det er et internt planleggingssystem |
| Optimization service | Optimeringsalgoritme / planleggingsstøtte | Kilden bruker dette om platform-tjenester for rute- og kapasitetsoptimering; vi bruker det om vår intern CP-SAT/Timefold-algoritme |

## Forbehold og begrensninger

- **Domeneavstand:** Heinbach et al. skriver om B2B-fraktmarkedet med freight forwarders, shippers, og carriers som distinkte aktører. Ressursplanlegger handler om intern daglig planlegging *innad* i ett transportselskap — mellom trafikkoordinatoren og selskapets egne sjåfører og kjøretøy. Kildens rammeverk beskriver markedsplasser og plattformer som medierer mellom separate juridiske enheter, ikke interne planleggingsverktøy.

- **TMS-definisjonen er lånt, ikke primær:** Heinbach et al. siterer TMS-definisjonen fra De Muynck et al. (2020, Gartner). Hvis primærkilden er tilgjengelig, bør den siteres direkte. Heinbach er akseptabel sekundærkilde for definisjonen, men dette bør noteres.

- **Norsk kontekst ikke dekket:** Kilden er begrenset til det europeiske markedet, med tyske og europeiske aktører. Norske TMS-er (Timpex, Trimtex, Opptur) er ikke nevnt. Kilden kan ikke brukes som kilde for påstander om norske verktøy.

- **Planleggingsgapet er implisitt, ikke eksplisitt:** Kilden konstaterer at DPs utfyller TMS, men analyserer ikke det spesifikke gapet mellom "oppdrag eksisterer" og "sjåfør er tildelt." Ressursplanleggers posisjonering i dette gapet kan støttes av kildens rammeverk, men krever at writer-agent trekker en eksplisitt slutning kilden selv ikke gjør.

- **Typologien (8 DP-typer) er ikke direkte relevant:** Ressursplanlegger passer ikke inn i noen av de åtte DP-typene. Typologien er nyttig som bakgrunn, men bør ikke siteres i en sammenheng der det kan fremstå som om Ressursplanlegger er en av disse typene.

- **Grounded theory fra 11 ekspertintervjuer (2020):** Funnene er basert på et begrenset utvalg europeiske plattformleverandører i 2020. Markedet har sannsynligvis endret seg siden da. Bruk kilden for den strukturelle TMS-beskrivelsen, ikke for spesifikke markedsdata.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Transport management system (TMS) | "TMSs generically refer to the category of software that deals with the planning and execution of the physical movement of goods across supply chains." | p. 811 (sitert fra De Muynck et al., 2020, p. 1) |
| Road freight transport management (RFTM) | Implisitt definert via tre stadier: "transport procurement and decision (e.g., purchasing of load capacities), transport service handling (e.g., transport order handling), and assisting functions (e.g., quality assurance)." | p. 817 |

## Rammeverk og modeller

### RFTM Activity Framework — tre transport management-stadier med 10 aktiviteter (s. 812)

| Stadium | Aktiviteter | Side |
|---|---|---|
| Transport procurement and decision | Tender/contracting, spot pricing | p. 812 |
| Transport service handling | Booking/transport order, transport execution (truck dispatching), monitoring (tracking and tracing), documentation and billing | p. 812 |
| Assisting functions | Service support, reporting and controlling, quality and compliance management | p. 812 |

**Merk:** "Transport execution — truck dispatching" under stadium 2 er den aktiviteten som direkte korresponderer med det Ressursplanlegger utfører (tildele sjåfør og kjøretøy til oppdrag). Eksisterende TMS-er er svake på dette steget, noe kildens rammeverk impliserer ved at det er adressert av DPs og ikke av kjerne-TMS.

### DP Typology — åtte plattformtyper for RFTM (s. 817–820)

| DP Type | Kategori | Kjernetjeneste | Side |
|---|---|---|---|
| Freight Procurement Provider (FPP) | Freight order coordination | Tender contracts, spot pricing | p. 819 (Table 4) |
| Digital Freight Forwarder (DFF) | Freight order coordination | Order processing, freight brokerage | p. 819 (Table 4) |
| Digital Freight Exchange (DFE) | Freight resource handling | Matching freight capacities and loads | p. 819 (Table 4) |
| Transport Order Integrator (TOI) | Transport data connectivity | Order data aggregation, tracking/tracing | p. 819 (Table 4) |
| Transport System Integrator (TSI) | Transport data connectivity | Telematics + TMS data aggregation | p. 819 (Table 4) |
| Transport Workflow Provider (TWP) | Transport process support | End-to-end visibility, order workflow, driver communication | p. 819 (Table 4) |
| Yard Management Provider (YMP) | Transport process support | ETA-based gate management, resource allocation | p. 819 (Table 4) |
| Transport Compliance Provider (TCP) | Transport process support | Legal compliance monitoring | p. 819 (Table 4) |

## Key arguments / lines of reasoning

### Argument: TMS forms the analytical backbone for digital platform services in road freight

- **Premiss(er):** TMS products define the core business process of freight transport (planning, execution, billing). Digital platforms extend or enrich these activities but follow the same process logic.
- **Konklusjon:** Understanding TMS activities provides the canonical framework for classifying what digital transport tools do.
- **Sted:** (p. 811–812)
- **Hvilke claims dette støtter:** Ch 2.3 ¶1 — introduces TMS as a software category grounded in this process logic.

---

### Argument: Data availability enables advanced optimisation and analytics services in digital transport management

- **Premiss(er):** Platforms that obtain operational data from shippers and carriers can deploy AI-based routing, intelligent matching algorithms, and ETA prediction.
- **Konklusjon:** "Access to operational road freight data appears to be an enabler for DPs to provide advanced data-driven services for RFTM, while market maturity is key for successful service innovations." (p. 821)
- **Sted:** (p. 821)
- **Hvilke claims dette støtter:** Ch 2.3 ¶3 (implicit context for why data-driven planning tools are a natural evolution); Ch 5.3 (adoption context).

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Timocom (digital freight exchange) | Established DFE-type platform that has added analysis and optimisation services over time; illustrates digital maturity progression | p. 820 |
| TRUCKAHEAD (transport workflow provider) | Uses mobile app to improve dispatcher–driver communication and automate checklists; closest to Ressursplanlegger's operational domain | p. 819 |
| MOVINGSTAR (transport system integrator) | Aggregates telematics data across mixed fleets for harmonised fleet management — shows TSI type | p. 820 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 11 expert interviews | Platform provider organisations | 2020, European market | p. 813 |
| European logistics sector annual turnover | 1120 billion EUR | 2019 | p. 808 |
| Several hundreds of thousands of carriers | Road carriers in regional European markets | ~2021 | p. 811 |

## Forfatter-perspektiv / metodologi

Grounded theory methodology with in-depth expert interviews of 11 digital platform organisations in the European road freight market (data collected July–October 2020). The study takes a supply-side perspective (platform providers as informants), not an end-user or transport company perspective. This limits the source's relevance for claims about how transport companies experience or adopt systems — that angle belongs to our own interview data.