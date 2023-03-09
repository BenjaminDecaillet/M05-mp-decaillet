from typing import List

import pandas as pd

from src.preparator import Preparator


class BasePreparator(Preparator):
    def __init__(
            self,
            source: str,
            features_names: list[str],
            targets_names: list[str],
            **read_csv_kwargs: dict) -> None:
        super().__init__()
        self._read_csv_kwargs = read_csv_kwargs
        self._source = source
        self._features_names = features_names
        self._targets_names = targets_names

    def load_data(self) -> pd.DataFrame:
        data = pd.read_csv(self._source, **self._read_csv_kwargs)
        dataset = {"dataset": data, "features_names": self._features_names, "targets_names": self._targets_names}
        return dataset
