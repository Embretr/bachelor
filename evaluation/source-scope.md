# Kildebehov — Bacheloroppgave Ressursplanlegger

> **Til Claude.ai:** Dette er en brief for å finne alle eksterne kilder oppgaven trenger. Dokumentet er selvstendig — du trenger ikke tilgang til noe repo. Returformat er spesifisert i §5.
>
> **Viktig om eksisterende kilder:** Det ligger allerede en liste med navngitte kilder i oppgavens referanseliste, men **ingen av dem er lest og validert**. De ble foreslått av en AI-assistent og skal behandles på linje med nye forslag — alt merket **[FORSLAG]** må verifiseres for eksistens, forfatter, år, publikasjonssted og fit mot claimet. Du står fritt til å foreslå bedre alternativer.
>
> **Din oppgave:**
> 1. For hvert tema i §3: vurder alle [FORSLAG]-kandidater, foreslå 1–3 beste kildene per behov, eventuelt erstatt med bedre
> 2. Verifiser alle kilder gjennom webresearch (ingen hallusinerte referanser)
> 3. Returner strukturert svar i formatet fra §5

---

## 1. Kontekst om oppgaven

**Tittel (arbeid):** Ressursplanlegger — Bacheloroppgave, Dataingeniør, NTNU IDI.

**Forskningsspørsmål (verbatim):**
> How can an algorithm-driven resource planning platform support traffic coordinators in Norwegian transport companies in assigning drivers and vehicles to assignments more efficiently than current manual processes?

**Tre delspørsmål:**
1. Hvilke nåværende praksiser, smertepunkter og behov har trafikkoordinatorer i norske transportselskap når de tildeler sjåfører og kjøretøy til oppdrag?
2. Hvordan bør et algoritmeassistert planleggingssystem utformes for å balansere automatisert optimalisering med operatørens behov for manuell kontroll og oversikt?
3. I hvilken grad adresserer det foreslåtte systemet de identifiserte behovene, og hva er begrensningene?

**Metodologi:** Design Science Research. Datainnsamling via 7 semi-strukturerte intervju med norske trafikkoordinatorer. Tematisk analyse. Valideres (ikke evalueres) gjennom kravsporing og algoritme-benchmarking.

**Artefaktet kort:**
- Webplattform: Next.js, TypeScript, PostgreSQL, Prisma, tRPC
- Multi-engine optimeringsalgoritme: custom greedy (Python), Google OR-Tools CP-SAT (Python), Timefold Solver (Java)
- Hard/soft constraint-modell (6 harde, 5 myke constraints)
- Human-in-the-loop: "suggest + override" med konfliktdeteksjon og score-breakdown

**Sensor-krav (NTNU/NRT A-nivå):**
- Holistisk ingeniørperspektiv (bærekraft, etikk, samfunnsnytte)
- Genuin teoretisk innsikt — primærkilder foretrekkes
- Kritisk refleksjon, ikke bare beskrivelse
- Hver kilde må direkte støtte påstanden den bærer

---

## 2. Kvalitetskrav til kilder

### Prioritert kildetype-hierarki

| Prioritet | Type | Egnet til |
|---|---|---|
| 1 | Peer-reviewed artikler i anerkjente tidsskrift/konferanser | Teoretiske påstander, metode-rasjonale, empirisk forskning |
| 2 | Autoritative lærebøker (Springer, MIT Press, Wiley, Elsevier, SIAM) | Etablerte begreper, fagfeltsoversikter |
| 3 | Offisiell teknisk dokumentasjon | **Kun** implementasjonsspesifikke tekniske claims |
| 4 | Rapporter fra etablerte organisasjoner (SSB, NHO, FN, EU, SINTEF, TØI) | Sektorkontekst, statistikk, politikk |
| 5 | Grå litteratur fra universitetsinstitusjoner | Kun som støtte, ikke bærende kilde |

### Unngå alltid
- Blogginnlegg, Medium, LinkedIn
- Wikipedia (kan brukes som navigasjon, aldri siteres)
- Generiske "intro to X"-ressurser
- Kilder uten tydelig forfatter, år eller publikasjonssted
- Markedsføringsmateriell fra programvareleverandører

