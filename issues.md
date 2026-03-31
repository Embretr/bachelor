GitHub Issues — Ressursplanlegger Bachelor Repo

Copy each block below into a new GitHub Issue.
Labels to create first: context, tech, rapport, Mikael, Embret, priority:high, priority:medium


🔴 PRIORITY 1 — Must be done before writing starts

Issue 1
Title: [context] Fyll inn context.md — tittel, problemstilling, forskningsspørsmål
Labels: context, Mikael, priority:high
Assignee: Mikael
Fyll inn følgende felter i context/context.md:

 Tittel på oppgaven
 Undertittel (hvis aktuelt)
 Navn på begge forfattere
 Navn på veileder
 Innleveringsfrist
 Hovedproblemstilling / research question
 2–3 delspørsmål
 Teknisk stack (legg inn verdier i tabellen)


Issue 2
Title: [context] Skriv scope.md — hva er og ikke er i scope
Labels: context, Mikael, priority:high
Assignee: Mikael
Gå gjennom context/scope.md og:

 Bekreft / utvid listen over hva som er i scope
 Legg til eventuelle manglende punkter under "Out of Scope"
 Fyll inn statusfelter i systemfunksjonalitet som er uklar


Issue 3
Title: [tech] Fyll inn algoritme.md — input, output, constraints, metode
Labels: tech, Embret, priority:high
Assignee: Embret
Fyll inn tech/algoritme.md fullstendig:

 Problemformulering — hvilken type problem er dette (VRP-variant, scheduling, etc.)
 Input — alle parametere med type og beskrivelse
 Output — hva returnerer algoritmen
 Hard constraints (must not be violated)
 Soft constraints (should be respected)
 Objective function — hva maksimeres/minimeres
 Valgt metode / bibliotek med begrunnelse
 Steg-for-steg beskrivelse av algoritmen
 Kjente begrensninger

Dette er direkte grunnlag for kapittel 4.5 og 5.2.

Issue 4
Title: [tech] Fyll inn arkitektur.md — frontend, backend, database, deploy
Labels: tech, Embret, priority:high
Assignee: Embret
Fyll inn tech/arkitektur.md:

 Overordnet arkitekturbeskrivelse (ett avsnitt)
 Legg til Mermaid-diagram over systemet
 Frontend: rammeverk, state management, nøkkelkomponenter
 Backend: rammeverk, struktur, autentisering, nøkkelmoduler
 Database: system, hosting, ORM
 Optimiseringsmotor: kjøres den i backend eller separat?
 Deploy-oppsett


Issue 5
Title: [context] Fyll inn disposisjon.md — stikkord per kapittel
Labels: context, Mikael, priority:high
Assignee: Mikael
Gå gjennom context/disposisjon.md og bekreft/juster:

 Er kapitlene riktig strukturert for vår oppgave?
 Legg til manglende seksjoner
 Fyll inn "Sources needed" per kapittel med faktiske kilder dere har eller skal finne
 Juster "Target length" per kapittel etter malens totale sidekrav


🟠 PRIORITY 2 — Viktig, gjøres parallelt

Issue 6
Title: [tech] Lag datamodell.md — alle entiteter med felter og relasjoner
Labels: tech, Embret, priority:medium
Assignee: Embret
Opprett tech/datamodell.md med:

 Alle entiteter (Oppdrag, Sjåfør, Kjøretøy, Bruker, Plan, osv.)
 Feltnavn, datatype og beskrivelse per felt
 Relasjoner mellom entiteter (1:1, 1:N, N:M)
 ER-diagram i Mermaid (valgfritt men anbefalt)


Issue 7
Title: [tech] Lag api-oversikt.md — alle endepunkter
Labels: tech, Embret, priority:medium
Assignee: Embret
Opprett tech/api-oversikt.md:

 Liste over alle API-endepunkter
 Metode (GET/POST/PUT/DELETE) og URL
 Kort beskrivelse av hva endepunktet gjør
 Request body og response format der relevant


Issue 8
Title: [tech] Lag tech-stack.md — teknologivalg med begrunnelse
Labels: tech, Embret, priority:medium
Assignee: Embret
Opprett tech/tech-stack.md:

 For hvert teknologivalg: hva ble valgt, hvorfor, hvilke alternativer ble vurdert
 Dekk minst: frontend, backend, database, algoritmebibliotek
 Dette brukes direkte i kapittel 4.4 og diskusjonen


Issue 9
Title: [krav] Lag funksjonelle-krav.md — kravliste med MoSCoW og kilde
Labels: context, Mikael, priority:medium
Assignee: Mikael
Opprett krav/funksjonelle-krav.md:

 Liste over alle funksjonelle krav med ID (FK-01, FK-02, ...)
 Beskrivelse, MoSCoW-prioritet og kilde (hvilket intervju / hvem ba om dette)
 Bruk context/intervju-funn.md og fit/gap-analysen som grunnlag
 Minimum 10 krav


Issue 10
Title: [krav] Lag kravsporing.md — krav vs. implementert vs. testet
Labels: tech, Embret, priority:medium
Assignee: Embret
Opprett krav/kravsporing.md basert på krav/funksjonelle-krav.md:

 Tabell: krav-ID, kort beskrivelse, implementert (✅/⬜), testet (✅/⬜), kommentar
 Oppdater når nye krav implementeres eller testes


