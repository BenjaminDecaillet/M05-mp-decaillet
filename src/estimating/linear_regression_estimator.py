from sklearn.linear_model import LinearRegression

from src.estimating import SkLearnEstimatorBase


class LinearRegressionEstimator(SkLearnEstimatorBase):
    @property
    def name(cls) -> str:
        return "linear-regression"

    def _get_model(self):
        return LinearRegression()
