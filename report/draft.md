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

### 5.1 Noise sweep experiment

The noise sweep experiment evaluated how increasing readout flip probability affected observed measurement error before and after mitigation.

As expected, noisy error increased as the readout flip probability increased. At low noise levels, mitigation substantially reduced the observed error and recovered probabilities close to the ideal distribution.

However, mitigation performance degraded as the flip probability approached `0.5`. This behavior is expected because the confusion matrix becomes nearly singular near this limit, making the inverse correction numerically unstable.

Overall, the experiment demonstrates that simple confusion-matrix-based mitigation can effectively reduce readout bias when noise levels remain moderate.

### 5.2 Deterministic versus superposition circuits

The circuit comparison experiment evaluated two circuit types:
- a deterministic measurement circuit
- a superposition circuit created using the `H` gate

The deterministic circuit ideally produces a single measurement outcome with probability near `1.0`, while the superposition circuit ideally produces approximately equal probabilities for `0` and `1`.

The results showed that mitigation improved both circuit types, but the superposition experiment provided a more informative demonstration of probabilistic quantum behavior. Because the ideal distribution is not concentrated entirely on one bitstring, the superposition circuit better illustrates how readout noise distorts measurement probabilities.

This experiment also demonstrated that the statevector simulation workflow integrates cleanly with the mitigation pipeline.

### 5.3 Compilation comparison experiment

The compilation comparison experiment evaluated an unoptimized circuit containing redundant adjacent inverse gates and compared it against an optimized circuit produced by `CancelAdjacentInversesPass`.

The unoptimized circuit:

    X X H MEASURE

was reduced to:

    H MEASURE

after compilation.

The experiment confirmed that compilation reduced circuit gate count while preserving the ideal output distribution. Under the current readout-only noise model, the noisy and mitigated errors remained similar between the two circuits.

This result is important because it demonstrates a limitation of the current experimental framework. Since the noise model only affects measurement outcomes and does not model gate-level physical noise, reducing circuit depth does not significantly change the observed error.

This naturally motivates future work involving:
- gate-level noise
- decoherence models
- depth-sensitive error accumulation
- multi-qubit experiments

### 5.4 Overall interpretation

Taken together, the experiments demonstrate that:
- measurement error mitigation can substantially reduce readout bias
- statevector simulation provides a useful framework for probabilistic circuit experiments
- compilation passes can simplify circuit structure while preserving ideal behavior
- the current framework is strongly sensitive to readout noise but not yet sensitive to circuit depth

These results establish a foundation for future experiments involving more realistic noise and larger circuit systems.

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
