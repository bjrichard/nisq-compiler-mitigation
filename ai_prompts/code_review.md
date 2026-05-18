# Qubit Review Prompt

Review this Qubit class for correctness, clarity, and future extensibility within a compilation and mitigation pipeline.

Specifically evaluate:
- Whether immutability is properly enforced
- Whether invariants are clearly defined and validated
- Whether equality semantics are appropriate
- Whether this abstraction will support compilation passes and qubit remapping later

Do not rewrite the implementation.
Provide critique only.

---

# Gate Review Prompt

Critique the Gate class design for later compilation passes and noise modeling.

List:
- structural strengths
- potential weaknesses
- edge cases
- suggested additional tests

Do not rewrite the implementation.
Provide critique only.

---

# Circuit Review Prompt

- Review this Circuit class as an IR for compilation passes.
- Evaluate invariants, mutability choice, and API clarity.
- Suggest edge cases and tests.

Do not rewrite the implementation.
Provide critique only.

---

# Example Script Review Prompt

- Does this example demonstrate the intended circuit application programming interface clearly?
- Is it minimal but realistic for later compilation passes?
- List any confusing naming or structure.

Do not rewrite the implementation.
Provide critique only.

---

# CompilerPass Design Review Prompt

Review this CompilerPass Protocol and CompilerPassBase design.

- Is primitive-only config enforcement appropriate?
- Is the separation between Protocol and Base clean?
- Are there missing elements required for a PassManager?

Do not rewrite the implementation.
Provide critique only.

---

# PassManager Review Prompt

Review this PassManager implementation for correctness and extensibility in a compiler pipeline.

Specifically evaluate:
- Whether pass validation is appropriate given a Protocol-based pass contract
- Whether sequential execution order is correct and clearly implemented
- Whether the API makes it easy to log pass names and configuration for reproducibility
- Whether error messages are clear for invalid passes and invalid circuit inputs

Suggest:
- One improvement
- One additional test case

Do not rewrite the implementation.
Provide critique only.

---

# Cancel Adjacent Inverses Pass Review Prompt

Review the CancelAdjacentInversesPass for correctness and edge cases.

Specifically evaluate:
- Whether the cancellation conditions are too strict or too loose
- Whether target matching logic is correct
- Whether parameter handling is safe
- Whether the pass correctly avoids mutating the input circuit

Suggest one additional test.

Do not rewrite the implementation.
Provide critique only.

---

# Compilation Metrics Review Prompt

Review these compilation metrics functions for correctness and usefulness.

Specifically evaluate:
- whether the metrics are well-defined
- whether edge cases are handled correctly
- whether the interfaces are clear for later benchmarking work

Suggest one additional metric that would be valuable next.

Do not rewrite the implementation.
Provide critique only.

---

# Benchmark Compilation Script Review Prompt

Review this benchmark script for clarity, correctness, and usefulness.

Specifically evaluate:
- whether the benchmark demonstrates the compiler pass clearly
- whether the printed metrics are sufficient for a first experiment
- whether the script structure is appropriate for future benchmarking work

Suggest one additional metric or output that would improve the script.

Do not rewrite the implementation.
Provide critique only.

---

# Noise Model Abstraction Review Prompt

Review this noise model abstraction for clarity, extensibility, and consistency with the compiler pass architecture.

Specifically evaluate:
- whether the Protocol and base class separation is appropriate
- whether the `apply(circuit)` interface is well chosen
- whether the naming and invariants are clear
- whether this design will support future concrete noise models cleanly

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Measurement Noise Model Review Prompt

Review this measurement noise model for clarity, correctness, and future extensibility.

Specifically evaluate:
- whether the `apply(circuit)` interface is appropriate
- whether inserting synthetic `READOUT_FLIP` gates is a reasonable first design
- whether edge cases around measurement handling are covered
- whether this model will integrate cleanly with future mitigation work

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Readout Sampling Review Prompt

Review these readout sampling utilities for clarity, correctness, and suitability for early measurement-noise experiments.

Specifically evaluate:
- whether the interpretation of READOUT_FLIP and MEASURE is internally consistent
- whether the interfaces are minimal but sufficient
- whether edge cases are covered appropriately
- whether this design will support confusion-matrix estimation later

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Confusion Matrix Review Prompt

Review this confusion matrix implementation for correctness and clarity.

Specifically evaluate:
- whether the mapping between flip probability and matrix entries is correct
- whether the interface is appropriate for later mitigation use
- whether the representation (dict vs array) is sufficient

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Readout Mitigation Review Prompt

Review this single-qubit readout error mitigation implementation for correctness, numerical stability, and architectural clarity.

Specifically evaluate:
- whether the 2x2 matrix inversion logic is correct
- whether singular-matrix handling is appropriate
- whether `mitigate_single_qubit_counts` correctly maps observed counts to mitigated probabilities
- whether the interfaces are suitable for later extension to multi-qubit mitigation

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Multi-Shot Sampling Review Prompt

Review these multi-shot sampling utilities for clarity, correctness, and architectural placement.

Specifically evaluate:
- whether `sample_counts` is implemented correctly
- whether repeated sampling is handled cleanly
- whether the `execution` module is the right home for this functionality
- whether the interface is appropriate for later experiment and mitigation work

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Readout Mitigation Demo Review Prompt

Review this readout mitigation demo for clarity, correctness, and usefulness as a first end-to-end experiment.

Specifically evaluate:
- whether the ideal, noisy, and mitigated stages are clearly separated
- whether noisy counts are sampled correctly on a per-shot basis
- whether the demo accurately illustrates the value of mitigation
- whether the helper functions are appropriately scoped

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Noise Sweep Experiment Review Prompt

