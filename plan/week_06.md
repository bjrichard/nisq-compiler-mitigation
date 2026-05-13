# QC Transition Plan — Week 06
**File:** `week_06.md`  
**Theme:** Experiment configuration, reproducibility, and report-ready workflow cleanup

This week turns the growing experiment scripts into a more systematic workflow. The goal is to reduce hardcoded parameters, improve reproducibility, and prepare the project for report-quality analysis.

---

## Day 1 — Centralized Experiment Configuration

### 1. Concepts to Learn
- Configuration objects
- Immutable dataclasses
- Reproducible experiment defaults

### 2. Concrete Coding Task
**Exercise name:** `experiment_config`

Create a centralized experiment configuration module.

Implement:
- `ExperimentConfig`
- `DEFAULT_CONFIG`
- `NOISE_SWEEP_LEVELS`

### 3. Exact GitHub Deliverable
- `experiments/config.py`
- `tests/experiments/test_config.py`
- One experiment script updated to use centralized config

**Commit message**  
feat(experiments): add centralized experiment configuration

### 4. Exact AI Prompt(s) to Run After Coding
Review this centralized experiment configuration module for clarity and extensibility.

### 5. Optional Stretch Goal
- Refactor one additional script to use `DEFAULT_CONFIG`.

---

## Day 2 — Refactor Noise Sweep to Use Config

### 1. Concepts to Learn
- Removing duplicated parameters
- Keeping experiment scripts configurable
- Avoiding magic numbers

### 2. Concrete Coding Task
**Exercise name:** `config_refactor_noise_sweep`

Update the noise sweep experiment to use shared config values.

### 3. Exact GitHub Deliverable
- Updated `experiments/scripts/run_noise_sweep.py`
- Updated tests if needed

**Commit message**  
refactor(experiments): use shared config in noise sweep

### 4. Exact AI Prompt(s) to Run After Coding
Review this config refactor for clarity and reproducibility.

### 5. Optional Stretch Goal
- Add sweep repeat count to config.

---

## Day 3 — Result Path Utilities

### 1. Concepts to Learn
- Path management
- Avoiding repeated path construction
- Project-root utilities

### 2. Concrete Coding Task
**Exercise name:** `result_paths`

Create shared helpers for experiment result paths.

### 3. Exact GitHub Deliverable
- `experiments/paths.py`
- Tests for path construction
- One script refactored to use shared paths

**Commit message**  
feat(experiments): add shared result path utilities

### 4. Exact AI Prompt(s) to Run After Coding
Review this result path utility design for clarity and portability.

### 5. Optional Stretch Goal
- Add separate constants for CSV and figure output paths.

---

## Day 4 — Result Summary Utility

### 1. Concepts to Learn
- Small reporting helpers
- Separating computation from display
- Experiment readability

### 2. Concrete Coding Task
**Exercise name:** `result_summary`

Create a helper for printing or formatting experiment summaries.

### 3. Exact GitHub Deliverable
- Shared helper module or function
- Tests for formatting behavior
- One script refactored to use it

**Commit message**  
feat(experiments): add result summary helper

### 4. Exact AI Prompt(s) to Run After Coding
Review this result summary helper for clarity and usefulness.

### 5. Optional Stretch Goal
- Return formatted strings instead of printing directly.

---

## Day 5 — Week 6 Cleanup Pass

### 1. Concepts to Learn
- Architecture review
- Reducing duplication
- Commit hygiene

### 2. Concrete Coding Task
**Exercise name:** `week_06_cleanup`

Review experiment scripts and make one small cleanup that improves consistency without changing behavior.

### 3. Exact GitHub Deliverable
- One cleanup/refactor commit
- All tests passing

**Commit message**  
refactor(experiments): clean up experiment workflow consistency

### 4. Exact AI Prompt(s) to Run After Coding
Review the Week 6 experiment workflow for consistency and report readiness.

### 5. Optional Stretch Goal
- Add a short `experiments/README.md`.

---

## End-of-Week Checkpoint

By the end of Week 6, the repository must contain:
- centralized experiment configuration
- reduced hardcoded parameters
- cleaner result path handling
- more consistent experiment scripts
- all tests passing
- experiment workflow ready for report drafting

---

## Next Step

Week 7 will focus on report structure, figure selection, and turning the experiment pipeline into a coherent technical narrative.
