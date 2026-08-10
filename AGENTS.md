# AGENTS.md

Context and rules for AI agents working in this repository. Humans should start with `README.md`.

## Project overview

- **Name**: MLOps Coding Course — a MkDocs Material documentation site that teaches end-to-end MLOps in Python.
- **Published**: https://mlops-coding-course.fmind.dev via GitHub Pages (deployed by GitHub Actions).
- **No application code**: this repo builds a static site from Markdown in `docs/`.

## Setup & core commands

All work goes through `mise` (see `mise.toml`); git hooks (`lefthook.yml`) and CI call the same tasks. Run `mise tasks` for the full list.

- Gate: `mise run all` — `format`, then `check`, then `build`. This is exactly what CI runs; a change is not done until it passes.
- Install: `mise run install` — sync dependencies (`uv`) and install git hooks (`lefthook`).
- Format: `mise run format` — `dprint` for config/markup only; prose under `docs/` is intentionally not reformatted.
- Check: `mise run check` — runs `check:actions` (`actionlint` + `zizmor`), `check:build` (`mkdocs build --strict`, which catches broken links and bad config), `check:format` (`validate-pyproject`, `dprint check`, `uv lock --check`), `check:leaks` (`gitleaks`), `check:scan` (`trivy fs`), and `check:vuln` (`pip-audit`).
- Build: `mise run build` — `mkdocs build`; Serve locally: `mise run serve` (live reload).
- There is no `test` task: the repository is prose, and its only executable assertion is the strict site build that `check:build` already runs. Do not add a `test` alias that re-runs it.

## Conventions

- Content lives in `docs/`, one numbered folder per chapter; the sidebar order comes from the numeric filename prefixes (no explicit `nav:`), so keep prefixes consistent when adding pages.
- Each page follows a consistent What / Why / How question-and-answer structure.
- Numbered lists use `1.` for every item so rendering stays dynamic; `docs/**` is excluded from `dprint` so prose formatting is preserved.
- Teach the current canonical stack: `uv`, Ruff, `ty`, `pytest`, `mise`, `lefthook`, `dprint`, `git-cliff`, MLflow 3, Docker, Python 3.14. Keep tool versions and examples in sync with the [cookiecutter-mlops-package](https://github.com/fmind/cookiecutter-mlops-package) and [mlops-python-package](https://github.com/fmind/mlops-python-package).
- Tool versions are pinned in `mise.toml` and locked in `mise.lock`; Python dependencies are locked in `uv.lock`. Both lockfiles are committed and `check:format` fails if `uv.lock` drifts from `pyproject.toml`.
- Commits: Conventional Commits; no attribution. Releases use `git-cliff`.

## Repository layout

- `docs/` — course chapters (`0. Overview` → `7. Observability`), `assets/`, and `CNAME` (custom domain, copied into the built site).
- `mkdocs.yml` — site configuration (Material theme, `strict: true`); `pyproject.toml` — mkdocs dependencies and the `dev` dependency group (`uv`, `package = false`).
- `mise.toml` / `mise.lock` — tasks and pinned tools; `lefthook.yml` — git hooks; `dprint.jsonc` — config/markup formatter; `trivy.yaml` — scanner policy; `cliff.toml` — changelog.

## GitHub configuration

Every file under `.github/` and what it does:

- `workflows/ci.yml` — runs `mise run all` on pushes to `main` and on every pull request, then asserts the working tree is unchanged.
- `workflows/pages.yml` — builds the site and deploys it to GitHub Pages on pushes to `main`.
- `workflows/security.yml` — weekly (and manual) full-history `gitleaks` and full-checkout `trivy` scan; the push-triggered checks only see recent commits.
- `workflows/assign.yml` — assigns newly opened issues to `fmind`. Issues only: a fork pull request gets a read-only token, so a `pull_request` trigger would fail on every external contribution.
- `dependabot.yml` — weekly grouped minor/patch updates for the `uv` and `github-actions` ecosystems, prefixed `chore(deps)`.
- `zizmor.yml` — relaxes `unpinned-uses` to `ref-pin`, because actions are deliberately pinned to major-version tags.
- `FUNDING.yml` — GitHub Sponsors link.

## Definition of done

A change is complete only when it answers the original request, fixes root causes rather than masking symptoms, comments the reasoning at any non-obvious choice, keeps `AGENTS.md` and `README.md` in sync with what the repository actually does, and passes `mise run all` warning-free. Never weaken a check to make the gate green. Do not commit, push, or tag unless the user asks.
