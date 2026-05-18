# QC Transition Plan — Project Overview & Outline
**File:** `00_project_overview.md`

---

## Single Project Question

**How do compilation structure, readout noise, and measurement error mitigation jointly affect observable outcome distributions in small quantum circuits?**

This project builds a minimal, transparent quantum experimentation pipeline in Python to study how circuit structure, simple compiler transformations, state preparation, readout noise, and measurement error mitigation influence experimental results under realistic noise.

The project emphasizes:
- clean software engineering
- reproducible experimentation
- transparent implementations
- incremental architecture growth
- responsible AI-assisted development

---

## Project End-State Deliverables (Global)

By the end of the plan, the project will include:

- A modular Python codebase implementing:
  - a minimal circuit intermediate representation (IR)
  - compiler-pass abstractions
  - simple transpilation / rewriting passes
  - measurement noise models
  - measurement error mitigation routines
  - lightweight single-qubit statevector simulation
- A reproducible experimental pipeline supporting:
  - deterministic and probabilistic circuits
  - noisy versus ideal execution paths
  - mitigated versus unmitigated comparisons
  - CSV-based experiment persistence
  - experiment visualization
- A written technical report containing:
  - project motivation
  - methodology
  - quantitative results
  - limitations
  - future work
- A professional GitHub repository demonstrating:
  - strong Python and OOP fundamentals
  - modular architecture
  - testing discipline
  - reproducibility practices
  - disciplined AI-assisted engineering workflow

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
- Compiler-pass abstraction
- Pass manager / pipeline abstraction
- Basic circuit rewriting and transformation passes
- Tests validating semantic preservation
- Comparison of pre- and post-transformation circuit structure

---

## Week 4 — Noise & Measurement Error Modeling

**Theme:** Modeling realistic measurement noise

**Deliverables:**
- Measurement noise model (confusion matrix–based)
- Simulation of noisy measurement outcomes
- Separation between ideal and noisy execution paths
- Noise sweep experiments
- CSV result generation
- Basic visualization pipeline

---

## Week 5 — Measurement Error Mitigation & Statevector Simulation

**Theme:** Mitigation algorithms and probabilistic quantum behavior

**Deliverables:**
- Measurement error mitigation routines
- Probability-space and count-space workflows
- Single-qubit statevector simulator
- Support for `X`, `Z`, `H`, and `MEASURE`
- Deterministic versus superposition circuit experiments
- Circuit comparison visualization
- Tests for mitigation correctness and edge cases
- Documentation discussing assumptions and limitations

---

## Week 6 — Pipeline Integration & Architecture Cleanup

**Theme:** System integration and maintainability

**Deliverables:**
- End-to-end experimental workflow:
  circuit → simulate → noise → mitigate → results
- Centralized experiment configuration
- Shared experiment path utilities
- Shared experiment summary helpers
- Shared validation utilities
- Refactored codebase with cleaner module boundaries
- Consistent experiment workflows and formatting
- CI passing for formatting, linting, and tests

---

## Week 7 — Technical Report Foundations & Compilation-Focused Experiments

**Theme:** Technical communication and experiment alignment

**Deliverables:**
- Initial technical report draft
- Methodology and architecture sections
- Results narrative for current experiments
- Compilation-focused benchmark experiments
- Comparison between transformed and untransformed circuits
- Integration of figures and experimental outputs into report structure

---

## Week 8 — Quantitative Analysis & Report Refinement

**Theme:** Results interpretation and professional presentation

**Deliverables:**
- Metrics comparing experimental configurations
- Improved plots and figure formatting
- Analysis scripts with documented assumptions
- Integrated report figures and captions
- Expanded limitations and future-work discussion

---

## Week 9 — Repository Polish & Portfolio Positioning

**Theme:** Professional presentation and external readability

**Deliverables:**
- Final refactors and cleanup
- Improved documentation and comments
- Final README with:
  - setup instructions
  - project narrative
  - experiment walkthrough
  - AI usage explanation
- Interview-ready repository structure
- Optional public-facing project summary or blog draft

---

## Optional Extensions (If Time Remains)

- Multi-qubit statevector simulation
- Additional compilation strategies
- Correlated readout noise
- More sophisticated benchmark circuits
- Comparison against conceptual behavior of existing frameworks
- Public-facing blog post summarizing findings

---

## Hiring Manager Narrative (Outline)

This project demonstrates:
- disciplined daily engineering practice
- strong Python and OOP fundamentals
- applied understanding of quantum circuits, noise, and mitigation
- experiment design and reproducibility
- modular software architecture
- responsible, transparent use of AI as a development aid
- ability to take a technical question from concept to reproducible result
