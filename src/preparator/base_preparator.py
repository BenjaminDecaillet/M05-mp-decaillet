from typing import List

import pandas as pd

from src.preparator import Preparator


class BasePreparator(Preparator):
    def __init__(self, sources: List[str], **files_kwargs) -> None:
        super().__init__()
        self._sources = sources
        self._src_type = files_kwargs['src_type']
        self._type = files_kwargs['type']
        self._sep = files_kwargs['sep']
        self._column_names = files_kwargs['columns']
        self._delim_whitespace = files_kwargs['delim_whitespace']
        self.data = pd.DataFrame()

    def load_data(self) -> pd.DataFrame:
        for src in self._sources:
            try:
                if (self._delim_whitespace):
                    _data = pd.read_csv(src, delim_whitespace=True, names=self._column_names)
                else:
                    _data = pd.read_csv(src, sep=self._sep, delim_whitespace=self._delim_whitespace,
                                        names=self._column_names)
            except BaseException:
                raise FileNotFoundError(f'File not found when trying to read {self._type} data from {self._src_type}.')
            frames = [self.data, _data]
            self.data = pd.concat(frames)
        return self.data
