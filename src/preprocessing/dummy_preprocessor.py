import pandas as pd

from src.preprocessing import Preprocessor


# dummy preprocessor that does nothing
class DummyPreprocessor(Preprocessor):  # pragma: no cover
    def fit_transform(self, features: pd.DataFrame) -> pd.DataFrame:
        return features

    def transform(self, features: pd.DataFrame) -> pd.DataFrame:
        return features
