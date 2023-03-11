from sklearn.linear_model import LinearRegression

from src.estimating import BaseEstimator


class LinearEstimator(BaseEstimator):
    def _get_model(self):
        return LinearRegression()
