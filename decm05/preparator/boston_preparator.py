import pandas as pd

from decm05.preparator import BasePreparator


class BostonPreparator(BasePreparator):
    def __init__(self, source: str):
        if source == 'file':
            sources = ['data/housing.data']
        else:
            sources = ['https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data']
        features_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                          'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        targets_names = ['MEDV']
        super().__init__(sources, features_names, targets_names, delim_whitespace=True, names=features_names + targets_names)

    @property
    def name(self) -> str:
        return "boston"
