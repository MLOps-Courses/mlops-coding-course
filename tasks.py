"""Tasks of the project."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% TASKS


@task
def clean(ctx: Context) -> None:
    """Clean the project."""
    ctx.run("rm -rf site/")
    ctx.run("rm -rf .venv/")
    ctx.run("rm -rf .mypy_cache/")


@task
def install(ctx: Context) -> None:
    """Install the project."""
    ctx.run("uv sync --all-groups")


@task
def build(ctx: Context) -> None:
    """Build the documentation."""
    ctx.run("uv run mkdocs build")


@task
def serve(ctx: Context) -> None:
    """Serve the documentation."""
    ctx.run("uv run mkdocs serve")


@task
def deploy(ctx: Context) -> None:
    """Deploy the documentation."""
    ctx.run("uv run mkdocs gh-deploy --force")
