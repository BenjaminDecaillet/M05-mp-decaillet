import abc

import pandas as pd


class Preprocessor(abc.ABC):
    @abc.abstractmethod
    def fit_transform(self, features: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("override me")  # pragma: no cover

    @abc.abstractmethod
    def transform(self, features: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("override me")  # pragma: no cover
