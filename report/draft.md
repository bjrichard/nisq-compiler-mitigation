# How compilation structure, readout noise, and measurement error mitigation jointly affect observable outcome distributions in small quantum circuits

## Abstract

This technical note studies how readout noise affects observable output distributions in small quantum circuits, and how confusion-matrix-based measurement error mitigation can partially recover ideal behavior. The project implements a minimal Python pipeline for circuit representation, compilation passes, statevector simulation, readout noise modeling, mitigation, experiment execution, and visualization.

## 1. Motivation

Near-term quantum devices are noisy. Even when a circuit is conceptually simple, measurement errors can distort observed outcome distributions. Understanding this pipeline is important because practical quantum software sits between ideal circuit descriptions and noisy hardware behavior.

This project asks:

> How do compilation structure, readout noise, and measurement error mitigation jointly affect observable outcome distributions in small quantum circuits?

The project emphasizes transparent implementations and reproducible experimentation rather than performance or feature completeness.

## 2. Project scope

This project intentionally uses a minimal implementation rather than a full quantum SDK.

Current scope:
- single-qubit and simple circuit abstractions
- compiler-pass infrastructure
- simple circuit rewriting passes
- measurement readout noise
- single-qubit statevector simulation
- confusion-matrix-based readout mitigation
- reproducible experiment scripts
- CSV results and plots

Out of scope for the current version:
- full multi-qubit statevector simulation
- hardware-calibrated noise models
- gate-level physical noise
- production-scale transpilation systems
- comparison against production SDK implementations

## 3. Methodology

### 3.1 Circuit representation

The project represents circuits using three core abstractions: `Qubit`, `Gate`, and `Circuit`. A `Qubit` identifies a logical qubit by index. A `Gate` stores the operation name, target qubits, and optional parameters. A `Circuit` stores an ordered sequence of gates.

This design intentionally keeps the intermediate representation minimal. The goal is not to reproduce a full quantum software development kit, but to build a transparent circuit representation that can support compilation passes, simulation, noise modeling, and mitigation experiments.

### 3.2 Compilation framework

Compilation behavior is organized around a pass-based architecture. A compiler pass implements a common interface and transforms one circuit into another. The `PassManager` runs passes sequentially, allowing circuit transformations to be composed into a pipeline.

The current implementation includes a simple optimization pass that cancels adjacent self-inverse gates. This provides a minimal example of a compiler transformation and establishes the structure needed for later compilation-focused experiments.

### 3.3 Execution and statevector simulation

The project includes two execution paths.

The first path samples measurement outcomes directly from circuits containing measurement-related operations. This path is useful for testing readout behavior and preserving a workflow that can later extend to multi-qubit circuits.

The second path uses a minimal single-qubit statevector simulator. The simulator starts in the state |0⟩ and supports the gates `X`, `Z`, and `H`. Measurement outcomes are sampled from the resulting state probabilities. This makes it possible to study probabilistic quantum behavior, such as the distribution produced by applying `H` before measurement.

### 3.4 Readout noise model

Readout noise is modeled as a classical bit-flip process. For a single measured bit, the noise model flips the observed outcome with probability `p` and preserves it with probability `1 - p`.

The corresponding confusion matrix is:

    [[1 - p, p],
     [p, 1 - p]]

Each row represents the true bit value, and each column represents the observed bit value. This model is intentionally simple, but it captures the core behavior needed to study measurement error mitigation.

### 3.5 Measurement error mitigation

Measurement error mitigation is implemented by inverting the single-qubit confusion matrix and applying it to the observed probability vector.

If the observed distribution is:

    p_observed = [P_observed(0), P_observed(1)]

and the confusion matrix is `M`, the mitigated estimate is computed as:

    p_mitigated = M^{-1} p_observed

This approach can reduce readout bias when the noise level is moderate. However, as the flip probability approaches `0.5`, the confusion matrix becomes singular or nearly singular, making the inversion unstable. This limitation is important for interpreting the results.

### 3.6 Experiment workflow

Experiments follow a common workflow:

    build circuit → sample ideal outcomes → apply readout noise → mitigate counts → save results → plot results

Configuration values such as shot count, noise levels, and random seeds are centralized in `experiments/config.py`. Output paths are centralized in `experiments/paths.py`. This keeps experiment scripts more reproducible and easier to maintain.

Current experiments include:
- a noise sweep comparing noisy and mitigated error
- a deterministic versus superposition circuit comparison
- visualizations saved as project artifacts

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
