from sklearn.linear_model import LinearRegression

from src.estimating import SkLearnEstimatorBase


class LinearEstimator(SkLearnEstimatorBase):
    def _get_model(self):
        return LinearRegression()
