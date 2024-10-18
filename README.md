# Dating App with LLM Matcher

#### Install Python 3.12

```bash
# This works for macOS
> brew install pyenv
# The rest of the commands can work for both mac and linux)
> pyenv install 3.12
> vim  ~/.zshrc
# insert those lines
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
```

#### Create Virtual Environment

```bash
> pyenv local 3.12.2 # use python 3.12
> pip install poetry==1.8.2
> poetry env use -vv 3.12.2
> poetry shell # activate venv
```

#### Install Dev Dependencies

```bash
> poetry install -vvvv
> poetry show # show project packages
```

#### Run Dev Utils ( Linter, Formatter & Type Checker - configuration in pyproject.toml)

```bash
# Linter
> poetry run ruff check .
# Formatter
> poetry run ruff format .
# Type Checker
> poetry run mypy . --explicit-package-bases
```

#### Run Application

1. Navigate to `backend` where there are all the python modules
   Navigate to the parent directory of `backend` where the docker files.

```bash
poetry run python3 app.py
```
