import src.estimating
from src.estimating import Estimator


class EstimatorFactory:
    def __init__(self, type: str):
        if type not in {"linear"}:
            raise ValueError(f"Unknown estimator type '{type}'")
        self._type = type

    def create(self) -> Estimator:
        if self._type == "linear":
            return src.estimating.LinearEstimator()