Review this noise sweep experiment for clarity and correctness.

Specifically evaluate:
- whether the experimental design properly varies noise levels
- whether error metrics are meaningful
- whether the comparison between noisy and mitigated results is clear
- whether this is a strong basis for plotting and analysis

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Noise Sweep Results Review Prompt

Review this noise sweep results workflow for clarity, reproducibility, and usefulness for later analysis.

Specifically evaluate:
- whether CSV is an appropriate output format
- whether the saved fields are sufficient
- whether the experiment remains reproducible
- whether the workflow supports later plotting and reporting

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Noise Sweep Visualization Review Prompt

Review this visualization for clarity and effectiveness.

Specifically evaluate:
- whether the plot clearly communicates the difference between noisy and mitigated error
- whether axes and labels are appropriate
- whether this figure is suitable for a technical report
- whether any additional visual elements would improve interpretability

Suggest one improvement.

Do not rewrite the implementation.

Provide critique only.

---

# Single-Qubit Statevector Simulator Review Prompt

Review this single-qubit statevector simulator for correctness, scope control, and future extensibility.

Specifically evaluate:
- whether the implementations of `X`, `Z`, and `H` are mathematically correct
- whether measurement sampling from state probabilities is handled appropriately
- whether the simulator scope is clearly limited to single-qubit circuits
- whether this design can support later integration with noise and mitigation experiments

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Statevector Readout Mitigation Demo Review Prompt

Review this statevector readout mitigation demo for correctness, clarity, and architecture.

Specifically evaluate:
- whether statevector sampling and readout noise are integrated cleanly
- whether `MeasurementNoiseModel.apply_to_bitstring` belongs in the noise model layer
- whether the demo clearly separates ideal, noisy, and mitigated distributions
- whether this design preserves the general readout demo while adding a statevector-specific path

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Circuit Type Comparison Review Prompt

Review this deterministic versus superposition mitigation comparison experiment for correctness and clarity.

Specifically evaluate:
- whether the measurement-only and superposition cases are separated cleanly
- whether the error metric is meaningful for both cases
- whether statevector sampling is used appropriately for the superposition circuit
- whether this comparison is useful for the final project narrative

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Circuit Comparison Results Workflow Review Prompt

Review this CSV results workflow for deterministic and superposition circuit experiments.

Specifically evaluate:
- whether experiment results are organized clearly
- whether the CSV structure is appropriate for later plotting
- whether result persistence is handled cleanly
- whether this workflow supports future benchmarking extensions

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Circuit Comparison Visualization Review Prompt

Review this deterministic versus superposition visualization workflow for clarity and usefulness.

Specifically evaluate:
- whether the plotted comparison is easy to interpret
- whether the four plotted curves are appropriately labeled
- whether the figure communicates mitigation behavior clearly
- whether this visualization would work in a technical report

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Experiment Configuration Review Prompt

Review this centralized experiment configuration module for clarity and extensibility.

Specifically evaluate:
- whether configuration responsibilities are separated cleanly from experiment logic
- whether the dataclass design is appropriate
- whether immutable configuration is a good choice here
- whether this structure will scale to larger experiment workflows

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Noise Sweep Config Refactor Review Prompt

Review this noise sweep refactor for clarity, reproducibility, and maintainability.

Specifically evaluate:
- whether shared configuration is used appropriately
- whether duplicated parameters were reduced cleanly
- whether experiment defaults remain easy to understand
- whether this design will scale to larger experiment workflows

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Result Path Utilities Review Prompt

Review this shared result path utility module for clarity, portability, and maintainability.

Specifically evaluate:
- whether project-root detection is robust
- whether centralizing result paths improves experiment scripts
- whether the path constants are named clearly
- whether this approach will scale as more experiment outputs are added

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Result Summary Helper Review Prompt

Review this experiment result summary helper for clarity, usefulness, and maintainability.

Specifically evaluate:
- whether formatting logic is separated cleanly from experiment logic
- whether the helper is reusable across experiment scripts
- whether validation is appropriate
- whether the output format is readable for terminal summaries

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Experiment Validation Cleanup Review Prompt

Review this validation cleanup refactor for clarity and maintainability.

Specifically evaluate:
- whether validation responsibilities are separated appropriately
- whether the helper function is scoped correctly
- whether this cleanup improves consistency without overengineering
- whether the naming and error handling are clear

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.

---

# Technical Report Skeleton Review Prompt

Review this technical report skeleton for clarity, completeness, and alignment with the project goals.

Specifically evaluate:
- whether the report structure is logical
- whether the motivation is clear
- whether the methodology and experiment sections are appropriately separated
- whether the placeholders identify the right material to fill in next

Suggest one improvement.

Do not rewrite the report.
Provide critique only.

---

# Methodology Section Review Prompt

Review this methodology section for technical clarity, accuracy, and alignment with the implemented codebase.

Specifically evaluate:
- whether the circuit representation is explained clearly
- whether the compilation framework is described accurately
- whether the execution and statevector paths are distinguished cleanly
- whether the readout noise and mitigation explanation is technically correct
- whether the experiment workflow is understandable to a technical reviewer

Suggest one improvement.

Do not rewrite the report.
Provide critique only.

---

# Compilation Comparison Experiment Review Prompt

Review this compilation-focused experiment for relevance to the project question and overall experiment quality.

Specifically evaluate:
- whether the experiment meaningfully connects compilation and mitigation
- whether the optimization pass is demonstrated clearly
- whether the result structure is understandable
- whether the experiment workflow is reproducible
- whether the benchmark is too trivial or appropriately scoped for the current project stage

Suggest one improvement.

Do not rewrite the implementation.
Provide critique only.