### Tidshorisont
- Klassikere fra før 1990 kun hvis kanoniske (Dantzig & Ramser 1959, Brundtland 1987, Sheridan & Verplank 1978, Bainbridge 1983)
- For teknologi/automatisering: foretrukket innenfor siste 15 år
- For metodikk: klassisk pensum er akseptabelt

### Redaksjonelle regler for kildevalg
1. **Én bærende kilde per claim er bedre enn tre svake.**
2. **Primærkilde foretrekkes over sekundærkilde.** Hvis forfatter X refererer Y som opphav til begrep, siter Y.
3. **Kilden må direkte støtte claimet, ikke bare temaet.**
4. **Tilgjengelighet:** DOI/URL inkluderes der mulig. Åpne tilgjengelige kilder foretrekkes.
5. **Flag usikkerhet:** Hvis en kilde ikke kan verifiseres eller virker hallusinert, si det eksplisitt.

### Format for retur
- APA 7
- BibTeX-nøkkel: `førsteforfatter + år + kortord` (eksempel: `pinedo2016scheduling`)
- Full BibTeX-entry per kilde

---

## 3. Kildebehov per tema

Behovene er organisert i ti temaer (A–J). Hvert tema lister:
- **Claims som må støttes** (konkrete påstander som trenger kildebakking)
- **[FORSLAG]-kandidater** (både tidligere foreslåtte og nye — alle valideres)
- **Prioritet**

---

### Tema A — Scheduling, Constraint Programming, solvers

**Brukes i:** Ch 2.1 (Resource Scheduling), Ch 4.5 (Optimisation Algorithm), Ch 5.2 (Algorithm and Human Override).

**Claims som må støttes:**
1. Definisjon av resource scheduling som å tilordne begrensede ressurser til oppgaver over tid under begrensninger
2. Analogi til crew scheduling, nurse scheduling, driver scheduling (felles struktur)
3. Hard vs. soft constraints-skille i constraint-rammeverk (feasibility vs. scoring)
4. NP-hardness av ressurs-scheduling, og hvorfor dette motiverer heuristikk/metaheuristikk
5. Constraint Programming som paradigme (variabler, domener, constraints, objektiv)
6. CP-SAT-solvere — hva de gjør, hvordan de kombinerer CP og SAT
7. Metaheuristikker brukt i Timefold: tabu search, simulated annealing, late-acceptance hill climbing
8. Greedy heuristics for assignment-problemer
9. Multi-criteria / weighted-sum scoring i constraint optimization

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Pinedo, M. L. (2016). *Scheduling: Theory, Algorithms, and Systems* (5th ed.). Springer. — Bærende lærebok for scheduling
- **[FORSLAG]** Rossi, F., van Beek, P., & Walsh, T. (Eds.). (2006). *Handbook of Constraint Programming*. Elsevier. — Bærende for CP-teori
- **[FORSLAG]** Ernst, A. T., Jiang, H., Krishnamoorthy, M., & Sier, D. (2004). *Staff scheduling and rostering: A review of applications, methods and models*. European Journal of Operational Research, 153(1), 3–27. — Personnel scheduling-oversikt
- **[FORSLAG]** Van den Bergh, J., Beliën, J., De Bruecker, P., Demeulemeester, E., & De Boeck, L. (2013). *Personnel scheduling: A literature review*. EJOR, 226(3), 367–385.
- **[FORSLAG]** Gendreau, M., & Potvin, J.-Y. (Eds.). (2019). *Handbook of Metaheuristics* (3rd ed.). Springer. — Bærende for metaheuristikk-teori
- **[FORSLAG]** Perron, L., & Furnon, V. / Google OR-Tools. Offisiell OR-Tools-dokumentasjon eller tekniske whitepapers om CP-SAT. — Teknisk referanse
- **[FORSLAG]** Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman. — Hvis ren NP-referanse trengs

