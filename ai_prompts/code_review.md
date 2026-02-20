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
