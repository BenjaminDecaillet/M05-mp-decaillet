import unittest.mock

from src import ArgParser
from src.estimating import EstimatorFactory


class TestArgParser(unittest.TestCase):
    def setUp(self) -> None:
        self.addCleanup(unittest.mock.patch.stopall)

        self._estimator_factory_class_mock = unittest.mock.patch('src.arg_parser.EstimatorFactory').start()
        self._estimator_factory_class_mock.allowed_types = EstimatorFactory.allowed_types

    def test__has_defaults(self) -> None:
        argv = []

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, None)
        self._estimator_factory_class_mock.assert_called_once_with('decision-tree')
        self.assertEqual(arg_parser.estimator_factory, self._estimator_factory_class_mock.return_value)
        self.assertEqual(arg_parser.evaluation_count, 3)

    def test__can_set_values(self) -> None:
        argv = ['--seed', '-12',
                '--evaluation-count', '15',
                '--estimator-type', 'linear-regression']  # This is the default, but it's the only allowed type.

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, -12)
        self._estimator_factory_class_mock.assert_called_once_with('linear-regression')
        self.assertEqual(arg_parser.estimator_factory, self._estimator_factory_class_mock.return_value)
        self.assertEqual(arg_parser.evaluation_count, 15)

    def test__seed_must_be_int(self) -> None:
        argv = ['--seed', '1.3']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--seed', 'forty-two']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__estimator_type_must_be_allowed(self) -> None:
        argv = ['--estimator-type', 'foo']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__evaluation_count_must_be_positive(self) -> None:
        argv = ['--evaluation-count', '0']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--evaluation-count', '-1']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--evaluation-count', '12.8']
        with self.assertRaises(SystemExit):
            ArgParser(argv)