**Prioritet:** **Høy** — Ch 2.1 og 4.5 kan ikke skrives uten solid dekning.

---

### Tema B — Vehicle Routing Problem (nabo-teori)

**Brukes i:** Ch 2.1 ¶4 (posisjonering mot VRP — oppgavens problem har fast tid og sted, VRP sekvenserer).

**Claims som må støttes:**
1. VRP som kombinatorisk optimaliseringsproblem — opphav og grunnleggende formulering
2. Moderne VRP-variantoversikt (VRPTW, CVRP, heterogeneous fleet) for kontrast-posisjonering

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Dantzig, G. B., & Ramser, J. H. (1959). *The Truck Dispatching Problem*. Management Science, 6(1), 80–91. — Kanonisk opphav
- **[FORSLAG]** Toth, P., & Vigo, D. (Eds.). (2014). *Vehicle Routing: Problems, Methods, and Applications* (2nd ed.). SIAM. — Autoritativ lærebok
- **[FORSLAG]** Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). *The vehicle routing problem: State of the art classification and review*. Computers & Industrial Engineering, 99, 300–313. — Moderne oversikt
- **[FORSLAG]** Koç, Ç., Bektaş, T., Jabali, O., & Laporte, G. (2016). *Thirty years of heterogeneous vehicle routing*. EJOR, 249(1), 1–21.

**Prioritet:** **Medium** — VRP er ikke kjerneteori, bare kontrast. Minimum ett opphav + én moderne oversikt er tilstrekkelig.

---

### Tema C — Human-in-the-Loop, Trust, Automation

**Brukes i:** Ch 2.2 (HITL-teori), Ch 5.2 (algoritmeytelse og overstyring), Ch 5.3 (adopsjon og tillit), Ch 5.4 (tacit knowledge).

**Claims som må støttes:**
1. HITL-automatisering som designmønster (algoritme foreslår, menneske godkjenner)
2. Taxonomy av automatiseringsnivåer (klassisk 10-level scale)
3. Trust in automation, calibrated trust, appropriate reliance
4. Transparens/explainability i beslutningsstøttesystemer
5. Adoption-barrierer for teknologi i SMB-kontekst
6. Tacit knowledge og grensene for formalisering (Ch 5.4)
7. "Ironies of automation" — deskilling og automation-paradokset (Ch 5.5)
8. Moderne HCI-perspektiv på menneske-AI-samspill

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Sheridan, T. B., & Verplank, W. L. (1978). *Human and Computer Control of Undersea Teleoperators*. MIT Man-Machine Systems Laboratory, Technical Report. — Primærkilde for 10-level scale
- **[FORSLAG]** Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). *A Model for Types and Levels of Human Interaction with Automation*. IEEE Transactions on Systems, Man, and Cybernetics — Part A, 30(3), 286–297.
- **[FORSLAG]** Lee, J. D., & See, K. A. (2004). *Trust in Automation: Designing for Appropriate Reliance*. Human Factors, 46(1), 50–80.
- **[FORSLAG]** Hoff, K. A., & Bashir, M. (2015). *Trust in automation: Integrating empirical evidence on factors that influence trust*. Human Factors, 57(3), 407–434. — Moderne syntese
- **[FORSLAG]** Endsley, M. R. (2017). *From here to autonomy: Lessons learned from human-automation research*. Human Factors, 59(1), 5–27.
- **[FORSLAG]** Bainbridge, L. (1983). *Ironies of automation*. Automatica, 19(6), 775–779. — Klassiker for deskilling
- **[FORSLAG]** Shneiderman, B. (2020). *Human-centered artificial intelligence: Reliable, safe and trustworthy*. International Journal of Human-Computer Interaction, 36(6), 495–504.
- **[FORSLAG]** Amershi, S., Weld, D., Vorvoreanu, M., et al. (2019). *Guidelines for Human-AI Interaction*. Proceedings of CHI 2019. — Design-retningslinjer
- **[FORSLAG]** Nonaka, I., & Takeuchi, H. (1995). *The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation*. Oxford University Press. — Klassiker om tacit knowledge
- **[FORSLAG]** Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). *User acceptance of information technology: Toward a unified view (UTAUT)*. MIS Quarterly, 27(3), 425–478.

