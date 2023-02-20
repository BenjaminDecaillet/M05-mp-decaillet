# M05-mp-decaillet

Mini-project, as part of [module M05](https://moodle.fernuni.ch/course/view.php?id=3063) of [UniDistance's Master in AI](https://unidistance.ch/en/mathematics-and-computer-science/master-in-artificial-intelligence).

Mind the [accompanying slides](https://docs.google.com/presentation/d/1K4tIIJnhCY4eQcIWi5A6ZEol2mN5A6Cau0tL68QcjHY/edit?usp=sharing) (_access restrictions may apply_)

- [M05-mp-decaillet](#m05-mp-decaillet)
  - [Quick Start](#quick-start)
  - [Installation](#installation)
    - [Setup virtual environment](#setup-virtual-environment)
      - [OSX and Linux](#osx-and-linux)
      - [Windows](#windows)
  - [Unit tests](#unit-tests)

<!-- -------------------------------------------------- -->

## Quick Start

From command line:

1. start your [virtual environment](#setup-virtual-environment): `workon m05-mp-decaillet`
2. run [main.py](main.py): `python main.py`
3. [run unit tests](#unit-tests) locally.

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

## Unit tests
* activate your virtualenv: `workon subtitles-creator`
* run unit tests: `python -m unittest discover -v`

<!-- -------------------------------------------------- -->
