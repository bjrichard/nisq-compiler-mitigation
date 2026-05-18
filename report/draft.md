# How compilation, readout noise, and mitigation affect small quantum circuits

## Abstract

This technical note studies how simple readout noise affects observable output distributions in small quantum circuits, and how confusion-matrix-based measurement error mitigation can partially recover ideal behavior. The project implements a minimal Python pipeline for circuit representation, sampling, readout noise modeling, mitigation, experiment execution, and visualization.

## 1. Motivation

Near-term quantum devices are noisy. Even when a circuit is conceptually simple, measurement errors can distort observed outcome distributions. For candidates entering the quantum computing industry, understanding this pipeline is important because practical quantum software often sits between ideal circuit descriptions and noisy hardware behavior.

This project asks:

> How do quantum compilation choices, readout noise, and measurement error mitigation affect observable outcome distributions in small quantum circuits?

## 2. Project scope

This project intentionally uses a minimal implementation rather than a full quantum SDK.

Current scope:
- single-qubit and simple circuit abstractions
- basic compiler-pass infrastructure
- measurement readout noise
- single-qubit statevector simulation
- confusion-matrix-based readout mitigation
- reproducible experiment scripts
- CSV results and plots

Out of scope for the current version:
- full multi-qubit statevector simulation
- hardware-calibrated noise models
- gate-level physical noise
- comparison against production SDK implementations

## 3. Methodology

### 3.1 Circuit representation

Placeholder: describe `Qubit`, `Gate`, and `Circuit`.

### 3.2 Compilation framework

Placeholder: describe `CompilerPass`, `BaseCompilerPass`, and `PassManager`.

### 3.3 Readout noise model

Placeholder: describe measurement bit-flip noise.

### 3.4 Statevector simulation

Placeholder: describe single-qubit statevector simulator supporting `X`, `Z`, and `H`.

### 3.5 Measurement error mitigation

Placeholder: describe confusion matrix construction, inversion, and corrected probabilities.

## 4. Experiments

### 4.1 Noise sweep experiment

Placeholder: describe the noise sweep experiment and generated CSV/plot.

Figure placeholder:
`experiments/results/noise_sweep_plot.png`

### 4.2 Circuit comparison experiment

Placeholder: describe comparison between measurement-only and superposition circuits.

Figure placeholder:
`experiments/results/circuit_comparison_plot.png`

## 5. Results

Placeholder: summarize observed noisy error, mitigated error, and limitations at higher noise.

## 6. Limitations

Placeholder: discuss single-qubit scope, simplified noise model, finite sampling noise, and instability near singular confusion matrices.

## 7. Future work

Placeholder: describe possible extensions:
- multi-qubit statevector simulation
- correlated readout noise
- richer benchmark circuits
- configuration-driven experiment runners
- comparison with existing SDK behavior

## 8. Responsible AI usage

This project was developed with AI assistance for planning, code review, debugging, and learning checks. Core implementation decisions and final code review were performed manually. AI-generated suggestions were treated as proposals, not authoritative solutions.

## 9. Conclusion

Placeholder: summarize what the project demonstrates technically and professionally.
