# https://just.systems/man/en/

# REQUIRES

rm := require("rm")
uv := require("uv")

# DEFAULTS

# display help information
default:
    @just --list

# TASKS

# clean the project
clean:
    rm -rf site/
    rm -rf .venv/
    rm -rf .mypy_cache/

# install the project
install:
    uv sync --all-groups

# build the documentation
build:
    uv run mkdocs build

# serve the documentation
serve:
    uv run mkdocs serve

# deploy the documentation
deploy:
    uv run mkdocs gh-deploy --force
