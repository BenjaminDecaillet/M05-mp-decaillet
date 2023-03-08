import unittest

from src.preparator import BostonPreparator


class TestBostonPreparator(unittest.TestCase):

    def test_constructor(self):
        file_preparator = BostonPreparator()

        self.assertIsNotNone(file_preparator)

    def test_load_data(self):
        file_preparator = BostonPreparator()
        features_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                          'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        targets_names = ['MEDV']

        actual = file_preparator.load_data()

        self.assertEqual(actual['dataset'].shape, (506, 14))
        self.assertEqual(actual['features_names'], features_names)
        self.assertEqual(actual['targets_names'], targets_names)
