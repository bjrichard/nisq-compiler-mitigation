# Week 03 — Compilation, Noise, and Readout Sampling

**Theme:** Compilation passes, noise modeling, and measurement interpretation

---

## Objectives

- Introduce compilation passes and pass manager abstraction
- Implement measurement noise model
- Build readout sampling utilities
- Establish the foundation for measurement error mitigation

---

## Deliverables

### Compilation

- CompilerPass Protocol
- BaseCompilerPass class with:
  - name validation
  - configuration handling
  - debug representation
- PassManager abstraction:
  - sequential pass execution
  - pass validation

---

### Noise Modeling

- NoiseModel Protocol
- BaseNoiseModel class
- MeasurementNoiseModel:
  - flip-probability–based readout noise
  - deterministic seeding support

---

### Readout Sampling

- `sample_readout(circuit)`:
  - interprets MEASURE and READOUT_FLIP gates
- `bitstring_from_readout(readout)`:
  - deterministic bitstring construction

---

## Key Design Decisions

- Separation of concerns:
  - compilation vs noise vs mitigation
- Noise modeled as circuit transformation
- Readout interpreted without full state simulation

---

## Tests

- Validation of pass behavior
- Validation of noise model correctness
- Validation of readout sampling logic

---

## Outcome

By the end of Week 3:

- Circuits can be compiled, noised, and sampled
- Measurement outcomes can be interpreted deterministically
- The system supports the next step: mitigation

---

## Notes

- Noise is currently modeled at the circuit level
- Stochastic behavior is introduced later at sampling time
