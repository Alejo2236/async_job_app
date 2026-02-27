# Async Job App

Async Job App is an asynchronous job processing system designed to manage computational tasks through a structured lifecycle.

The project focuses on building a clean orchestration architecture where jobs move through explicit states (pending, running, completed, failed, canceled), with controlled retry behavior and database-backed state persistence.

The primary goal of this project is to explore:

- Clear separation between API, orchestration, execution, and persistence layers
- Deterministic job lifecycle management
- Retry and cancellation strategies
- Process-based execution for CPU-bound tasks

This repository represents Version 1 of the system, centered on building a robust orchestration core.

*See more details on project "docs" folder.*
