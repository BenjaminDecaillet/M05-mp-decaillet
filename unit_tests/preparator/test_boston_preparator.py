import unittest
from unittest.mock import patch

import pandas as pd

from src.preparator import BostonPreparator


class TestBostonPreparator(unittest.TestCase):
    _features_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                       'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    _targets_names = ['MEDV']

    def test_constructor_file(self):
        file_preparator = BostonPreparator('file')

        self.assertIsNotNone(file_preparator)

    def test_constructor_url(self):
        file_preparator = BostonPreparator('url')

        self.assertIsNotNone(file_preparator)

    def test_name(self):
        actual = BostonPreparator('file').name

        self.assertEqual(actual, 'boston')

    def test_load_from_file(self):
        file_preparator = BostonPreparator('file')

        actual = file_preparator.load_data()

        self.assertEqual(actual['dataset'].shape, (506, 14))
        self.assertEqual(actual['dataset'].columns.tolist(), self._features_names + self._targets_names)
        self.assertEqual(actual['features_names'], self._features_names)
        self.assertEqual(actual['targets_names'], self._targets_names)

    def test_load_from_url(self):
        url_preparator = BostonPreparator('url')
        self.addCleanup(patch.stopall)
        mock_df = unittest.mock.Mock(spec=pd.DataFrame)
        mock_read_csv = patch('pandas.read_csv').start()
        mock_concat = patch('pandas.concat').start()
        mock_read_csv.return_value = mock_df
        mock_concat.return_value = mock_df

        actual = url_preparator.load_data()

        mock_read_csv.assert_called_once_with(
            'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
            delim_whitespace=True, names=self._features_names + self._targets_names)
        mock_concat.assert_called_once_with([mock_df])
        self.assertEqual(actual['dataset'], mock_df)
        self.assertEqual(actual['features_names'], self._features_names)
        self.assertEqual(actual['targets_names'], self._targets_names)
