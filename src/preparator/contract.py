import abc

import pandas as pd


class Preparator(abc.ABC):
    @abc.abstractmethod
    def load_data(self) -> pd.DataFrame:
        raise NotImplementedError("override me")  # pragma: no cover
