# QC Transition Plan — Week 01
**File:** `week_01.md`  
**Theme:** Foundations — environment, repo structure, Python OOP basics, first quantum circuit abstractions

This week establishes the **engineering baseline** and introduces the **project-specific code**.  
All tasks must follow `00_project_overview.md`, `01_repo_and_tooling_setup.md`, and the master prompt.

---

## Day 1 — Repository & Environment Bootstrap

### 1. Concepts to Learn
- Python virtual environments (conceptual level)
- Repo-as-a-product mindset
- Minimal Python package structure
- Role of `__init__.py`

### 2. Concrete Coding Task (20–40 min)
**Exercise name:** `package_skeleton`

Create the initial Python package skeleton for the project.

Implement:
- `src/qc_compiler/__init__.py`
- empty subpackages:
  - `circuits/`
  - `compilation/`
  - `noise/`
  - `mitigation/`
  - `utils/`

Each subpackage must include an `__init__.py`.

No logic yet — structure only.

### 3. Exact GitHub Deliverable
- New directories and files under `src/qc_compiler/`
- No tests yet

**Commit message**  
feat(structure): initialize qc_compiler package skeleton

### 4. Exact AI Prompt(s) to Run After Coding
Review this repository structure for a small, research-oriented Python project.  
Is the package layout clean, idiomatic, and extensible?  
Do not suggest adding new features.

### 5. Optional Stretch Goal
- Add a short comment in `src/qc_compiler/__init__.py` describing the package purpose.

---

## Day 2 — Qubit Abstraction

### 1. Concepts to Learn
- Python classes and constructors
- Immutability vs mutability
- Representing physical vs logical entities

### 2. Concrete Coding Task (20–40 min)
**Exercise name:** `qubit_class`

Implement a `Qubit` class in:  
`src/qc_compiler/circuits/qubit.py`

Requirements:
- Unique integer index
- Equality comparison
- Clear `__repr__`

Include full PEP-8 docstring.

### 3. Exact GitHub Deliverable
- `src/qc_compiler/circuits/qubit.py`
- Update `circuits/__init__.py` to expose `Qubit`

**Commit message**  
feat(circuits): add Qubit abstraction

### 4. Exact AI Prompt(s) to Run After Coding
Review this Qubit class for clarity, correctness, and extensibility.  
Is the abstraction appropriate for later circuit and compilation work?  
Do not rewrite the code.

### 5. Optional Stretch Goal
- Add a simple unit test for equality in `tests/circuits/`.

---

## Day 3 — Gate Abstraction

### 1. Concepts to Learn
- Base classes
- Simple inheritance (conceptual)
- Representing operations vs data

### 2. Concrete Coding Task (20–40 min)
**Exercise name:** `gate_class`

Implement a `Gate` class in:  
`src/qc_compiler/circuits/gate.py`

Requirements:
- Name (string)
- Target qubits (list of `Qubit`)
- Optional parameters (dict)
- Validation of inputs

Use the required docstring template.

### 3. Exact GitHub Deliverable
- `src/qc_compiler/circuits/gate.py`
- Update `circuits/__init__.py`

**Commit message**  
feat(circuits): add Gate abstraction

### 4. Exact AI Prompt(s) to Run After Coding
Critique the Gate class design.  
Is it flexible enough for compilation passes and noise modeling later?  
Identify any missing edge cases.

### 5. Optional Stretch Goal
- Add a `__repr__` that prints gate name and qubit indices.

---

## Day 4 — Circuit Container

### 1. Concepts to Learn
- Composition over inheritance
- Managing ordered collections
- Minimal circuit IR design

### 2. Concrete Coding Task (20–40 min)
**Exercise name:** `circuit_container`

Implement a `Circuit` class in:  
`src/qc_compiler/circuits/circuit.py`

Requirements:
- Maintain ordered list of `Gate` objects
- Method to add a gate
- Method to return number of qubits used
- No execution or simulation yet

### 3. Exact GitHub Deliverable
- `src/qc_compiler/circuits/circuit.py`
- Update `circuits/__init__.py`

**Commit message**  
feat(circuits): add Circuit container abstraction

### 4. Exact AI Prompt(s) to Run After Coding
Evaluate this Circuit abstraction as an intermediate representation (IR).  
Is it minimal but sufficient for compilation and mitigation experiments?

### 5. Optional Stretch Goal
- Add a simple test ensuring gate order is preserved.

---

## Day 5 — First Integration & Sanity Checks

### 1. Concepts to Learn
- Integration vs unit thinking
- Public APIs
- Small end-to-end examples

### 2. Concrete Coding Task (20–40 min)
**Exercise name:** `circuit_construction_example`

Create a small example script:  
`experiments/scripts/build_simple_circuit.py`

The script should:
- Create 2–3 qubits
- Define a few gates
- Assemble a circuit
- Print a readable representation

No physics yet — structure only.

### 3. Exact GitHub Deliverable
- `experiments/scripts/build_simple_circuit.py`
- Minor refinements to existing classes if needed

**Commit message**  
feat(experiments): add simple circuit construction example

### 4. Exact AI Prompt(s) to Run After Coding
Does this example clearly demonstrate the intended usage of the circuit API?  
Is anything confusing or misleading for a new reader?

### 5. Optional Stretch Goal
- Add a short comment block explaining how this will feed into compilation next week.

---

## End-of-Week Checkpoint

By the end of Week 1, the repository must contain:
- A clean package skeleton
- `Qubit`, `Gate`, and `Circuit` abstractions
- At least one runnable example
- Daily commits with new executable code

No compilation, noise, or mitigation yet — **structure first**.

---

## Next Step

After completing Day 5 and committing all changes:

Generate **Week 2**: compilation and transpilation passes.

Do **not** move ahead until this week is fully complete.
