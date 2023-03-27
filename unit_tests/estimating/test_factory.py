import unittest.mock

from decm05.estimating import EstimatorFactory


class TestEstimatorFactory(unittest.TestCase):
    def test__can_init_linear_regression(self):
        estimator_factory = EstimatorFactory("linear-regression")
        self.assertIsNotNone(estimator_factory)

    def test__can_init_decision_tree(self):
        estimator_factory = EstimatorFactory("decision-tree")
        self.assertIsNotNone(estimator_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown estimator type 'foo'$"):
            EstimatorFactory("foo")

    def test__can_create_linear_regression(self):
        estimator_factory = EstimatorFactory("linear-regression")

        with unittest.mock.patch("decm05.estimating.LinearRegressionEstimator") as mock:
            actual = estimator_factory.create_many()

        mock.assert_called_once_with()
        self.assertEquals(actual, [mock.return_value])

    def test__can_create_decision_tree(self):
        estimator_factory = EstimatorFactory("decision-tree")

        with unittest.mock.patch("decm05.estimating.DecisionTreeEstimator") as mock:
            actual = estimator_factory.create_many()

        mock.assert_called_once_with()
        self.assertEquals(actual, [mock.return_value])
