import unittest.mock

from src import Service
from src.estimating import Estimator
from src.preparator import Preparator
from src.preprocessing import Preprocessor


class TestService(unittest.TestCase):
    def setUp(self) -> None:
        self.addCleanup(unittest.mock.patch.stopall)

        arg_parser_mock = unittest.mock.patch('src.ArgParser').start().return_value
        arg_parser_mock.seed = 12345
        arg_parser_mock.evaluation_count = 54321

        self._evaluator_class_mock = unittest.mock.patch('src.Evaluator').start()
        self._evaluator_mock = self._evaluator_class_mock.return_value

        self._preparator_factory_class_mock = unittest.mock.patch('src.preparator.PreparatorFactory').start()
        self._preparator_mock = unittest.mock.Mock(spec=Preparator)
        self._preparator_factory_class_mock.return_value.create.return_value = self._preparator_mock

        self._preprocessor_factory_class_mock = unittest.mock.patch('src.preprocessing.PreprocessorFactory').start()
        self._preprocessor_mock = unittest.mock.Mock(spec=Preprocessor)
        self._preprocessor_factory_class_mock.return_value.create.return_value = self._preprocessor_mock

        self._estimator_factory_class_mock = unittest.mock.patch('src.estimating.EstimatorFactory').start()
        self._estimator_mock = unittest.mock.Mock(spec=Estimator)
        self._estimator_factory_class_mock.return_value.create.return_value = self._estimator_mock

        self._print_mock = unittest.mock.patch('builtins.print').start()

    def test__constructor_sets_random_seed(self) -> None:
        with unittest.mock.patch('src.service.set_random_seed') as set_random_seed_mock:
            Service()

        set_random_seed_mock.assert_called_once_with(12345)

    def test_runs(self) -> None:
        self._evaluator_mock.evaluate.return_value = 42
        service = Service()
        service.run()
        self._evaluator_class_mock.assert_called_once_with(self._preparator_mock,
                                                           self._preprocessor_mock,
                                                           self._estimator_mock,
                                                           54321)
        self._evaluator_mock.evaluate.assert_called_once()
        self._print_mock.assert_called_once_with('MAE: 42')
