"""Tasks for the project."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% TASKS


@task
def install(ctx: Context) -> None:
    """Install the project."""
    ctx.run("poetry install")


@task
def build(ctx: Context) -> None:
    """Build the documentation."""
    ctx.run("poetry run mkdocs build")


@task
def serve(ctx: Context) -> None:
    """Serve the documentation."""
    ctx.run("poetry run mkdocs serve")


@task
def deploy(ctx: Context) -> None:
    """Deploy the documentation."""
    ctx.run("poetry run mkdocs gh-deploy")
