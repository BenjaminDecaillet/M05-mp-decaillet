# M05-mp-decaillet

Mini-project, as part of [module M05](https://moodle.fernuni.ch/course/view.php?id=3063) of [UniDistance's Master in AI](https://unidistance.ch/en/mathematics-and-computer-science/master-in-artificial-intelligence).

Mind the [accompanying slides](https://docs.google.com/presentation/d/1K4tIIJnhCY4eQcIWi5A6ZEol2mN5A6Cau0tL68QcjHY/edit?usp=sharing) (_access restrictions may apply_)

- [M05-mp-decaillet](#m05-mp-decaillet)
  - [Quick Start](#quick-start)
  - [Installation](#installation)
    - [Setup virtual environment](#setup-virtual-environment)

<!-- -------------------------------------------------- -->

## Quick Start

From command line:

1. start your [virtual environment](#setup-virtual-environment): `workon m05-mp-decaillet`
2. run [main.py](main.py): `python main.py`

<!-- -------------------------------------------------- -->

## Installation

### Setup virtual environment

This README.md assumes a functional Python development environment, as described [here](https://docs.python.org/3/library/venv.html).

The project requires Python 3.11.1 (exact path to **python3.11** may vary; locate it with: `which python3.11`)

```bash
rmvirtualenv m05-mp-decaillet
mkvirtualenv m05-mp-decaillet --python=/usr/local/bin/python3.11 -r requirements.txt
```

<!-- -------------------------------------------------- -->
