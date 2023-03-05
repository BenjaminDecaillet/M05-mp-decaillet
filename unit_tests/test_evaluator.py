import unittest.mock

from src import Evaluator
from src.preprocessing import Preprocessor


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self._mock_preprocessor = unittest.mock.Mock(spec=Preprocessor)

    def test__can_init(self):
        evaluator = Evaluator(self._mock_preprocessor)

        self.assertIsNotNone(evaluator)

    def test__init_fails__on_bad_preprocessor(self):
        with self.assertRaisesRegex(TypeError, "^preprocessor must be a Preprocessor$"):
            Evaluator("not a preprocessor")

    def test__can_evaluate(self):
        evaluator = Evaluator(self._mock_preprocessor)

        result = evaluator.evaluate()

        self.assertEqual(result, 42)
        self._mock_preprocessor.fit_transform.assert_called_once()
        self._mock_preprocessor.transform.assert_called_once()
