import pandas as pd
from sklearn import preprocessing

from src.preprocessing import Preprocessor


class MinMaxPreprocessor(Preprocessor):
    def __init__(self) -> None:
        super().__init__()
        self._scaler = None
        self._columns = []

    def fit_transform(self, features: pd.DataFrame) -> pd.DataFrame:
        self._columns = features.columns
        self._scaler = preprocessing.MinMaxScaler()

        scaled_features = self._scaler.fit_transform(features)

        return pd.DataFrame(data=scaled_features,
                            index=features.index,
                            columns=self._columns)

    def transform(self, features: pd.DataFrame) -> pd.DataFrame:
        if self._scaler is None:
            raise RuntimeError("Preprocessor has not been fit yet.")
        if not self._columns == features.columns:
            raise ValueError("Features have different columns than training features.")

        scaled_features = self._scaler.transform(features)

        return pd.DataFrame(data=scaled_features,
                            index=features.index,
                            columns=self._columns)
