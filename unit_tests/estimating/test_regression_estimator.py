import unittest

import pandas as pd

from src.estimating import RegressionEstimator


class TestRegressionEstimator(unittest.TestCase):
    def test_fit(self):
        estimator = RegressionEstimator()
        features = pd.DataFrame({'x1': [1.0, 2.0, 3.0], 'x2': [4.0, 5.0, 6.0]})
        targets = pd.DataFrame({'y1': [7.0, 8.0, 9.0]})

        self.assertIsNone(estimator.fit(features, targets))

    def test_predict(self):
        estimator = RegressionEstimator()
        features = pd.DataFrame({'x1': [1.0, 2.0, 3.0], 'x2': [4.0, 5.0, 6.0]})
        targets = pd.DataFrame({'y1': [7.0, 8.0, 9.0]})
        test_features = pd.DataFrame({'x1': [4.0, 5.0, 6.0], 'x2': [7.0, 8.0, 9.0]})
        estimator.fit(features, targets)

        result = estimator.predict(test_features)

        pd.testing.assert_frame_equal(result, pd.DataFrame({'y1': [9.0, 9.0, 9.0]}))
