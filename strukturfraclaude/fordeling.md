# Oppgavefordeling – Kontekstfase (før rapportskriving)

> Mål: få alle kontekstfiler på plass i GitHub slik at AI kan brukes effektivt til rapportskriving.
> Siden rapporten ikke er startet og dere er like sterke på skriving, fordeles kontekstfilene
> etter kunnskap – ikke etter hvem som skal skrive hva i rapporten.

---

## 👨‍💻 Embret – teknisk kontekst

Disse filene kan bare Embret skrive raskt og presist. Ikke deleger til Mikael.

### Prioritet 1 – må være på plass først (blokkerer Mikael)
| Fil | Hva som skal inn | Estimert tid |
|-----|-----------------|:------------:|
| `tech/algoritme.md` | Input, output, constraints, metode, begrensninger, målfunksjon | 2–3t |
| `tech/arkitektur.md` | Frontend, backend, database, deploy, kommunikasjon mellom lag | 1–2t |
| `tech/datamodell.md` | Alle entiteter med felter, typer og relasjoner | 1–2t |

### Prioritet 2 – viktig, men blokkerer ikke Mikael
| Fil | Hva som skal inn | Estimert tid |
|-----|-----------------|:------------:|
| `tech/api_oversikt.md` | Alle endepunkter, metode, request/response | 1t |
| `tech/kodebase_oppsummering.md` | Mappestruktur, viktige filer, eksterne biblioteker | 1t |
| `tech/tech_stack_begrunnelse.md` | Hvert teknologivalg med begrunnelse og alternativer vurdert | 1t |
| `tech/flytdiagrammer.md` | Mermaid-diagram for hovedflyten (oppdrag inn → sjåfør varslet) | 1t |
| `prosjekt/beslutningslogg.md` | Tekniske valg: hva, hvorfor, alternativer | 1–2t |
| `prosjekt/endringslogg.md` | Hva endret seg fra tidlig MVP til nå | 1t |
| `krav/ikke_funksjonelle_krav.md` | Ytelse, sikkerhet, skalerbarhet, tilgjengelighet | 1t |
| `krav/kravsporing.md` | Tabell: krav → implementert (ja/nei) → testet (ja/nei) | 1–2t |

**Estimert total Embret: ~12–16 timer**

---

## 🎤 Mikael – prosjekt- og brukerkontekst

Disse filene bygger på det du allerede vet og har gjort.

### Prioritet 1 – må være på plass først (blokkerer begge)
| Fil | Hva som skal inn | Estimert tid |
|-----|-----------------|:------------:|
| `context/master_context.md` | Hva er Ressursplanlegger, problem, målgruppe, stack-oversikt, status | 1–2t |
| `context/scope.md` | Hva er i scope og hva er ikke i scope – konkret og presis | 0.5t |
| `context/ordliste.md` | Alle sentrale begreper definert i vår kontekst | 0.5t |
| `PROMPT_GUIDE.md` | Instruksjoner til AI om språk, stil, hvilke filer den skal lese | 0.5t |
| `DONT.md` | Eksplisitte forbud: ikke finn opp refs, ikke endre scope, osv. | 0.5t |

### Prioritet 2 – viktig, men blokkerer ikke Embret
| Fil | Hva som skal inn | Estimert tid |
|-----|-----------------|:------------:|
| `context/rapportoutline.md` | Deres versjon av innholdsfortegnelsen med stikkord per kapittel | 1t |
| `context/skrivestil_eksempel.md` | 2–4 avsnitt som setter tone og formelt nivå | 0.5t |
| `brukerinnsikt/personas.md` | 2–3 brukerroller med beskrivelse og behov | 1t |
| `brukerinnsikt/ui_flyt.md` | Tekstlig gjennomgang av skjermene og brukerflytene | 1–2t |
| `brukerinnsikt/brukertester.md` | Tilbakemeldinger fra trafikkledere underveis | 1t |
| `krav/funksjonelle_krav.md` | Kravliste med ID, beskrivelse, prioritet, kilde (fra intervjuer) | 1–2t |
| `metode/forskningsdesign.md` | Valgt metode med begrunnelse | 1t |
| `metode/teoriramme.md` | VRP, resource scheduling, human-in-the-loop – kort beskrivelse | 1–2t |
| `metode/litteraturliste.md` | Faktiske kilder dere har lest – BibTeX eller enkel liste | 2–3t |
| `prosjekt/sprint_logg.md` | Kort per sprint / uke bakover i tid | 1–2t |
| `prosjekt/risikologg.md` | Risikoer, sannsynlighet, konsekvens, tiltak | 0.5t |
| `STATUS.md` | Hva som er gjort, pågår og mangler – oppdateres løpende | 0.5t |

**Estimert total Mikael: ~14–18 timer**

---

## 🤝 Gjøres sammen (etter at Prioritet 1 er ferdig)

| Oppgave | Estimert tid |
|---------|:------------:|
| Les hverandres Prioritet 1-filer og gi tilbakemelding | 1t |
| Bli enige om rapportoutline og kapittelstruktur | 1t |
| Test AI med kontekstfilene – generer et prøvekapittel og evaluer | 1t |

---

## Anbefalt rekkefølge denne uken

```
Dag 1
├── Mikael: master_context.md + scope.md + ordliste.md
└── Embret: algoritme.md + arkitektur.md

Dag 2
├── Mikael: PROMPT_GUIDE.md + DONT.md + rapportoutline.md
└── Embret: datamodell.md + api_oversikt.md

Dag 3
├── Begge: les hverandres filer, gi tilbakemelding, juster
└── Begge: test AI med kontekstfilene på et prøvekapittel

Dag 4–5
├── Mikael: personas, ui_flyt, krav, litteraturliste
└── Embret: tech_stack, flytdiagrammer, kravsporing, beslutningslogg
```

---

## Hvorfor denne rekkefølgen?

`master_context.md` og `algoritme.md` er de to filene som gir AI-en mest
å jobbe med. Alt annet bygger på dem. Lag disse to først – da kan dere
begynne å teste AI-arbeidsflyten allerede på dag 3 mens resten av
filene fylles inn.
