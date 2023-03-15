import src.estimating
from src.estimating import Estimator


class EstimatorFactory:
    def __init__(self, type: str):
        if type not in self.allowed_types:
            raise ValueError(f"Unknown estimator type '{type}'")
        self._types = [type]

    def create_many(self) -> list[Estimator]:
        estimators = []
        for type in self._types:
            if type == "linear-regression":
                estimators.append(src.estimating.LinearRegressionEstimator())
                continue
            if type == "decision-tree":
                estimators.append(src.estimating.DecisionTreeEstimator())
                continue
        return estimators

    @classmethod
    @property
    def allowed_types(cls) -> list[str]:
        return ["linear-regression", "decision-tree"]
