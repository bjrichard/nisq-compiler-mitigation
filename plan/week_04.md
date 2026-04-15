# Week 04 — Sampling, Mitigation, and First Experiments

**Theme:** From sampling to distributions to mitigation

---

## Objectives

- Move from single-shot sampling to distributions
- Implement confusion matrix–based mitigation
- Build first end-to-end experiment
- Validate mitigation effectiveness

---

## Deliverables

### Execution Layer

- New module: `execution/`
- `sample_counts(circuit, shots)`:
  - multi-shot sampling
  - distribution generation

---

### Mitigation

- `single_qubit_confusion_matrix(p)`
- `confusion_matrix_from_model(model)`
- `invert_2x2_matrix(matrix)`
- `mitigate_single_qubit_counts(counts, matrix)`

---

### Experiment

- Script:
  `experiments/scripts/run_readout_mitigation_demo.py`

Pipeline:
circuit → noise → sampling → counts → mitigation → corrected probabilities

---

### Metrics

- Conversion of counts to probabilities
- Absolute error vs ideal distribution
- Comparison:
  - ideal
  - noisy
  - mitigated

---

## Key Design Decisions

- Introduced `execution/` as separate layer:
  - sampling ≠ noise
- Noise applied per shot in experiments
- Mitigation operates in probability space

---

## Tests

- Sampling correctness
- Confusion matrix validation
- Matrix inversion correctness
- Mitigation behavior under known conditions
- Experiment helper validation

---

## Outcome

By the end of Week 4:

- Full readout mitigation pipeline is implemented
- First empirical demonstration of mitigation is working
- System produces measurable results

---

## Notes

- Mitigation may produce non-physical probabilities (expected)
- Finite sampling introduces estimation error
- This sets up multi-experiment analysis in Week 5
