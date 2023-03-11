import abc

import numpy as np
import pandas as pd

from src.estimating import Estimator


class BaseEstimator(Estimator):
    def __init__(self):
        super().__init__()
        self._model = self._get_model()

    def fit(self, features: pd.DataFrame, targets: pd.DataFrame):
        self._model.fit(features, targets)

    def predict(self, features: pd.DataFrame) -> np.array:
        return self._model.predict(features)

    @abc.abstractmethod
    def _get_model(self):
        raise NotImplementedError("override me")  # pragma: no cover
