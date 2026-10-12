---
description: This chapter covers advanced techniques to refine your MLOps workflows. Master design patterns, automation, CI/CD, and more to build robust and scalable ML systems.
---

# 5. Refining

Refining your MLOps practices is crucial for moving from experimental models to production-grade systems. This chapter focuses on enhancing the efficiency, reliability, and scalability of your projects. By mastering these techniques, you will streamline the entire development-to-deployment pipeline, improve code quality, automate repetitive work, and ensure consistency across all environments.

- **[5.0. Design Patterns](./5.0. Design Patterns.md)**: Master architectural blueprints to solve common MLOps challenges, creating scalable and maintainable systems.
- **[5.1. Task Automation](./5.1. Task Automation.md)**: Define one canonical task vocabulary with `mise`—including the `all` gate and a locked toolchain—so your terminal, hooks, and CI can never disagree.
- **[5.2. Pre-Commit Hooks](./5.2. Pre-Commit Hooks.md)**: Enforce code quality standards automatically before commits, ordering thin `lefthook` commands so formatting, secret scanning, and checks each run at the right moment.
- **[5.3. CI/CD Workflows](./5.3. CI-CD Workflows.md)**: Implement hardened CI/CD pipelines that call the same gate you run locally, and lint the workflows themselves with `actionlint` and `zizmor`.
- **[5.4. Software Containers](./5.4. Software Containers.md)**: Use containers to create consistent, portable environments, with a linted, pinned, non-root `Dockerfile`.
- **[5.5. AI/ML Experiments](./5.5. AI-ML Experiments.md)**: Effectively manage, track, and reproduce experiments to accelerate model development and innovation.
- **[5.6. Model Registries](./5.6. Model Registries.md)**: Leverage model registries to version, share, and manage your machine learning models systematically.

## Checkpoint: compare two tracked runs
Using the reference project's local data, run two training configurations through `mise run project:run training` with a documented parameter change between runs. Inspect both runs with `mise run mlflow:serve`; compare the changed parameter, duration, and stored model artifact, then evaluate both model versions on the same heldout data. You are ready when another reader could identify which run you prefer and reproduce your reason from the logged evidence. Does the better score justify the additional runtime? Do not change the champion alias until evaluation succeeds.

Record the registered model version from each training run. Evaluate each explicitly, replacing `1` with its version:

```bash
uv run bikes confs/evaluations.yaml --extras '{"job": {"alias_or_version": 1}}'
```

Compare each training run with its corresponding evaluation run. The default evaluator reads the case-sensitive `Champion` alias; it does not automatically evaluate the latest candidate.

Run `mise run project` for the connected workflow in `confs/pipeline.yaml`. Inspect `selected_params.json` in the tuning run and `tuning_run_id` in the training run. Confirm that evaluation and promotion reference the registered version returned by that training run. A rejected evaluation must leave the champion unchanged.