**Prioritet:** **Høy** — Ch 2.2 er kjernekapittel; Ch 5.3 og 5.4 bygger videre.

---

### Tema D — Transport Management Systems (TMS)

**Brukes i:** Ch 2.3 (TMS-landskapet), Ch 4.3 (fit/gap), Ch 5.3 (adopsjon, integrasjon).

**Claims som må støttes:**
1. TMS som programvarekategori — hva det typisk dekker (ordre, ruteplanlegging, fraktadmin, fakturering)
2. Skille mellom TMS (transaksjons-/fakturafokus) og optimering/beslutningsstøtte (planleggingsfokus)
3. Logistikk-software i SMB-kontekst — generelle mønstre
4. Digitalisering av godstransport som bredere trend

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Ghiani, G., Laporte, G., & Musmanno, R. (2013). *Introduction to Logistics Systems Management* (2nd ed.). Wiley. — Lærebok med TMS-kapittel
- **[FORSLAG]** Crainic, T. G., & Laporte, G. (1997). *Planning models for freight transportation*. EJOR, 97(3), 409–438. — Klassiker for fraktplanlegging
- **[FORSLAG]** Hesse, M., & Rodrigue, J.-P. (2004). *The transport geography of logistics and freight distribution*. Journal of Transport Geography, 12(3), 171–184.
- **[FORSLAG]** Spesiell forespørsel til Claude.ai: søk etter nyere peer-reviewed review om TMS/digitale plattformer i logistikk (siste 10 år), i tidsskrifter som Transportation Research Part E, Computers & Industrial Engineering, International Journal of Production Economics.
- **[FORSLAG]** Gartner Magic Quadrant for Transportation Management Systems (nyeste versjon). — Bransjerapport, merk som industrikilde ikke peer-reviewed.

**Prioritet:** **Høy** — Dette er oppgavens svakeste område fagmessig og må styrkes.

---

### Tema E — Norsk transport- og logistikkontekst

**Brukes i:** Ch 1.1 (bakgrunn og motivasjon), Ch 2.3 ¶2 (hvorfor manuell planlegging dominerer i Norge).

**Claims som må støttes:**
1. Norsk transportsektor: størrelse, antall bedrifter, antall sjåfører, omsetning
2. Digitaliseringsgrad i norsk logistikk/transport
3. SMB-dominans og fragmentering i bransjen
4. Hvorfor manuell planlegging fortsatt er utbredt
5. Aktuelle bransjeutfordringer (sjåførmangel, arbeidsforhold, kostnadspress)

**[FORSLAG]-kandidater (valideres, alle er nye):**
- **[FORSLAG]** Statistisk sentralbyrå (SSB). *Godstransport på veg* (årlig statistikkpublikasjon). Hentes fra ssb.no, nyeste tilgjengelige utgave.
- **[FORSLAG]** Statistisk sentralbyrå (SSB). *Strukturstatistikk for transport og lagring*. ssb.no.
- **[FORSLAG]** NHO Logistikk og Transport. *Konjunkturrapport* eller årsrapport (siste tilgjengelige år).
- **[FORSLAG]** Menon Economics. Rapporter om transportsektoren. menon.no.
- **[FORSLAG]** Transportøkonomisk institutt (TØI). Rapporter om godstransport og digitalisering. toi.no.
- **[FORSLAG]** SINTEF. Rapporter om digitalisering i transport/logistikk. sintef.no.
- **[FORSLAG]** Statens vegvesen / Vegdirektoratet. Rapporter om godstransport.

**Til Claude.ai spesielt:** Ferske rapporter (2022–2025) foretrekkes. Konkrete tall — antall bedrifter, antall sjåfører, omsetning, digitaliseringsgrad — er det mest verdifulle. Oppgi direkte lenker til nedlastbare PDF-er.

