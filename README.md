NISQ Compiler Mitigation

A minimal quantum experimentation framework exploring how compilation structure, readout noise, and measurement error mitigation jointly affect observable outcome distributions in small quantum circuits.

This project was developed as part of a structured quantum computing and software engineering transition program focused on:

* clean Python architecture
* compiler abstractions
* reproducible experimentation
* technical reporting
* disciplined AI-assisted development

⸻

Current project status

Current implemented components include:

* circuit IR abstractions (Qubit, Gate, Circuit)
* compiler-pass infrastructure and pass manager
* circuit optimization passes
* single-qubit statevector simulation
* readout noise modeling
* confusion-matrix-based mitigation
* experiment workflows and CSV result generation
* visualization scripts
* technical report drafting

Current experiments include:

* readout noise sweep experiments
* deterministic versus superposition circuit comparisons
* compilation comparison experiments

⸻

Repository structure

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

⸻

Key experiments

Noise sweep experiment

Studies how increasing readout flip probability affects:

* noisy measurement error
* mitigated measurement error

Outputs:

* CSV results
* visualization plot

Circuit comparison experiment

Compares:

* deterministic measurement circuits
* probabilistic superposition circuits

Demonstrates how readout mitigation behaves under different probability distributions.

Compilation comparison experiment

Compares:

* unoptimized circuits
* optimized circuits after compiler passes

Demonstrates that compiler transformations preserve ideal behavior while reducing gate count.

Under the current readout-only noise model, compilation depth reduction does not substantially affect observed error, motivating future gate-level noise modeling.

⸻

Technical report

Current report draft:

report/draft.md

The report includes:

* methodology
* experiment descriptions
* quantitative interpretation
* limitations
* future work discussion

⸻

Installation

Create and activate the project environment:

conda create -n qc_compiler_em python=3.11
conda activate qc_compiler_em

Install development dependencies:

pip install -r requirements.txt

⸻

Running experiments

Example:

python -m experiments.scripts.run_noise_sweep

Other experiment scripts are located in:

experiments/scripts/

⸻

Running tests

pytest

⸻

AI-assisted development

AI tools were used for:

* planning
* code review prompts
* debugging support
* learning reinforcement
* architecture discussion

Final implementation decisions and validation were performed manually.

⸻

Current limitations

The current framework intentionally prioritizes transparency and educational value over realism and scale.

Current limitations include:

* single-qubit simulation only
* readout-only noise modeling
* limited compilation passes
* simplified mitigation workflow

Future work includes:

* multi-qubit simulation
* gate-level noise
* correlated errors
* deeper compilation benchmarking
* larger experiment workflows
