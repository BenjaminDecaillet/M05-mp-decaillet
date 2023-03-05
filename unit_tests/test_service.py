import unittest.mock

from src import Service
from src.preprocessing import Preprocessor


class TestService(unittest.TestCase):
    def setUp(self) -> None:
        self.addCleanup(unittest.mock.patch.stopall)

        self._evaluator_class_mock = unittest.mock.patch('src.Evaluator').start()
        self._evaluator_mock = self._evaluator_class_mock.return_value

        self._preprocessor_factory_class_mock = unittest.mock.patch('src.preprocessing.PreprocessorFactory').start()
        self._preprocessor_mock = unittest.mock.Mock(spec=Preprocessor)
        self._preprocessor_factory_class_mock.return_value.create.return_value = self._preprocessor_mock

        self._print_mock = unittest.mock.patch('builtins.print').start()

    def test_runs(self) -> None:
        self._evaluator_mock.evaluate.return_value = 42
        service = Service()

        service.run()

        self._evaluator_class_mock.assert_called_once_with(self._preprocessor_mock)
        self._evaluator_mock.evaluate.assert_called_once()
        self._print_mock.assert_called_once_with('MAE: 42')
