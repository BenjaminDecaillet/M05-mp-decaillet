import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

from src.estimating import Estimator


class RegressionEstimator(Estimator):  # pragma: no cover TODO add unit tests + define if we want to pass the max_depth
    def __init__(self):
        super().__init__()
        self._model = DecisionTreeRegressor(max_depth=7, random_state=42)

    def fit(self, features: pd.DataFrame, targets: pd.DataFrame):
        """ Performs grid search over the 'max_depth' parameter for a 
        decision tree regressor trained on the input data [features, targets]. """

        self._model.fit(features, targets)

    def predict(self, features: pd.DataFrame) -> np.array:
        return self._model.predict(features)
