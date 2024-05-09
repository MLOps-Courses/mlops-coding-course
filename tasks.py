"""Tasks for the project."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task
from pathlib import Path
import shutil

# %% TASKS


@task
def install(ctx: Context) -> None:
    """Install the project."""
    ctx.run("poetry install")


@task
def reset(ctx: Context) -> None:
    """Reset the installation."""
    ctx.run("rm -rf .venv/")
    ctx.run("rm -f poetry.lock")


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
    ctx.run("poetry run mkdocs gh-deploy --force")


@task(pre=[build])
def assist(ctx: Context) -> None:
    """Gather content for assistant."""
    source_folder = Path("site")
    destination_folder = Path("assistant")
    ctx.run(f"rm -f {destination_folder}/*.html")
    for source_file in source_folder.rglob("*.html"):
        destination_path = source_file.relative_to(source_folder)
        if source_file.parent == source_folder:
            destination_name = destination_path.name # do not include parent name
        else:
            destination_name = f"{destination_path.parent} - {destination_path.name}"
        destination_file = destination_folder / destination_name
        print(f"{source_file} -> {destination_file}")
        shutil.copy(source_file, destination_file)


