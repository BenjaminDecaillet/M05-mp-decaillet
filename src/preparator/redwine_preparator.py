import pandas as pd

from src.preparator import BasePreparator


class RedWinePreparator(BasePreparator):
    def __init__(self, source: str):
        if source == 'file':
            sources = 'data/winequality-red.csv'
        else:
            sources = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
        features_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                          'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
        targets_names = ['quality']
        super().__init__(sources, features_names, targets_names, sep=';')
