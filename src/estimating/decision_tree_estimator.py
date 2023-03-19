from random import randint

from sklearn.tree import DecisionTreeRegressor

from src.estimating import SkLearnEstimatorBase


class DecisionTreeEstimator(SkLearnEstimatorBase):
    @property
    def name(self) -> str:
        return "decision-tree"

    def _get_model(self):
        return DecisionTreeRegressor(max_depth=7, random_state=randint(0, 1000))
