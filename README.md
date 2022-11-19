# python project template

This is a template project for python based on poetry, pre-commit, pytest and many other tools

## [poetry](https://python-poetry.org/)

The following will create the virtual environment within the project directory in .../my-project/.venv. This allows vscode to find the virtual environment.

```
poetry config virtualenvs.in-project true
```

## [pre-commit](https://pre-commit.com/)

To install pre-commit git hooks, run the following:

```
poetry shell && pre-commit install
```

Run the following to run the pre-commit hooks:

```
pre-commit run --all-files
```

## [vscode](https://code.visualstudio.com/)