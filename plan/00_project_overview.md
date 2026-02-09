# QC Transition Plan — Project Overview & Outline
**File:** `00_project_overview.md`

---

## Single Project Question

**How do quantum compilation choices interact with measurement error mitigation to affect observable outcome distributions in small, NISQ-era quantum circuits?**

This project builds a minimal, transparent quantum compilation and error-mitigation pipeline in Python to study how different circuit representations, transpilation strategies, and measurement error mitigation techniques jointly influence experimental results under realistic noise.

---

## Project End-State Deliverables (Global)

By the end of the plan, the project will include:

- A modular Python codebase implementing:
  - a minimal circuit intermediate representation (IR)
  - simple compilation / transpilation passes
  - noise and measurement error models
  - measurement error mitigation routines
- A reproducible experimental pipeline comparing:
  - multiple compilation strategies
  - mitigated vs. unmitigated measurement outcomes
- A written technical report (Markdown or LaTeX) with:
  - problem motivation
  - methodology
  - quantitative results (plots, tables)
  - discussion and limitations
- A professional GitHub repository demonstrating:
  - clean software engineering practices
  - disciplined AI-assisted development
  - incremental daily progress

---

## Week-by-Week Outline

---

## Week 1 — Project & Engineering Foundations

**Theme:** Environment setup, repo structure, Python fundamentals, project framing

**Deliverables:**
- GitHub repository initialized with professional structure
- Reproducible Python environment
- Initial README describing project scope and AI usage policy
- First Python modules with strict PEP-8 + docstrings
- Clear definition of circuit abstraction goals

---

## Week 2 — Quantum Circuit Representation (IR)

**Theme:** Object-oriented design for quantum circuits

**Deliverables:**
- Circuit, gate, and qubit abstractions implemented in Python
- Methods for circuit construction and inspection
- Unit tests for basic circuit behavior
- Documentation of design decisions in module README

---

## Week 3 — Compilation & Transpilation Passes

**Theme:** Simple compiler transformations

**Deliverables:**
- One or more compilation passes (e.g., gate rewriting, reordering)
- Pass manager or pipeline abstraction
- Comparison of pre- and post-compilation circuit structure
- Tests validating semantic preservation

---

## Week 4 — Noise & Measurement Error Modeling

**Theme:** Modeling realistic measurement noise

**Deliverables:**
- Measurement noise model (confusion matrix–based)
- Optional simple gate noise model
- Simulation of noisy measurement outcomes
- Clear separation between ideal and noisy execution paths

---

## Week 5 — Measurement Error Mitigation

**Theme:** Mitigation algorithms and numerical stability

**Deliverables:**
- Measurement error mitigation routines
- Probability-space vs. count-space handling
- Tests for mitigation correctness and edge cases
- Documentation discussing assumptions and limitations

---

## Week 6 — End-to-End Pipeline Integration

**Theme:** System integration and architecture cleanup

**Deliverables:**
- End-to-end pipeline:
  circuit → compile → noise → mitigate → results
- Refactored codebase with clean module boundaries
- CI passing for formatting, linting, and tests
- Architecture overview documentation

---

## Week 7 — Benchmark Circuits & Experiments

**Theme:** Experimental design

**Deliverables:**
- Small benchmark circuits (e.g., toy VQE-style circuits)
- Parameterized experiment scripts
- Data collection and storage format
- Reproducible experiment configuration

---

## Week 8 — Quantitative Analysis & Visualization

**Theme:** Results and interpretation

**Deliverables:**
- Metrics comparing compilation strategies
- Plots showing mitigated vs. unmitigated outcomes
- Analysis scripts with documented assumptions
- Initial figures for the technical report

---

## Week 9 — Technical Report Drafting

**Theme:** Writing and communication

**Deliverables:**
- Full draft of technical report (Markdown or LaTeX)
- Clear explanation of methodology and results
- Figures integrated into the report
- Internal consistency checks between code and text

---

## Week 10 — Refinement, Polish, and Signaling

**Theme:** Professional polish and external readability

**Deliverables:**
- Final refactors and cleanup
- Improved documentation and comments
- Final README with:
  - setup instructions
  - project narrative
  - AI usage explanation
- Optional submission-ready version of the report (preprint / workshop style)

---

## Optional Extensions (If Time Remains)

- Additional compilation strategies
- Sensitivity analysis over noise parameters
- Comparison with conceptual behavior of existing frameworks (no code copying)
- Public-facing blog post summarizing findings

---

## Hiring Manager Narrative (Outline)

This project demonstrates:
- disciplined daily engineering practice
- strong Python and OOP fundamentals
- applied understanding of quantum compilation and error mitigation
- responsible, transparent use of AI as a development aid
- ability to take a research question from concept to reproducible result

---
