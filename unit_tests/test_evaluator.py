import unittest

from src import Evaluator


class TestEvaluator(unittest.TestCase):
    def test_evaluate(self):
        evaluator = Evaluator()
        self.assertEqual(evaluator.evaluate(), 42)
