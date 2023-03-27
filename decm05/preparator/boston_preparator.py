import pandas as pd

from decm05.preparator import BasePreparator


class BostonPreparator(BasePreparator):
    def __init__(self, file_or_url: str):
        if file_or_url == 'file':
            sources = ['decm05/data/housing.data']
        else:
            sources = ['https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data']
        features_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                          'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        targets_names = ['MEDV']
        super().__init__(sources, features_names, targets_names, delim_whitespace=True, names=features_names + targets_names)

    @property
    def name(self) -> str:
        return "boston"
