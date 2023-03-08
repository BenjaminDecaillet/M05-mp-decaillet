import unittest

import numpy as np
import pandas as pd

from src.estimating import LinearEstimator


class TestLinearEstimator(unittest.TestCase):
    def test_fit(self):
        estimator = LinearEstimator()
        features = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, 6]})
        targets = pd.Series([7, 8, 9])

        self.assertIsNone(estimator.fit(features, targets))

    def test_predict(self):
        estimator = LinearEstimator()
        features = pd.DataFrame({'x1': [1, 2, 3], 'x2': [4, 5, 6]})
        targets = pd.Series([7, 8, 9])
        test_features = pd.DataFrame({'x1': [4, 5, 6], 'x2': [7, 8, 9]})

        estimator.fit(features, targets)
        result = estimator.predict(test_features)

        self.assertEqual(result.shape, (3,))
        np.testing.assert_array_almost_equal(result, np.array([10., 11., 12.]))
