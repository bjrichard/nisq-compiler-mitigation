# NISQ Compiler Mitigation

A minimal research-style quantum experimentation framework exploring how compilation structure, readout noise, and measurement error mitigation jointly affect observable outcome distributions in small quantum circuits.

The project combines:
- compiler abstractions
- statevector simulation
- readout noise modeling
- measurement error mitigation
- reproducible experiments
- technical reporting

The repository was developed as part of a structured transition program focused on quantum computing, software engineering, and research-oriented technical communication.

This project was developed as part of a structured quantum computing and software engineering transition program focused on:
- clean Python architecture
- compiler abstractions
- reproducible experimentation
- technical reporting
- disciplined AI-assisted development

---

## Why this project exists

Many quantum computing tutorials focus on isolated concepts or notebook-style demonstrations. This project instead emphasizes:
- reusable architecture
- experiment reproducibility
- transparent implementation
- technical interpretation
- disciplined iteration

The goal is not to compete with production quantum SDKs, but to build a minimal framework that clearly demonstrates the interaction between:
- compilation
- probabilistic execution
- readout noise
- mitigation workflows
- quantitative experiment analysis

---

## Current project status

Current implemented components include:
- circuit IR abstractions (`Qubit`, `Gate`, `Circuit`)
- compiler-pass infrastructure and pass manager
- circuit optimization passes
- single-qubit statevector simulation
- readout noise modeling
- confusion-matrix-based mitigation
- experiment workflows and CSV result generation
- visualization scripts
- technical report drafting

Current experiments include:
- readout noise sweep experiments
- deterministic versus superposition circuit comparisons
- compilation comparison experiments

---

## Key technical themes

This repository focuses on several core engineering and research themes:

| Theme | Current implementation |
|---|---|
| Circuit IR design | `Qubit`, `Gate`, and `Circuit` abstractions |
| Compilation | Pass manager and optimization passes |
| Simulation | Single-qubit statevector workflow |
| Noise modeling | Readout bit-flip noise |
| Mitigation | Confusion-matrix inversion |
| Experimentation | CSV generation and reproducible scripts |
| Reporting | Technical report and figure interpretation |

---

## Repository structure overview

The repository is organized to separate reusable source code, experiment workflows, generated artifacts, tests, and technical reporting.

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
```

---

## Key experiments

### Noise sweep experiment

Studies how increasing readout flip probability affects:
- noisy measurement error
- mitigated measurement error

Outputs:
- CSV results
- visualization plot

### Circuit comparison experiment

Compares:
- deterministic measurement circuits
- probabilistic superposition circuits

Demonstrates how readout mitigation behaves under different probability distributions.

### Compilation comparison experiment

Compares:
- unoptimized circuits
- optimized circuits after compiler passes

Demonstrates that compiler transformations preserve ideal behavior while reducing gate count.

Under the current readout-only noise model, compilation depth reduction does not substantially affect observed error, motivating future gate-level noise modeling.

---

## Technical report

Current report draft:

```text
report/draft.md
```

The report includes:
- methodology
- experiment descriptions
- quantitative interpretation
- limitations
- future work discussion

---

## Installation

Create and activate the project environment:

```bash
conda create -n qc_compiler_em python=3.11
conda activate qc_compiler_em
```

Install development dependencies:

```bash
pip install -r requirements.txt
```

---

## Running experiments

Example:

```bash
python -m experiments.scripts.run_noise_sweep
```

Other experiment scripts are located in:

```text
experiments/scripts/
```

---

## Running tests

```bash
pytest
```

---

## Reproducibility

Experiments use centralized configuration values defined in:

```text
experiments/config.py
```

Current defaults include:
- fixed random seeds
- standardized shot counts
- shared noise sweep levels

Generated experiment artifacts are stored in:

```text
experiments/results/
```

Primary experiment entry points:
- `run_noise_sweep.py`
- `run_circuit_comparison.py`
- `run_compilation_comparison.py`

---

## Report workflow

The technical report draft is maintained in:

```text
report/draft.md
```

The report references generated experiment artifacts stored in:

```text
experiments/results/
```

Recommended workflow:
1. run experiments
2. regenerate plots/results
3. update report interpretation
4. rerun tests

---

## AI-assisted development

AI tools were used for:
- planning
- code review prompts
- debugging support
- learning reinforcement
- architecture discussion

Final implementation decisions and validation were performed manually.

---

## Current project maturity

The current repository should be viewed as:
- a research-style prototype
- a software engineering learning project
- a reproducible experimentation framework
- a portfolio demonstration of architecture and technical communication skills

It is intentionally scoped smaller than a production quantum SDK.

---

## Current repository state

At the end of Week 9, the repository includes:
- reusable experiment infrastructure
- reproducible result generation
- visualization workflows
- a structured technical report
- documented limitations and future work
- portfolio-oriented project documentation

The remaining work is focused primarily on final polish, presentation quality, and optional future extensions.

---

## Current limitations

The current framework intentionally prioritizes transparency and educational value over realism and scale.

Current limitations include:
- single-qubit simulation only
- readout-only noise modeling
- limited compilation passes
- simplified mitigation workflow

Future work includes:
- multi-qubit simulation
- gate-level noise
- correlated errors
- deeper compilation benchmarking
- larger experiment workflows
