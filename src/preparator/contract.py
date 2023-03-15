import abc

import pandas as pd


class Preparator(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError("override me")  # pragma: no cover

    @abc.abstractmethod
    def load_data(self) -> pd.DataFrame:
        raise NotImplementedError("override me")  # pragma: no cover