**Prioritet:** **Høy** — Sensor er streng på "holistisk systemperspektiv"; norsk kontekst må forankres i data.

---

### Tema F — Design Science Research

**Brukes i:** Ch 2.4 (DSR-teori), Ch 3.1 (DSR-anvendelse), Ch 5.6 (validering vs. evaluering).

**Claims som må støttes:**
1. DSR som forskningsparadigme — skillet mellom behavioral science og design science
2. Peffers' seks-fase prosess-modell
3. Hevners tre-syklus rammeverk (hvis brukt)
4. Validering vs. evaluering — Wieringas skille

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). *Design Science in Information Systems Research*. MIS Quarterly, 28(1), 75–105. — Bærende
- **[FORSLAG]** Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems, 24(3), 45–77. — Bærende
- **[FORSLAG]** Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer. — For validering/evalueringsskille
- **[FORSLAG]** Hevner, A. R. (2007). *A Three Cycle View of Design Science Research*. Scandinavian Journal of Information Systems, 19(2), 87–92.
- **[FORSLAG]** Gregor, S., & Hevner, A. R. (2013). *Positioning and presenting design science research for maximum impact*. MIS Quarterly, 37(2), 337–355. — For DSR-presentasjon

**Prioritet:** **Medium-høy** — Peffers + Hevner 2004 + Wieringa er minimum; andre er styrkning.

---

### Tema G — Kvalitative metoder

**Brukes i:** Ch 3.2 (Data Collection), Ch 3.3 (Data Analysis), Ch 3.5 (Validity).

**Claims som må støttes:**
1. Semi-strukturerte intervju som metode — formål og styrker
2. Purposive sampling som utvalgsmetode
3. Forskningsetikk i kvalitative intervju (informert samtykke, anonymisering, datalagring)
4. Tematisk analyse som metode (seks faser)
5. Validitet/reliabilitet-kriterier i kvalitativ forskning
6. Trustworthiness-rammeverket (valgfritt tillegg)

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Braun, V., & Clarke, V. (2006). *Using Thematic Analysis in Psychology*. Qualitative Research in Psychology, 3(2), 77–101. — Bærende for tematisk analyse
- **[FORSLAG]** Malterud, K. (2003). *Kvalitative metoder i medisinsk forskning* (2. utg.). Universitetsforlaget. — Validitet-kriterier
- **[FORSLAG]** Oates, B. J., Griffiths, M., & McLean, R. (2022). *Researching Information Systems and Computing*. SAGE. — IS-metodelærebok
- **[FORSLAG]** Kvale, S., & Brinkmann, S. (2015/2017). *Det kvalitative forskningsintervju* (3. utg.). Gyldendal. — Norsk kanonisk intervjuverk, sterkt ønsket i NTNU-kontekst
- **[FORSLAG]** Tjora, A. (2021). *Kvalitative forskningsmetoder i praksis* (4. utg.). Gyldendal. — Nyere norsk alternativ
- **[FORSLAG]** Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic Inquiry*. SAGE. — Trustworthiness, valgfritt

**Prioritet:** **Høy** — Braun & Clarke + én norsk metodekilde (Kvale & Brinkmann eller Tjora) er minimum.

---

### Tema H — Agile og iterativ utvikling

**Brukes i:** Ch 3.4 (System Development Process).

**Claims som må støttes:**
1. Iterativ/inkrementell utvikling som metodologisk begrep — ikke formelt Scrum, men strukturert iterasjon
2. Krav-evolusjon i iterative prosjekter
3. Agile prinsipper (ikke ceremonies)

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Larman, C., & Basili, V. R. (2003). *Iterative and incremental developments: A brief history*. IEEE Computer, 36(6), 47–56. — Kanonisk akademisk kilde
- **[FORSLAG]** Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson. — Lærebok-dekning
- **[FORSLAG]** Cockburn, A. (2002). *Agile Software Development: The Cooperative Game*. Addison-Wesley.
- **[FORSLAG]** Beck, K., et al. (2001). *Manifesto for Agile Software Development*. agilemanifesto.org. — Primærkilde for prinsipper, ikke akademisk

