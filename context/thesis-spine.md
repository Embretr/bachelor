# Thesis Spine — Ressursplanlegger

> This file is the backbone of the thesis.
> Every agent reads this before writing or reviewing anything.
> Update it if the argument changes — but try not to change it.
> One sentence per chapter. No more.

---

## The Problem

Traffic coordinators in Norwegian transport companies assign drivers and vehicles to
jobs manually, relying on tacit knowledge not captured in any system, using legacy
software that is too slow and provides no decision support.

---

## The Research Question

> How can an algorithm-driven resource planning platform support traffic coordinators in Norwegian transport companies in assigning drivers and vehicles to assignments more efficiently than current manual processes?

### Sub-questions the thesis must answer

1. What are the current practices, pain points, and needs of traffic coordinators in Norwegian transport companies when assigning drivers and vehicles to assignments? → Ch 4.1, 4.3
2. How should an algorithm-assisted planning system be designed to balance automated optimisation with the coordinator's need for manual control and oversight? → Ch 2, 4.4, 4.5
3. To what extent does the proposed system address the identified needs, and what are its limitations? → Ch 5, 6

---

## The Argument — One Sentence Per Chapter

**Chapter 1 — Introduction:**
Manual resource planning in Norwegian transport is inefficient, error-prone, and dependent on individual coordinators' tacit knowledge — a problem that warrants a structured, algorithm-assisted solution.

**Chapter 2 — Theory:**
Resource scheduling and constraint programming define the algorithmic problem class, human-in-the-loop automation defines the interaction pattern, the Transport Management System landscape positions Ressursplanlegger against existing tools, and Design Science Research frames the build-and-validate inquiry — together providing the theoretical foundation for a system that automates plan generation while preserving coordinator control; vehicle routing theory is referenced only to delimit the problem.

**Chapter 3 — Methodology:**
Design Science Research structures the project: semi-structured interviews with seven traffic coordinators identified the problem and requirements, iterative development produced the artefact, and validation through benchmarking and requirements traceability assessed its quality.

**Chapter 4 — Findings:**
Interviews revealed universal pain points (slow systems, tacit knowledge dependency, no planning support), and Ressursplanlegger was built to address these through a multi-engine optimisation algorithm, conflict detection, and a human-in-the-loop planning interface.

**Chapter 5 — Discussion:**
Ressursplanlegger addresses the core planning gap that no existing system fills, but adoption depends on invoicing integration, system performance, and coordinator trust — and the irreducible role of tacit knowledge means full automation is neither feasible nor desirable.

**Chapter 6 — Conclusion:**
Algorithm-assisted resource planning can meaningfully support traffic coordinators, but the system complements rather than replaces human judgment; production deployment and invoicing integration are essential next steps.

---

## How to Use This File

- **Writer agent:** Check that each section you write serves the chapter's one-sentence purpose above.
- **Red thread agent:** Verify that no chapter introduces arguments or conclusions that contradict or skip ahead of this spine.
- **Quality agent:** Use this to assess whether the overall argument is coherent.

---

## Spine Status: APPROVED DRAFT

Last revised: 2026-04-12. Based on finalised sub-questions and complete context files.
Review again after Chapter 4 is drafted — if findings shift the argument, update the spine before writing Chapter 5.
