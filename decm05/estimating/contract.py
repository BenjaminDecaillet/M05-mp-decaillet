import abc

import pandas as pd


class Estimator(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError("override me")  # pragma: no cover

    @abc.abstractmethod
    def fit(self, features: pd.DataFrame, targets: pd.DataFrame) -> None:
        raise NotImplementedError("override me")  # pragma: no cover

    @abc.abstractmethod
    def predict(self, features: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("override me")  # pragma: no cover
