# M05-mp-decaillet

Mini-project, as part of [module M05](https://moodle.fernuni.ch/course/view.php?id=3063) of [UniDistance's Master in AI](https://unidistance.ch/en/mathematics-and-computer-science/master-in-artificial-intelligence).

Mind the [accompanying slides](https://docs.google.com/presentation/d/1K4tIIJnhCY4eQcIWi5A6ZEol2mN5A6Cau0tL68QcjHY/edit?usp=sharing) (_access restrictions may apply_)

- [M05-mp-decaillet](#m05-mp-decaillet)
  - [Quick Start](#quick-start)
  - [Installation](#installation)
    - [Setup virtual environment](#setup-virtual-environment)
      - [OSX and Linux](#osx-and-linux)
      - [Windows](#windows)
  - [Unit tests and coverage](#unit-tests-and-coverage)
  - [Linter](#linter)
    - [Reformat from command line](#reformat-from-command-line)
    - [VS-code settings](#vs-code-settings)
  - [Doc](#doc)
    - [Generate sphinx doc locally](#generate-sphinx-doc-locally)

<!-- -------------------------------------------------- -->

## Quick Start

From command line:

1. start your [virtual environment](#setup-virtual-environment): `workon m05-mp-decaillet`
2. run [main.py](main.py): `python main.py`
3. [run unit tests](#unit-tests-and-coverage) locally.

<!-- -------------------------------------------------- -->

## Installation

### Setup virtual environment

This README.md assumes a functional Python development environment with:

- [virtual environments](https://docs.python.org/3/library/venv.html)
- a virtualenv wrapper:
  - **OSX and Linux**: use package [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - **Windows**: use package [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/)

The project requires **Python 3.11.1**.

Create the virtualenv as follows:

#### OSX and Linux

```bash
rmvirtualenv m05-mp-decaillet
mkvirtualenv m05-mp-decaillet --python=/usr/local/bin/python3.11 -r requirements.txt
```

_NB: exact path to **python3.11** may vary; locate it with: `which python3.11`_

#### Windows

```cmd
rmvirtualenv m05-mp-decaillet
mkvirtualenv m05-mp-decaillet --python "%userprofile%\AppData\Local\Programs\Python\Python311\python.exe" -r requirements.txt 
```

_NB: exact path to **python3.11** may vary; locate it with: `where python` (Windows CMD) or `get-command python` (Windows PowerShell)_

<!-- -------------------------------------------------- -->

## Unit tests and coverage
* activate your virtualenv: `workon m05-mp-decaillet`
* run unit tests: `python -m unittest discover -v`
* run unit tests and display coverage report: `coverage run --source=src -m unittest -v  &&  coverage report -m`

[GitHub actions](.github/workflows/main.yml) will enforce unit-test coverage of 100%.

<!-- -------------------------------------------------- -->

## Linter

The python code in this project must match [autopep8](https://pypi.org/project/autopep8/) and [isort](https://pypi.org/project/isort/) linting/formatting rules.

[GitHub actions](.github/workflows/main.yml) will enforce these rules.

### Reformat from command line
* activate your virtualenv: `workon m05-mp-decaillet`
* apply autopep8 to all local files: `autopep8 --max-line-length=120 --recursive . -aaa --in-place`
* apply isort to all local files: `isort .`

### VS-code settings
In VS-code, the linting  can be automated as follows:
- Install extension [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (which is a [recommended extensions](.vscode/extensions.json))
- Edit your **User** Settings:
  - CMD + shift + P > "Preferences: Open User Settings (JSON)"
- Append the following to you User Settings:
  ```json
  "python.formatting.autopep8Args": [
      "--max-line-length=120"
  ],
  "[python]": {
      "editor.defaultFormatter": "ms-python.python",
      "editor.formatOnSave": true,
      "editor.codeActionsOnSave": {
          "source.organizeImports": true,
      },
  },
  ```

<!-- -------------------------------------------------- -->

## Doc

This projects uses [sphinx](https://www.sphinx-doc.org/en/master/) do generate its doc.

### Generate sphinx doc locally
* activate your virtualenv: `workon m05-mp-decaillet`
* build doc: `sphinx-build doc sphinx`
* open [sphinx/index.html](sphinx/index.html) in your web browser

<!-- -------------------------------------------------- -->