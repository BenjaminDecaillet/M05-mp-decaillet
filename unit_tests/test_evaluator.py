import unittest.mock

import pandas as pd

from src import Evaluator
from src.estimating import Estimator
from src.preparator import BostonPreparator
from src.preprocessing import Preprocessor


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.addCleanup(unittest.mock.patch.stopall)
        self._randint_patch = unittest.mock.patch("src.evaluator.randint").start()
        self._tts_patch = unittest.mock.patch("src.evaluator.train_test_split").start()
        self._mae_patch = unittest.mock.patch("src.evaluator.mean_absolute_error").start()

        self._mock_preparator = unittest.mock.Mock(spec=BostonPreparator)
        self._mock_preprocessor = unittest.mock.Mock(spec=Preprocessor)
        self._mock_estimator = unittest.mock.Mock(spec=Estimator)

    def test__can_init(self):
        evaluator = Evaluator(self._mock_preparator,
                              self._mock_preprocessor,
                              self._mock_estimator,
                              evaluation_count=3)

        self.assertIsNotNone(evaluator)

    def test__init_fails__on_bad_preparator(self):
        with self.assertRaisesRegex(TypeError, "^preparator must be a Preparator$"):
            Evaluator("not a preparator", self._mock_preprocessor, self._mock_estimator, 2)

    def test__init_fails__on_bad_preprocessor(self):
        with self.assertRaisesRegex(TypeError, "^preprocessor must be a Preprocessor$"):
            Evaluator(self._mock_preparator, "not a preprocessor", self._mock_estimator, 2)

    def test__init_fails__on_bad_estimator(self):
        with self.assertRaisesRegex(TypeError, "^estimator must be an Estimator$"):
            Evaluator(self._mock_preparator, self._mock_preprocessor, "not an estimator", 1)

    def test__init_fails__on_bad_evaluation_count(self):
        with self.assertRaisesRegex(TypeError, "^evaluation_count must be an int$"):
            Evaluator(self._mock_preparator, self._mock_preprocessor, self._mock_estimator, None)  # None is not an int

        with self.assertRaisesRegex(ValueError, "^evaluation_count must be >= 1$"):
            Evaluator(self._mock_preparator, self._mock_preprocessor, self._mock_estimator, 0)

    def test__can_evaluate(self):
        evaluator = Evaluator(self._mock_preparator,
                              self._mock_preprocessor,
                              self._mock_estimator,
                              evaluation_count=3)
        self._tts_patch.return_value = (unittest.mock.MagicMock(spec=pd.DataFrame),
                                        unittest.mock.MagicMock(spec=pd.DataFrame))
        self._mae_patch.side_effect = [40.0, 43.0, 43.0]
        self._mock_preparator.load_data.return_value = {
            "dataset": pd.DataFrame(),
            "features_names": [],
            "targets_names": []
        }

        result = evaluator.evaluate()

        self.assertEqual(result, 42.0)
        self._mock_preparator.load_data.assert_called_once_with()
        self.assertEqual(self._randint_patch.call_count, 3)
        self.assertEqual(self._tts_patch.call_count, 3)
        self.assertEqual(self._mock_preprocessor.fit_transform.call_count, 3)
        self.assertEqual(self._mock_preprocessor.transform.call_count, 3)
        self.assertEqual(self._mock_estimator.fit.call_count, 3)
        self.assertEqual(self._mock_estimator.predict.call_count, 3)
        self.assertEqual(self._mae_patch.call_count, 3)
