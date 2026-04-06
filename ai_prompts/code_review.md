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
