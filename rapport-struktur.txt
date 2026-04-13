Rapportstruktur — Ressursplanlegger
Innledning
1.1 Bakgrunn og motivasjon


Transportsektoren i Norge, digitalisering
Trafikklederrollen og daglig planlegging
Problemet: taus kunnskap, trege systemer, ingen planleggingsstøtte
Konsekvenser: ineffektivitet, nøkkelpersonavhengighet, feilrisiko
Hvorfor nå: OR-Tools, Timefold, digital transformasjon
Introduser Ressursplanlegger i ett avsnitt
1.2 Forskningsspørsmål


Hovedspørsmålet (verbatim)
Tre delspørsmål: problem -> løsning -> evaluering
1.3 Avgrensninger


Hva systemet dekker
Hva som er utenfor scope (og hvorfor)
Arbeidsfordeling Mikael / Embret
1.4 Oppgavens oppbygning


Narrativ kjede, ikke innholdsfortegnelse
Teori
2.1 Ressursplanlegging


Definisjon og analoge domener (Pinedo)
Multi-ressurs: ansatt + kjøretøy
Harde og myke begrensninger (Rossi) + systemets modell
NP-hardhet, VRP-sammenligning (Dantzig, Toth)
Tre solvere: greedy, CP-SAT, Timefold
2.2 Menneske-i-løkka-automatisering


Definisjon + Parasuraman 10-nivå skala
Hvorfor HITL er nødvendig i transport
"Suggest + override"-designmønster
Tillit og adopsjon (Lee)
HITL som designbegrensning
2.3 Transportadministrasjonssystemer (TMS)


TMS som programvarekategori
Norsk landskap: Timpex, Trimtex, Opptur
Planleggingsgapet ingen systemer dekker
2.4 Design Science Research


DSR-definisjon (Hevner, Peffers)
Hvorfor DSR passer dette prosjektet
Validering vs. evaluering (Wieringa)
Metode
3.1 Forskningsdesign


DSR som metode (Peffers 6 faser, Hevner)
Hvorfor DSR passer
DSR-faser mappt til prosjektet
Validering vs. evaluering
3.2 Datainnsamling


Semi-strukturerte intervjuer — begrunnelse
Utvalg: 7 selskaper, variasjon i størrelse/system
Intervjuguide: 5 temaer
Gjennomføring: telefonintervju 4. mars 2026
Transkripsjon: Sonix.ai + manuell korrigering
3.3 Dataanalyse


Tematisk analyse (Braun & Clarke)
Fra temaer til krav (MoSCoW, fit/gap)
Begrensninger
3.4 Utviklingsprosess


Smidig, iterativ utvikling
Kobling mellom brukerundersøkelse og utvikling
Teknologivalg (kort)
Tidslinje
3.5 Validitet og reliabilitet


Malteruds fire kriterier
Intervjuvaliditet
Systemvaliditet
Forskerbiasrisiko
Funn
4.1 Intervjufunn


Dagens planleggingsprosesser
Smertepunkter: treghet, taus kunnskap, kapasitetsoversikt
Sykefravårshåndtering
Holdninger til automatisering
Tildelingskriterier — rangert liste
4.2 Krav


Funksjonelle krav (MoSCoW-tabell)
Ikke-funksjonelle krav
4.3 Fit/gap-analyse


Hva eksisterende systemer gir vs. behov
Fit-tabell og gap-tabell
4.4 Systembeskrivelse


Arkitekturoversikt
Nøkkelfunksjoner: planvisning, manuell overstyring
UI-flyt
Teknologistakk med begrunnelse
4.5 Optimaliseringsalgoritme


Problemformulering
Valgt tilnærming og begrunnelse
Modellerte begrensninger (harde + myke)
Målfunksjon
Kjente begrensninger
Diskusjon
5.1 Adresserer Ressursplanlegger smertepunktene?


Intervjufunn mappt til implementerte funksjoner
Løst / delvis løst / uadressert
Kobling til teori (scheduling + HITL)
5.2 Algoritmens ytelse og menneske-i-løkka


Algoritmens håndtering av begrensninger
Hvor manuell overstyring fortsatt trengs
Kobling til HITL-teori (Parasuraman)
Er "suggest + override" riktig mønster?
5.3 Adopsjonshindringer


Kost/nytte-terskel
Brukervennlighet og tillit
Integrasjon med faktureringssystemer
Hva trengs for produksjonsdrift?
5.4 Taus kunnskap som designutfordring


Hvordan systemet formaliserer koordinatorkunnskap
Hva som ikke kan automatiseres
Implikasjoner for fremtidig design
5.5 Bærekraft


SusAF-rammeverk (Duboc)
Bærekraftseffekter-tabell
Nøkkeldilemmaer
Mapping til FNs bærekraftsmål
Begrensninger i analysen
5.6 Begrensninger ved studien


Lite intervjuutvalg (7)
Ikke deployert i produksjon
Utviklingsteam = forskere
Konklusjon
6.1 Oppsummering


Ett avsnitt per kapittel
6.2 Svar på forskningsspørsmålene


Svar på hovedspørsmålet
Svar på SQ1, SQ2, SQ3
6.3 Videre arbeid


Sjåførapp med push-varsler
Fakturering/integrasjon
Produksjonspilot
Sanntidsomplanlegging ved sykefravær
Algoritmeforbedringer med større datasett


