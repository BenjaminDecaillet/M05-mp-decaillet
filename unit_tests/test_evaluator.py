import unittest.mock

import pandas as pd

from src import Evaluator
from src.estimating import Estimator
from src.preprocessing import Preprocessor


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.addCleanup(unittest.mock.patch.stopall)
        self._tts_patch = unittest.mock.patch("src.evaluator.train_test_split").start()
        self._mae_patch = unittest.mock.patch("src.evaluator.mean_absolute_error").start()

        self._mock_preprocessor = unittest.mock.Mock(spec=Preprocessor)
        self._mock_estimator = unittest.mock.Mock(spec=Estimator)

    def test__can_init(self):
        evaluator = Evaluator(self._mock_preprocessor,
                              self._mock_estimator)

        self.assertIsNotNone(evaluator)

    def test__init_fails__on_bad_preprocessor(self):
        with self.assertRaisesRegex(TypeError, "^preprocessor must be a Preprocessor$"):
            Evaluator("not a preprocessor", self._mock_estimator)

    def test__init_fails__on_bad_estimator(self):
        with self.assertRaisesRegex(TypeError, "^estimator must be an Estimator$"):
            Evaluator(self._mock_preprocessor, "not an estimator")

    def test__can_evaluate(self):
        evaluator = Evaluator(self._mock_preprocessor,
                              self._mock_estimator)
        self._tts_patch.return_value = (unittest.mock.MagicMock(spec=pd.DataFrame),
                                        unittest.mock.MagicMock(spec=pd.DataFrame))
        self._mae_patch.return_value = 42

        result = evaluator.evaluate()

        self.assertEqual(result, 42)
        self._tts_patch.assert_called_once()
        self._mock_preprocessor.fit_transform.assert_called_once()
        self._mock_preprocessor.transform.assert_called_once()
        self._mock_estimator.fit.assert_called_once()
        self._mock_estimator.predict.assert_called_once()
        self._mae_patch.assert_called_once()
