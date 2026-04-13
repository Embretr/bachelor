# Literature List — Ressursplanlegger

> **Owner: Mikael** — add sources here AS YOU READ THEM.
> Claude will ONLY cite sources listed here — it will never invent references.
> Once confirmed read and relevant, add the BibTeX entry to result/references.bib.
> Mark Read = ✅ only after you have actually read the source.

---

## Status

| Key | Authors | Title | Read? | In .bib? |
|-----|---------|-------|:-----:|:--------:|
| toth2014vrp | Toth & Vigo | Vehicle Routing: Problems, Methods, and Applications (2nd ed.) | ⬜ | ⬜ |
| dantzig1959truck | Dantzig & Ramser | The Truck Dispatching Problem | ⬜ | ⬜ |
| hevner2004dsr | Hevner et al. | Design Science in IS Research | ⬜ | ⬜ |
| peffers2007dsr | Peffers et al. | A DSR Methodology for IS Research | ⬜ | ⬜ |
| parasuraman2000automation | Parasuraman, Sheridan & Wickens | A Model for Types and Levels of Human Interaction with Automation | ⬜ | ⬜ |
| pinedo2016scheduling | Pinedo | Scheduling: Theory, Algorithms, and Systems (5th ed.) | ⬜ | ⬜ |
| braun2006qualitative | Braun & Clarke | Using thematic analysis in psychology | ⬜ | ⬜ |
| [FILL IN] | | | ⬜ | ⬜ |

---

## Category: Vehicle Routing Problem

### ⬜ Dantzig & Ramser (1959) — origin of the VRP
**Full reference:** Dantzig, G. B., & Ramser, J. H. (1959). The Truck Dispatching Problem. *Management Science*, 6(1), 80–91.
**Why relevant:** The foundational paper that first formulated the vehicle routing problem. Historical context for Chapter 2.1.
**BibTeX key:** `dantzig1959truck`

### ⬜ Toth & Vigo (2014) — comprehensive VRP reference
**Full reference:** Toth, P., & Vigo, D. (Eds.). (2014). *Vehicle Routing: Problems, Methods, and Applications* (2nd ed.). Society for Industrial and Applied Mathematics.
**Why relevant:** Definitive textbook covering VRP variants (CVRP, VRPTW, multi-depot), exact and heuristic methods, and real-world applications. Primary source for Chapter 2.1.
**BibTeX key:** `toth2014vrp`

### ⬜ [FIND: VRPTW survey paper]
**Search term:** "vehicle routing problem time windows survey" OR "VRPTW survey"
**Why needed:** Ressursplanlegger uses time windows — need a focused source on the VRPTW variant specifically.

### ⬜ [FIND: VRP with heterogeneous fleet]
**Search term:** "vehicle routing heterogeneous fleet"
**Why needed:** Different vehicle types (truck, van, crane) is a key constraint in Ressursplanlegger.

---

## Category: Resource Scheduling / Decision Support

### ⬜ Pinedo (2016) — scheduling theory
**Full reference:** Pinedo, M. L. (2016). *Scheduling: Theory, Algorithms, and Systems* (5th ed.). Springer.
**Why relevant:** Comprehensive textbook on scheduling theory, algorithms, and real-world systems. Resource scheduling is the broader theoretical frame for the assignment problem.
**BibTeX key:** `pinedo2016scheduling`

### ⬜ [FIND: crew scheduling / driver scheduling]
**Search term:** "crew scheduling optimization transportation" OR "driver scheduling constraints"
**Why needed:** Direct analogues to Ressursplanlegger's problem — assigning human resources to tasks with competency and availability constraints.

### ⬜ [FIND: nurse scheduling as analogous domain]
**Search term:** "nurse scheduling problem constraint programming"
**Why needed:** Nurse scheduling shares key structural features with driver scheduling: competencies, shift patterns, fairness, hard/soft constraints. Well-studied domain with applicable methods.

---

## Category: Human-in-the-Loop and Automation

### ⬜ Parasuraman, Sheridan & Wickens (2000) — levels of automation
**Full reference:** Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans*, 30(3), 286–297.
**Why relevant:** Provides the 10-level automation scale. Ressursplanlegger operates at level 5–6 (system suggests, human approves). Key theoretical backing for the suggest+override pattern.
**BibTeX key:** `parasuraman2000automation`

### ⬜ [FIND: trust in automation]
**Search term:** "trust in automation decision support systems"
**Why needed:** Adoption barrier identified in interviews — coordinators must trust the algorithm. Trust-in-automation literature provides theoretical framing for this finding.

### ⬜ [FIND: decision support systems in logistics]
**Search term:** "decision support systems logistics transportation"
**Why needed:** Positions Ressursplanlegger within the DSS literature, not just the VRP literature.

---

## Category: Research Methodology

### ⬜ Hevner et al. (2004) — Design Science Research
**Full reference:** Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
**Why relevant:** Foundational DSR paper. Justification for the research approach in Chapter 3.
**BibTeX key:** `hevner2004dsr`

