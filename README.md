# python project template

This is a lightweight template project for python based on poetry, pre-commit, pytest and many other tools. All tool configuration is done within [pyproject.toml](pyproject.toml). Adapt it to your liking.

## [poetry](https://python-poetry.org/)

The following will create the virtual environment within the project directory in .../my-project/.venv. This allows vscode natively to find the virtual environment.

```
poetry config virtualenvs.in-project true
```

Installs all dependencies (if virtualenvs.in-project is set to true) to [.venv](.venv) within this repository location and creates a [pyproject.lock](pyproject.lock) file.

```
poetry install
```

## [pre-commit](https://pre-commit.com/)

Within [.pre-commit-config.yaml](.pre-commit-config.yaml) you can find all pre-commit hooks that are installed. Basically all code quality tools defined in [pyproject.toml](pyproject.toml) are installed as pre-commit hooks as well.

To install pre-commit git hooks, run the following:

```
poetry shell && pre-commit install
```

Run the following to run the pre-commit hooks:

```
pre-commit run --all-files
```

## [pytest](https://docs.pytest.org/en/stable/)

For all pytest markers and settings refer to [pyproject.toml](pyproject.toml).

```bash
poetry run python -m pytest tests/
```

## [vscode](https://code.visualstudio.com/)

If setup properly vscode will automatically use the virtual environment created by poetry. It will use the linting and formatting settings according to the [pyproject.toml](pyproject.toml). Therefore the behavior of your editor is the same as pre-commit. To do so, open the project folder in vscode and run the following command in the integrated terminal:

```
poetry shell
```

or start vs code from the terminal:

```
poetry run code .
```

Some basic extensions (focus on python):

```
code --install-extension donjayamanne.python-environment-manager
code --install-extension donjayamanne.python-extension-pack
code --install-extension KevinRose.vsc-python-indent
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension njpwerner.autodocstring
code --install-extension streetsidesoftware.code-spell-checker
```
