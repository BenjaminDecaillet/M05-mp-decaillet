from typing import List

import pandas as pd

from src.preparator import Preparator


class BasePreparator(Preparator):
    def __init__(
            self,
            sources: List[str],
            features_names: list[str],
            targets_names: list[str],
            **read_csv_kwargs: dict) -> None:
        super().__init__()
        self._read_csv_kwargs = read_csv_kwargs
        self._sources = sources
        self._features_names = features_names
        self._targets_names = targets_names

    def load_data(self) -> pd.DataFrame:
        data_list = []
        for source in self._sources:
            data_list.append(pd.read_csv(source, **self._read_csv_kwargs))
        data_frame = pd.concat(data_list)
        dataset = {"dataset": data_frame, "features_names": self._features_names, "targets_names": self._targets_names}
        return dataset
