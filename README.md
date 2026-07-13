# NISQ Compiler Mitigation

A compact quantum experimentation framework for studying how quantum-circuit compilation, readout noise, and measurement-error mitigation interact to affect observed measurement distributions.

The framework includes:

- object-oriented circuit representations
- compiler-pass abstractions and optimization passes
- single-qubit statevector simulation
- configurable readout-noise model
- confusion-matrix-based measurement mitigation
- reproducible experiment pipelines
- automated tests and technical reporting

## Research question

How do circuit compilation, readout noise, and measurement-error mitigation jointly affect observed outcome distributions in small quantum circuits?

The experiments test whether compiler transformations alter noisy and mitigated outcomes under the project’s current readout-noise model.

## Motivation

Compilation, noise, and mitigation are often studied independently. This project provides a compact framework for testing how these layers interact within a single reproducible workflow.

The implementation is intentionally small enough to remain transparent while still separating circuit representation, compilation, execution, noise, mitigation, experimentation, and reporting.

## Key findings

Within the tested single-qubit, readout-noise setting:

- Measurement-error mitigation reduces distribution error across the tested readout-noise range.
- Mitigation behavior differs between deterministic and superposition-state measurement distributions.
- Compiler optimizations preserve ideal circuit behavior while reducing gate count.
- Under the current readout-only noise model, gate-count reduction does not materially reduce measurement error, highlighting the need for gate-level noise modeling in future work.

## Implemented components

| Area | Implementation |
|---|---|
| Circuit representation | `Qubit`, `Gate`, and `Circuit` abstractions |
| Compilation | Pass manager and circuit-optimization passes |
| Simulation | Single-qubit statevector simulation |
| Noise | Configurable readout bit-flip model |
| Mitigation | Confusion-matrix inversion |
| Experiments | Reproducible scripts, CSV outputs, and plots |
| Validation | Automated tests with `pytest` |
| Reporting | Technical report covering methods, results, and limitations |

## Quick start

From the repository root:

```bash
conda create -n qc_compiler_em python=3.11
conda activate qc_compiler_em
pip install -r requirements.txt

pytest
python -m experiments.scripts.run_noise_sweep
python -m experiments.scripts.save_circuit_comparison_results
python -m experiments.scripts.plot_circuit_comparison_results
python -m experiments.scripts.run_compilation_comparison
```

Generated results are written to:

[`experiments/results/`](experiments/results/)

## Repository structure

```text
src/qc_compiler/
    circuits/
    compilation/
    execution/
    mitigation/
    noise/
    simulation/

experiments/
    scripts/
    results/

tests/

report/

docs/
```

## Experiments

### Readout-noise sweep

Measures noisy and mitigated distribution error as the readout-flip probability increases.

### Circuit-distribution comparison

Compares mitigation behavior for deterministic and superposition-state circuits.

### Compilation comparison

Compares circuits before and after optimization passes, verifies preservation of ideal behavior, and measures changes in gate count.

Because the current model includes readout noise only, circuit-depth reduction does not materially change observed error. This result motivates future gate-level noise experiments.

## Reproducibility

Experiments use centralized configuration values defined in:

```text
experiments/config.py
```

Current defaults include:

- fixed random seeds
- standardized shot counts
- shared noise-sweep levels

Generated experiment artifacts are stored in:

[`experiments/results/`](experiments/results/)

Primary experiment entry points:

- `run_noise_sweep.py`
- `run_circuit_comparison.py`
- `run_compilation_comparison.py`

Recommended workflow:

1. Run the test suite.
2. Run or regenerate experiments.
3. Review generated CSV files and plots.
4. Update the technical report interpretation.
5. Rerun the test suite.

## Technical report

The technical report draft is maintained in:

[`report/draft.md`](report/draft.md)

It covers:

- methodology
- experiment design
- quantitative results
- interpretation
- limitations
- future work

## Limitations

The current implementation is intentionally scoped to:

- single-qubit statevector simulation
- readout-only noise
- independent bit-flip errors
- a limited set of compiler passes
- confusion-matrix-based mitigation

Future extensions could include multi-qubit simulation, gate-level and correlated noise, routing, noise-aware compilation, and comparison with established software development kits such as Qiskit or Cirq.

## Development process

This project was developed as part of a structured transition program focused on quantum computing, software engineering, and research-oriented technical communication.

AI-assisted tools supported planning, debugging, architecture review, and documentation. Final implementation decisions, validation, and interpretation were performed manually.

See [`docs/development_process.md`](docs/development_process.md) for additional detail.

## Repository guide

- `src/qc_compiler/` — reusable framework code
- `experiments/scripts/` — experiment entry points
- `experiments/results/` — generated CSV files and plots
- `tests/` — automated validation
- `report/draft.md` — methodology, results, and interpretation
- `docs/development_process.md` — development workflow, scope, and AI-assisted process
