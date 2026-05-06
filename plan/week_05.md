# QC Transition Plan — Week 05
**File:** `week_05.md`  
**Theme:** Statevector sampling and non-trivial readout mitigation demos

This week moves beyond deterministic measurement-only circuits by adding a minimal single-qubit statevector simulator and using it to support experiments with meaningful quantum behavior.

---

## Day 1 — Single-Qubit Statevector Simulator

### 1. Concepts to Learn
- Statevector representation
- Single-qubit gate action
- Measurement sampling from probabilities

### 2. Concrete Coding Task
**Exercise name:** `single_qubit_statevector`

Implement a minimal single-qubit statevector simulator supporting:
- `X`
- `Z`
- `H`
- `MEASURE`

### 3. Exact GitHub Deliverable
- `src/qc_compiler/execution/statevector.py`
- Updated `execution/__init__.py`
- Tests in `tests/execution/test_statevector.py`

**Commit message**  
feat(execution): add single-qubit statevector simulator

### 4. Exact AI Prompt(s) to Run After Coding
Review this single-qubit statevector simulator for correctness, scope control, and future extensibility.

### 5. Optional Stretch Goal
- Add tests for unsupported gates.

---

## Day 2 — Statevector Readout Mitigation Demo

### 1. Concepts to Learn
- Ideal statevector sampling
- Readout noise applied to sampled bitstrings
- Separation between generic readout demos and statevector demos

### 2. Concrete Coding Task
**Exercise name:** `statevector_readout_mitigation_demo`

Create a separate demo script for statevector-based readout mitigation.

### 3. Exact GitHub Deliverable
- `experiments/scripts/run_statevector_readout_mitigation_demo.py`
- Tests in `tests/experiments/test_run_statevector_readout_mitigation_demo.py`
- `MeasurementNoiseModel.apply_to_bitstring`

**Commit message**  
feat(experiments): add statevector readout mitigation demo

### 4. Exact AI Prompt(s) to Run After Coding
Review this statevector readout mitigation demo for correctness, clarity, and architecture.

### 5. Optional Stretch Goal
- Compare output against the measurement-only demo.

---

## Day 3 — Compare Deterministic and Superposition Circuits

### 1. Concepts to Learn
- Distribution comparison
- Deterministic vs probabilistic measurement
- Error metrics for non-trivial ideal distributions

### 2. Concrete Coding Task
**Exercise name:** `compare_circuit_types`

Create an experiment comparing:
- measurement-only circuit
- `H` then measurement circuit

### 3. Exact GitHub Deliverable
- New experiment script or extension to existing demo
- Tests for helper functions

**Commit message**  
feat(experiments): compare deterministic and superposition mitigation cases

### 4. Exact AI Prompt(s) to Run After Coding
Review this comparison experiment for clarity and usefulness.

### 5. Optional Stretch Goal
- Save comparison results to CSV.

---

## Day 4 — Save Statevector Mitigation Results

### 1. Concepts to Learn
- Reproducible experiment outputs
- CSV result storage
- Result hygiene

### 2. Concrete Coding Task
**Exercise name:** `statevector_results_csv`

Save statevector mitigation experiment outputs to CSV.

### 3. Exact GitHub Deliverable
- CSV output in `experiments/results/`
- Updated experiment script
- Tests for result-writing helper

**Commit message**  
feat(experiments): save statevector mitigation results to CSV

### 4. Exact AI Prompt(s) to Run After Coding
Review this results workflow for reproducibility and clarity.

### 5. Optional Stretch Goal
- Include shot count and seed in output.

---

## Day 5 — Plot Statevector Mitigation Results

### 1. Concepts to Learn
- Visualization of distributions
- Report-ready plotting
- Interpreting mitigation behavior

### 2. Concrete Coding Task
**Exercise name:** `statevector_results_plot`

Generate a simple plot comparing ideal, noisy, and mitigated distributions.

### 3. Exact GitHub Deliverable
- Plot script or extension to existing plot workflow
- Figure saved in `experiments/results/`
- Optional test for CSV loading

**Commit message**  
feat(experiments): plot statevector mitigation results

### 4. Exact AI Prompt(s) to Run After Coding
Review this visualization for clarity and report readiness.

### 5. Optional Stretch Goal
- Add the figure to `report/figures/`.

---

## End-of-Week Checkpoint

By the end of Week 5, the repository must contain:
- A minimal single-qubit statevector simulator
- A statevector-based readout mitigation demo
- Clear separation between readout-only and statevector workflows
- Saved results for non-trivial quantum behavior
- At least one plot suitable for later report use

---

## Next Step

Week 6 will focus on:
- cleaner experiment configuration
- report-ready analysis
- comparing multiple circuits and noise strengths