**Prioritet:** **Høy** — Minst én akademisk kilde (Larman & Basili eller Sommerville) trengs for Ch 3.4.

---

### Tema I — Bærekraft (SusAF, SDG, Karlskrona)

**Brukes i:** Ch 5.5 (Sustainability and Ethical Considerations).

**Claims som må støttes:**
1. Brundtlands bærekraftsdefinisjon
2. UNs 2030 Agenda og Sustainable Development Goals
3. Karlskrona Manifesto — fem dimensjoner av bærekraft i programvare
4. SusAF (Sustainability Awareness Framework) — analyseverktøy
5. Tre-ordens effekter: immediate / enabling / structural
6. Mapping mellom SusAF-effekter og SDG-er

**[FORSLAG]-kandidater (valideres):**
- **[FORSLAG]** Brundtland, G. H. (1987). *Our Common Future*. WCED, United Nations. — Fundamentdefinisjon
- **[FORSLAG]** United Nations General Assembly. (2015). *Transforming Our World: The 2030 Agenda for Sustainable Development*. A/RES/70/1.
- **[FORSLAG]** Becker, C., Chitchyan, R., Duboc, L., et al. (2015). *The Karlskrona Manifesto for Sustainability Design*. arXiv:1410.6968.
- **[FORSLAG]** Duboc, L., Penzenstadler, B., Porras, J., et al. (2020). *Do We Really Know What We Are Building? Raising Awareness of Potential Sustainability Effects of Software Systems in Requirements Engineering*. Journal of Systems and Software, 165, 110570. — SusAF-kilde
- **[FORSLAG]** Seyff, N., Betz, S., Lammert, D., et al. (2022). *Transforming Our World through Software: Mapping the Sustainability Awareness Framework to the UN Sustainable Development Goals*. Proceedings of ENASE 2022, 417–425.
- **[FORSLAG]** Hilty, L. M., Arnfalk, P., Erdmann, L., Goodman, J., Lehmann, M., & Wäger, P. A. (2006). *The relevance of information and communication technologies for environmental sustainability — A prospective simulation study*. Environmental Modelling & Software, 21(11), 1618–1629. — Mulig primærkilde for immediate/enabling/structural effect-klassifiseringen
- **[FORSLAG]** Penzenstadler, B., Femmer, H., & Richardson, D. (2013). *Who is the advocate? Stakeholders for sustainability*. GREENS 2013. — Valgfritt utvidelse

**Til Claude.ai spesielt:** For punkt 5 (tre-ordens effekter) — det er usikkert om Hilty et al. 2006 er nøyaktig primærkilde. Søk etter den kanoniske kilden for klassifiseringen "first-order / second-order / third-order" eller "immediate / enabling / structural" effekter av IT på bærekraft. Kandidater kan også være Berkhout & Hertin (2001) eller Hilty & Aebischer (2015).

**Prioritet:** **Medium-høy** — Grunnsettet (Brundtland, UN, Duboc, Karlskrona) er tilstrekkelig for Ch 5.5; resten er styrkning.

---

### Tema J — Algoritmisk etikk

**Brukes i:** Ch 5.5 ¶5 (Ethical Perspective).

**Claims som må støttes:**
1. Algoritmisk rettferdighet — hvordan algoritmer kan systematisk favorisere eller diskriminere
2. Accountability for algoritmebeslutninger
3. Personvern og datahåndtering i systemer som lagrer persondata
4. Rammeverk for AI-etikk

**[FORSLAG]-kandidater (valideres, alle er nye):**
- **[FORSLAG]** Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016). *The ethics of algorithms: Mapping the debate*. Big Data & Society, 3(2), 1–21. — Fundamentkilde
- **[FORSLAG]** Floridi, L., Cowls, J., Beltrametti, M., et al. (2018). *AI4People — An ethical framework for a good AI society: Opportunities, risks, principles, and recommendations*. Minds and Machines, 28, 689–707.
- **[FORSLAG]** Jobin, A., Ienca, M., & Vayena, E. (2019). *The global landscape of AI ethics guidelines*. Nature Machine Intelligence, 1, 389–399.
- **[FORSLAG]** EU Commission. (2021/2024). *Artificial Intelligence Act*. — Offisielt regulatorisk rammeverk
- **[FORSLAG]** Martin, K. (2019). *Ethical implications and accountability of algorithms*. Journal of Business Ethics, 160, 835–850.

