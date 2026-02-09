# QC Transition Plan — Repository & Tooling Setup
**File:** `01_repo_and_tooling_setup.md`

---

## Purpose

This document defines the **authoritative engineering workflow** for the project described in  
`00_project_overview.md`.

It specifies:
- repository structure
- environment and dependency management
- code quality standards
- testing and automation
- AI-integrated development rules

This document is a **contract**.  
All implementation work must conform to it.

---

## Repository Structure

The repository is organized to separate **planning**, **source code**, **experiments**, and **communication artifacts**.

```text
<repo-root>/
├── plan/
│   ├── 00_project_overview.md
│   ├── 01_repo_and_tooling_setup.md
│   ├── week_01.md
│   ├── week_02.md
│   └── ...
├── src/
│   └── qc_compiler/
│       ├── __init__.py
│       ├── circuits/
│       ├── compilation/
│       ├── noise/
│       ├── mitigation/
│       └── utils/
├── tests/
│   ├── circuits/
│   ├── compilation/
│   ├── noise/
│   └── mitigation/
├── experiments/
│   ├── configs/
│   ├── scripts/
│   └── results/
├── report/
│   ├── figures/
│   └── draft.md
├── ai_prompts/
│   ├── code_review.md
│   ├── architecture_review.md
│   └── learning_checks.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
└── requirements.txt / environment.yml / pyproject.toml