Issue 11
Title: [metode] Skriv forskningsdesign.md
Labels: context, Mikael, priority:medium
Assignee: Mikael
Opprett metode/forskningsdesign.md:

 Valgt forskningsmetode (Design Science Research, casestudie, eller annet)
 Begrunnelse for valget — hvorfor passer denne metoden for et utviklingsprosjekt?
 Koble til kapittel 3 i disposisjon.md


Issue 12
Title: [metode] Bygg litteraturliste — faktiske kilder dere har lest
Labels: context, Mikael, priority:medium
Assignee: Mikael
Opprett metode/litteraturliste.md og fyll inn bibtex/referanser.bib:

 Finn og les minst 3 kilder om VRP / resource scheduling
 Finn og les minst 2 kilder om TMS / transport management
 Finn og les minst 1 kilde om human-in-the-loop automation
 Finn og les minst 1 kilde om Design Science Research (hvis brukt som metode)
 Legg alle i referanser.bib med korrekt BibTeX-format


Issue 13
Title: [context] Fyll inn fitgap-sammendrag.md
Labels: context, Mikael, priority:medium
Assignee: Mikael
Fullfør context/fitgap-sammendrag.md:

 Beskriv hva som sammenlignes (Ressursplanlegger vs. eksisterende systemer / behov)
 Fyll inn Fit-tabellen — krav som dekkes
 Fyll inn Gap-tabellen — krav som ikke dekkes, med alvorlighetsgrad
 Skriv oppsummeringsavsnitt


🟡 PRIORITY 3 — Gjøres etter Prioritet 1 og 2

Issue 14
Title: [prosjekt] Lag beslutningslogg.md — tekniske valg med begrunnelse
Labels: tech, Embret, priority:medium
Assignee: Embret
Opprett prosjekt/beslutningslogg.md:

 Dokumenter alle viktige tekniske beslutninger bakover i tid
 Format: dato, beslutning, alternativer vurdert, begrunnelse
 Minst 5 beslutninger (algoritmemetode, stack-valg, arkitektur, osv.)


Issue 15
Title: [prosjekt] Lag sprint-logg.md — ukesvise fremgang
Labels: context, Mikael, priority:medium
Assignee: Mikael
Opprett prosjekt/sprint-logg.md:

 Dokumenter alle sprints / uker bakover i tid
 For hver sprint: hva ble planlagt, hva ble gjort, hindringer
 Brukes direkte i kapittel 3 (metodologi / prosess)


Issue 16
Title: [tech] Lag flytdiagrammer i Mermaid for hovedflyten
Labels: tech, Embret, priority:medium
Assignee: Embret
Opprett eller utvid tech/arkitektur.md med Mermaid-diagrammer for:

 Flyt: oppdrag mottas → algoritme kjøres → plan vises til koordinator → sjåfør varsles
 Flyt: manuell overstyring av algoritmens forslag
 Flyt: sykdomshåndtering / omrokkering


Issue 17
Title: [rapport] Skriv Kapittel 1 — Introduction
Labels: rapport, Mikael, priority:medium
Assignee: Mikael
Forutsetning: Issue 1, 2, 5 må være lukket først.
Skriv kapitler/kap1-innledning.tex:

 1.1 Background and Motivation
 1.2 Research Questions
 1.3 Scope and Delimitations
 1.4 Thesis Structure
 Kjør make og verifiser at det kompilerer


Issue 18
Title: [rapport] Skriv Kapittel 3 — Methodology
Labels: rapport, Mikael, priority:medium
Assignee: Mikael
Forutsetning: Issue 11 og sprint-logg må være på plass.
Skriv kapitler/kap3-metode.tex:

 3.1 Research Design
 3.2 Data Collection (intervjuprosessen)
 3.3 Data Analysis
 3.4 System Development Process
 3.5 Validity and Reliability


Issue 19
Title: [rapport] Skriv Kapittel 4 — Findings
Labels: rapport, Embret, priority:medium
Assignee: Embret (koordiner med Mikael)
Forutsetning: Issue 3, 4, 6, 9 må være lukket.
Skriv kapitler/kap4-funn.tex:

 4.1 Interview Findings (Mikael)
 4.2 Requirements (Mikael)
 4.3 Fit/Gap Analysis (Mikael)
 4.4 System Description (Embret)
 4.5 Optimisation Algorithm (Embret)


Issue 20
Title: [rapport] Skriv Kapittel 5 — System og Arkitektur + Implementasjon
Labels: rapport, Embret, priority:medium
Assignee: Embret
Forutsetning: Issue 4, 6, 7, 8 må være lukket.
Skriv eller utvid relevante kapitler:

 System og arkitektur (basert på tech/arkitektur.md)
 Implementasjon (basert på tech/kodebase-oppsummering.md)
 Tekniske valg og begrunnelser (basert på tech/tech-stack.md)
 Kjør make og verifiser at det kompilerer


Issue 21
Title: [oppsett] Fyll inn metadata i main.tex
Labels: tech, priority:high
Assignee: Mikael
Fyll inn placeholders i main.tex:

 [THESIS TITLE]
 [SUBTITLE IF ANY]
 [Author 1 Name]
 [Author 2 Name]
 [Supervisor Name]
 Sjekk at make kompilerer uten feil etter endringene


Issue 22
Title: [oppsett] Test at LaTeX-miljøet fungerer lokalt for begge
Labels: tech, priority:high
Assignee: Begge

 Embret: kjør make og bekreft at main.pdf genereres
 Mikael: kjør make og bekreft at main.pdf genereres
 Installer MacTeX / TeX Live hvis det mangler (se README.md)
 Test make watch for auto-kompilering
