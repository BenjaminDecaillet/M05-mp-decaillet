# Quick Start
<!-- -------------------------------------------------- -->

From command line:

1. start your virtual environment: `conda activate m05-mp-decaillet`
   - initial setup described below
2. run **main.py**: `decm05`
   - for additional options, run `decm05 --help` (i.e: `decm05 --dataset=boston --dataset-source=file --preprocessor-type=standard --estimator=decision-tree`)

<!-- -------------------------------------------------- -->

## Installation

### Setup virtual environment

This quick-start.md chooses conda as an environment manager and assumes a functional Python development environment:

- [miniconda](https://docs.conda.io/en/latest/miniconda.html)

Create the virtual environment as follows:

```bash
git clone https://github.com/master-ai-batch5/M05-mp-decaillet.git decm05
cd decm05
conda env create -f environment.yml
conda activate m05-mp-decaillet
pip install --extra-index-url https://test.pypi.org/simple decm05
```