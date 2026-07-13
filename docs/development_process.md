# Development process

## Purpose

This document records how the project was developed, including the role of AI-assisted tools, the validation process, and the boundaries of the current implementation.

The goal is transparency. AI tools supported the work, but they did not replace manual implementation, testing, or scientific interpretation.

## Project context

The repository was developed as part of a structured transition program focused on:

- quantum computing
- software engineering
- compiler abstractions
- reproducible experimentation
- scientific interpretation
- technical communication

The project was intentionally scoped as a small research framework rather than a production quantum software development kit.

## Development workflow

The project was developed iteratively:

1. Define a narrow technical or research objective.
2. Design or revise the relevant abstraction.
3. Implement the change manually.
4. Add or update tests.
5. Run the test suite.
6. Execute experiments where applicable.
7. Review outputs and revise the interpretation.
8. Document assumptions, limitations, and results.

This process was repeated across circuit abstractions, compiler passes, simulation, noise modeling, mitigation, experiment scripts, and reporting.

## Use of AI-assisted tools

AI tools were used for:

- planning development steps
- discussing software architecture
- generating review checklists
- debugging support
- suggesting test cases
- clarifying quantum-computing concepts
- reviewing documentation
- identifying edge cases
- reinforcing software-engineering practices

AI-generated suggestions were treated as proposals rather than authoritative answers.

## Manual responsibilities

The following remained manual responsibilities:

- deciding project scope
- choosing abstractions and interfaces
- implementing code
- reviewing generated or suggested code
- validating mathematical and physical assumptions
- running tests
- interpreting experiment results
- deciding whether outputs were scientifically meaningful
- documenting limitations
- approving final technical claims

## Validation

Validation relied on:

- automated tests with `pytest`
- reproducible experiment scripts
- fixed seeds and shared experiment configuration
- comparison of ideal, noisy, and mitigated distributions
- checks that compiler transformations preserved ideal behavior
- manual review of generated CSV files and plots

The project does not claim hardware validation or production-scale benchmarking.

## Scope boundaries

The current implementation is limited to:

- single-qubit statevector simulation
- readout-only noise
- independent bit-flip errors
- confusion-matrix-based mitigation
- a limited compiler-pass set

These constraints are deliberate. They keep the system small enough to inspect while making the interaction among compilation, noise, mitigation, and experiment design explicit.

## Limitations of the development process

The development process has several limitations:

- AI-assisted review can miss errors or reinforce incorrect assumptions.
- Passing tests does not establish physical realism.
- The current experiments do not model gate-level noise or correlated errors.
- The repository is a research and learning prototype, not a production software system.
- Results should be interpreted within the narrow assumptions documented in the code and report.

## Authorship and accountability

The project author is responsible for the final implementation, tests, experiment design, documentation, and interpretation.

AI-assisted tools contributed suggestions and review support, but final technical decisions and claims were made by the author.
