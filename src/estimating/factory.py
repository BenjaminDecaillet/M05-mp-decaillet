import src.estimating
from src.estimating import Estimator


class EstimatorFactory:
    def __init__(self, type: str):
        if type not in {"linear-regression", "decision-tree"}:
            raise ValueError(f"Unknown estimator type '{type}'")
        self._type = type

    def create(self) -> Estimator:
        if self._type == "linear-regression":
            return src.estimating.LinearRegressionEstimator()
        if self._type == "decision-tree":
            return src.estimating.DecisionTreeEstimator()
