import unittest.mock

from src.estimating import EstimatorFactory


class TestEstimatorFactory(unittest.TestCase):
    def test__can_init_linear(self):
        estimator_factory = EstimatorFactory("linear")
        self.assertIsNotNone(estimator_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown estimator type 'foo'$"):
            EstimatorFactory("foo")

    def test__can_create_linear(self):
        estimator_factory = EstimatorFactory("linear")

        with unittest.mock.patch("src.estimating.LinearEstimator") as mock:
            estimator = estimator_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(estimator, mock.return_value.__class__)
