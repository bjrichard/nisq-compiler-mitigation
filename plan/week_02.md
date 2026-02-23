# QC Transition Plan — Week 02
**File:** `week_02.md`  
**Theme:** Compilation and Transpilation — compiler passes, sequential pipelines, simple optimizations, and native gate-set restriction

This week introduces the compilation layer. We move from defining a circuit intermediate representation to transforming it. All tasks must follow `00_project_overview.md`, `01_repo_and_tooling_setup.md`, and the master prompt.

Daily time cap: **45 minutes**

Each day must include:
- A concrete coding task
- Passing tests
- A commit
- A post-hoc AI review

---

## Day 1 — Compiler Pass Interface

### 1. Concepts to Learn
- Interface design for program transformations
- Returning new objects versus mutating in place
- Minimal abstraction for compilation passes

### 2. Concrete Coding Task (20–30 min)
**Exercise name:** `pass_interface`

Create a compiler pass base class in:

`src/qc_compiler/compilation/pass_base.py`

Requirements:
- Define `class CompilerPass`
- Include:
  - `name` property
  - `run(self, circuit: Circuit) -> Circuit`
- `run` must raise `NotImplementedError`
- Passes must return **new Circuit objects**, not mutate in place

Include full PEP-8 docstrings using the required template.

### 3. Exact GitHub Deliverable
- New file: `pass_base.py`
- Export `CompilerPass` in `compilation/__init__.py`
- Minimal test in `tests/compilation/test_pass_base.py` verifying `run()` raises `NotImplementedError`

**Commit message**  
feat(compilation): add compiler pass interface

### 4. Exact AI Prompt(s) to Run After Coding
Review this compiler pass interface for clarity and extensibility.  
Is returning a new circuit the correct architectural choice?  
List one potential limitation. Do not rewrite.

### 5. Optional Stretch Goal
- Add a `__repr__` method returning the pass name.

---

## Day 2 — Pass Manager (Sequential Pipeline)

### 1. Concepts to Learn
- Sequential transformation pipelines
- Composition over inheritance
- Deterministic transformation ordering

### 2. Concrete Coding Task (20–30 min)
**Exercise name:** `pass_manager`

Create:

`src/qc_compiler/compilation/pass_manager.py`

Implement `class PassManager`:

Requirements:
- Constructor takes `passes: list[CompilerPass]`
- Validate all entries are instances of `CompilerPass`
- Implement `run(self, circuit: Circuit) -> Circuit`
  - Sequentially apply passes
  - Output of one pass becomes input of next

### 3. Exact GitHub Deliverable
- New file: `pass_manager.py`
- Export in `compilation/__init__.py`
- Tests in `tests/compilation/test_pass_manager.py`
  - Define a dummy pass inside the test
  - Verify sequential execution order

**Commit message**  
feat(compilation): add PassManager for sequential compiler passes

### 4. Exact AI Prompt(s) to Run After Coding
Critique the PassManager design for realistic compiler usage.  
Are validations sufficient? Suggest one additional invariant. Do not rewrite.

### 5. Optional Stretch Goal
- Add a `__repr__` listing pass names in order.

---

## Day 3 — Optimization Pass: Cancel Adjacent Self-Inverse Gates

### 1. Concepts to Learn
- Peephole optimization
- Local rewrite rules
- Conservative correctness

### 2. Concrete Coding Task (20–30 min)
**Exercise name:** `cancel_adjacent_inverses`

Create directory:

`src/qc_compiler/compilation/passes/`

Add:

`cancel_inverses.py`

Implement `CancelAdjacentInversesPass(CompilerPass)`:

Behavior:
- If `X(q)` followed immediately by `X(q)`, remove both
- If `Z(q)` followed immediately by `Z(q)`, remove both
- Only cancel if:
  - Targets match exactly
  - Parameters are empty

Return a new `Circuit`.

### 3. Exact GitHub Deliverable
- New pass file
- Export in `compilation/passes/__init__.py`
- Tests in `tests/compilation/test_cancel_inverses.py`
  - Matching cancellation
  - Non-matching targets
  - Mixed gate names
  - Parametrized gates not canceled

**Commit message**  
feat(compilation): add pass to cancel adjacent self-inverse gates

### 4. Exact AI Prompt(s) to Run After Coding
Review this cancellation pass for correctness and edge cases.  
Is the matching logic too strict or too loose?  
Suggest one additional test. Do not rewrite.

### 5. Optional Stretch Goal
- Extend cancellation to additional self-inverse gate names.

---

## Day 4 — Compilation Metrics

### 1. Concepts to Learn
- Compiler instrumentation
- Quantitative comparison before and after passes

### 2. Concrete Coding Task (20–30 min)
**Exercise name:** `circuit_metrics`

Create:

`src/qc_compiler/compilation/metrics.py`

Implement:
- `gate_count(circuit: Circuit) -> int`
- `gate_counts_by_name(circuit: Circuit) -> dict[str, int]`
- `two_qubit_gate_count(circuit: Circuit) -> int`

Return defensive copies where appropriate.

### 3. Exact GitHub Deliverable
- New metrics module
- Tests in `tests/compilation/test_metrics.py`
  - Empty circuit
  - Mixed gates
  - Two-qubit gate count

**Commit message**  
feat(compilation): add basic circuit metrics

### 4. Exact AI Prompt(s) to Run After Coding
Critique these metrics functions for correctness and usefulness.  
What single additional metric would be most valuable next?  
Do not rewrite.

### 5. Optional Stretch Goal
- Add `depth(circuit: Circuit) -> int` assuming serial execution.

---

## Day 5 — Native Gate-Set Transpilation

### 1. Concepts to Learn
- Native gate-set restriction
- Gate decomposition
- Transpilation versus optimization

### 2. Concrete Coding Task (20–30 min)
**Exercise name:** `native_gate_set_transpile`

Create:

`src/qc_compiler/compilation/passes/native_gates.py`

Define a simple native gate set:

Allowed:
- `X`
- `Z`
- `RZ`
- `CX`

Implement `ToNativeGateSetPass(CompilerPass)`:

Rule:
- Replace `H(q)` with:
  - `RZ(q, theta=π/2)`
  - `X(q)`
  - `RZ(q, theta=π/2)`

Return a new `Circuit`.

### 3. Exact GitHub Deliverable
- New pass file
- Tests in `tests/compilation/test_native_gates.py`
  - `H(q)` rewrites into three gates
  - Native gates remain unchanged

**Commit message**  
feat(compilation): add pass to transpile H into native gate set

### 4. Exact AI Prompt(s) to Run After Coding
Review this native-gate transpilation pass.  
Is the decomposition rule encoded clearly and safely?  
List one edge case. Do not rewrite.

### 5. Optional Stretch Goal
- Run PassManager with cancellation + native pass on the example circuit and print before/after metrics.

---

## End-of-Week Checkpoint

By the end of Week 2, the repository must contain:
- A CompilerPass abstraction
- A PassManager
- At least one optimization pass
- Basic compilation metrics
- A native gate-set transpilation pass
- Passing tests
- AI prompts stored in `ai_prompts/`
- Structured commit history

---

## Next Step

Week 3 will introduce:
- Noise models (starting with measurement error)
- Confusion matrix generation
- Measurement error mitigation
- Quantitative comparison of compilation choices under noise