### ⬜ Peffers et al. (2007) — DSR methodology
**Full reference:** Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.
**Why relevant:** Provides the six-phase DSR process model used to structure this project.
**BibTeX key:** `peffers2007dsr`

### ⬜ Braun & Clarke (2006) — thematic analysis
**Full reference:** Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
**Why relevant:** Justification for the thematic analysis approach used on interview transcripts. Chapter 3.3.
**BibTeX key:** `braun2006qualitative`

### ⬜ [FIND: semi-structured interviews methodology]
**Search term:** "semi-structured interviews qualitative research methodology"
**Why needed:** Chapter 3.2 — justification for interview format and design.

---

## Category: Transport Management Systems

### ⬜ [FIND: TMS overview / industry report]
**Search term:** "transport management systems TMS review" OR "TMS logistics software"
**Why needed:** Chapter 2.3 — background on TMS landscape. Positions Ressursplanlegger relative to existing software categories.

### ⬜ [FIND: digitalisation in Norwegian transport]
**Search term:** "digitalisation transport logistics Norway" OR "digital transformation freight transport Scandinavia"
**Why needed:** Context for why this problem exists now — the Norwegian transport sector and its digital maturity.

---

## Category: Constraint Programming and Solvers

### ⬜ [FIND: CP-SAT / constraint programming for scheduling]
**Search term:** "constraint programming scheduling survey" OR "CP-SAT solver applications"
**Why needed:** Chapter 2 or 4.5 — theoretical basis for the OR-Tools solver approach.

### ⬜ [FIND: metaheuristics for vehicle routing]
**Search term:** "metaheuristics vehicle routing problem tabu search simulated annealing"
**Why needed:** Theoretical basis for the Timefold solver approach (tabu search, simulated annealing, late acceptance).

**Candidates from NTNU CVRP thesis (Andersen et al., 2021):**
- Lourenço, H.L., Martin, O.C., & Stützle, T. (2003). Iterated Local Search. In *Handbook of Metaheuristics*, ch. 11, pp. 321–353. Kluwer.
- Máximo, V.R. et al. (2020). A hybrid adaptive iterated local search with diversification control to the CVRP. arXiv:2012.11021.
- Bräysy, O. (2001). Genetic algorithms for the vehicle routing problem with time windows.
- *Check with Embret which of these are relevant for our solver implementations.*

---

## BibTeX Entries (copy to result/references.bib when ready)

```bibtex
@article{dantzig1959truck,
  author  = {Dantzig, George B. and Ramser, John H.},
  title   = {The Truck Dispatching Problem},
  journal = {Management Science},
  year    = {1959},
  volume  = {6},
  number  = {1},
  pages   = {80--91},
}

@book{toth2014vrp,
  editor    = {Toth, Paolo and Vigo, Daniele},
  title     = {Vehicle Routing: Problems, Methods, and Applications},
  edition   = {2nd},
  publisher = {Society for Industrial and Applied Mathematics},
  address   = {Philadelphia},
  year      = {2014},
}

@article{hevner2004dsr,
  author  = {Hevner, Alan R. and March, Salvatore T. and Park, Jinsoo and Ram, Sudha},
  title   = {Design Science in Information Systems Research},
  journal = {MIS Quarterly},
  year    = {2004},
  volume  = {28},
  number  = {1},
  pages   = {75--105},
}

@article{peffers2007dsr,
  author  = {Peffers, Ken and Tuunanen, Tuure and Rothenberger, Marcus A. and Chatterjee, Samir},
  title   = {A Design Science Research Methodology for Information Systems Research},
  journal = {Journal of Management Information Systems},
  year    = {2007},
  volume  = {24},
  number  = {3},
  pages   = {45--77},
}

@article{parasuraman2000automation,
  author  = {Parasuraman, Raja and Sheridan, Thomas B. and Wickens, Christopher D.},
  title   = {A Model for Types and Levels of Human Interaction with Automation},
  journal = {IEEE Transactions on Systems, Man, and Cybernetics --- Part A: Systems and Humans},
  year    = {2000},
  volume  = {30},
  number  = {3},
  pages   = {286--297},
}

@book{pinedo2016scheduling,
  author    = {Pinedo, Michael L.},
  title     = {Scheduling: Theory, Algorithms, and Systems},
  edition   = {5th},
  publisher = {Springer},
  year      = {2016},
}

@article{braun2006qualitative,
  author  = {Braun, Virginia and Clarke, Victoria},
  title   = {Using Thematic Analysis in Psychology},
  journal = {Qualitative Research in Psychology},
  year    = {2006},
  volume  = {3},
  number  = {2},
  pages   = {77--101},
}
```

---

## How to Add a New Source

1. Find the source — verify it exists (DOI, publisher, Google Scholar)
2. Add an entry in the relevant category above with full reference, why relevant, and BibTeX key
3. Read it and mark Read = ✅
4. Copy the BibTeX entry to `result/references.bib`
5. Mark In .bib = ✅
6. Update the status table at the top
