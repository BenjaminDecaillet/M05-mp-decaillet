from sklearn.linear_model import LinearRegression

from src.estimating import SkLearnEstimatorBase


class LinearRegressionEstimator(SkLearnEstimatorBase):
    def _get_model(self):
        return LinearRegression()
