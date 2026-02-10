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

---

## Daily AI Check-In Loop (Mandatory)

Each execution day must include an explicit interaction with AI, following this sequence:

1. **Pre-coding check-in**
   - State the day number and exercise name.
   - Restate, in your own words, what you intend to implement.
   - Ask for confirmation that the scope is appropriate.

2. **Post-coding review**
   - After completing the coding task, present:
     - the code (or a summary and link)
     - the test status
   - Run the specified AI review prompt(s).
   - Request critique focused on correctness, design, and clarity.

3. **Commit confirmation**
   - State the exact commit message you intend to use.
   - Confirm whether the changes align with the week’s goals.

This daily interaction is considered part of the task completion.