**Prioritet:** **Høy** — Ingen etikk-kilde finnes i foreslått referanse i dag; Ch 5.5 ¶5 kan ikke skrives uten fundament.

---

## 4. Prioritert oversikt

Hvis Claude.ai må rangere arbeidet, her er rekkefølgen:

### Absolutt nødvendig (blokkerer A-karakter hvis mangler eller svakt)
- **Tema D — TMS:** Pr. i dag er Ch 2.3 uten akademisk fundament. Må fylles.
- **Tema E — Norsk transportkontekst:** Sensor forventer norsk dataforankring i Ch 1.1.
- **Tema H — Iterativ utvikling:** Trenger akademisk kilde utover Agile Manifesto.
- **Tema J — Algoritmisk etikk:** Ch 5.5 ¶5 krever fundament.
- **Tema A — Scheduling/CP/solvers:** Sterkt fundament nødvendig for Ch 2.1 og 4.5.
- **Tema C — HITL/Trust:** Kjerne for Ch 2.2, 5.3, 5.4.
- **Tema G — Kvalitative metoder:** Minst Braun & Clarke + én norsk metodekilde.

### Sterkt anbefalt (styrker teoretisk innsikt)
- **Tema F — DSR:** Peffers + Hevner 2004 + Wieringa som minimum.
- **Tema I — Bærekraft:** Grunnsettet pluss klargjøring av effect-klassifisering.

### Valgfritt / polering
- **Tema B — VRP:** Bare nabo-teori, ett opphav + én oversikt er nok.

---

## 5. Returformat

Returner én samlet respons strukturert per tema:

```md
## Tema [bokstav] — [tittel]

### Validerte kandidater

#### [bibtex-nøkkel]
- **Full sitering (APA 7):** ...
- **DOI/URL:** ...
- **Kildetype:** peer-reviewed / lærebok / rapport / dokumentasjon
- **Dekker claim(s):** [konkret: hvilke påstander fra temabeskrivelsen]
- **Autoritet/kvalitet:** [tidsskriftsrang, forlag, sitater, forfatters posisjon]
- **Tilgjengelighet:** åpen / bak betalingsmur / NTNU Oria
- **BibTeX:**
  ```bibtex
  @article{key2020name,
    author  = {...},
    title   = {...},
    ...
  }
  ```

#### [neste kandidat]
...

### Avviste forslag

**[FORSLAG] X ble ikke tatt med fordi:** [kort begrunnelse — f.eks. ikke verifisert, for snever, finnes bedre alternativ, utdatert]

### Oversett gap
[Hvis du finner en kildetype eller et behov jeg har oversett, flagg det her.]

### Anbefaling
[Kort: hvilke 1–3 kandidater per behov er best; hvilke komplementerer hverandre.]
```

### Spesielle krav til svaret

- **Ikke hallusiner.** Hvis en kilde ikke kan verifiseres via webresearch, si det eksplisitt.
- **Verifiser alle [FORSLAG].** Flag de som ikke finnes, har feil forfatter/år, eller er feilsitert.
- **Vær rask på klare valg.** Hvis Peffers 2007 er riktig for Peffers-claimet, si bare det — ikke lag omfattende alternativanalyse.
- **Legg vekt på tema D, E, H, J.** Dette er områder uten sterke kandidater; bruk mest tid her.
- **Norske rapporter (Tema E):** Gi direkte lenker til nedlastbare PDF-er der mulig.

---

## Slutt

Kontaktpunkt: Hvis noe er uklart, flagg det i svaret i stedet for å gjette.

Last brief update: 2026-04-22.