import pandas as pd

from src.preparator import Preparator


class RedWinePreparator(Preparator):
    def __init__(self, source: str):
        if source == 'file':
            self._source = 'data/winequality-red.csv'
        else:
            self._source = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

    def load_data(self) -> pd.DataFrame:
        features_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                          'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
        targets_names = ['quality']
        data = pd.read_csv(self._source, sep=';')
        dataset = {"dataset": data, "features_names": features_names, "targets_names": targets_names}
        return dataset
