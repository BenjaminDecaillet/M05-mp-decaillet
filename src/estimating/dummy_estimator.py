import pandas as pd

from src.estimating import Estimator


# dummy estimator that always predicts 42
class DummyEstimator(Estimator):  # pragma: no cover
    def fit(self, features: pd.DataFrame, targets: pd.DataFrame) -> None:
        pass

    def predict(self, features: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame(data=[42] * len(features), columns=["target"])
