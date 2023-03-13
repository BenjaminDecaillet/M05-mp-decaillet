import abc

import pandas as pd

from src.estimating import Estimator


class SkLearnEstimatorBase(Estimator):
    def __init__(self):
        super().__init__()
        self._model = None
        self._feature_columns = []
        self._target_columns = []

    def fit(self, features: pd.DataFrame, targets: pd.DataFrame):
        self._feature_columns = features.columns
        self._target_columns = targets.columns

        self._model = self._get_model()
        self._model.fit(features, targets)

    def predict(self, features: pd.DataFrame) -> pd.DataFrame:
        if self._model is None:
            raise RuntimeError("Estimator has not been fit yet.")
        if not self._feature_columns.equals(features.columns):
            raise ValueError("Features have different columns than training features.")

        prediction = self._model.predict(features)

        return pd.DataFrame(data=prediction,
                            index=features.index,
                            columns=self._target_columns)

    @abc.abstractmethod
    def _get_model(self):
        raise NotImplementedError("override me")  # pragma: no cover
