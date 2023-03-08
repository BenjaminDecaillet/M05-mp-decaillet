import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from src.estimating import Estimator


class LinearEstimator(Estimator):
    def __init__(self):
        super().__init__()
        self._model = LinearRegression()

    def fit(self, features: pd.DataFrame, targets: pd.DataFrame):
        self._model.fit(features, targets)

    def predict(self, features: pd.DataFrame) -> np.array:
        return self._model.predict(features)
