import unittest
from unittest.mock import patch

import pandas as pd

from decm05.preparator import RedWinePreparator


class TestRedWinePreparator(unittest.TestCase):
    _features_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                       'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    _targets_names = ['quality']

    def test_constructor_file(self):
        file_preparator = RedWinePreparator('file')

        self.assertIsNotNone(file_preparator)

    def test_constructor_url(self):
        url_preparator = RedWinePreparator('url')

        self.assertIsNotNone(url_preparator)

    def test_name(self):
        actual = RedWinePreparator('file').name

        self.assertEqual(actual, 'red-wine')

    def test_load_from_file(self):
        file_preparator = RedWinePreparator('file')

        actual = file_preparator.load_data()

        self.assertEqual(actual['dataset'].shape, (1599, 12))
        self.assertEqual(actual['dataset'].columns.tolist(), self._features_names + self._targets_names)
        self.assertEqual(actual['features_names'], self._features_names)
        self.assertEqual(actual['targets_names'], self._targets_names)

    def test_load_from_url(self):
        url_preparator = RedWinePreparator('url')
        self.addCleanup(patch.stopall)
        mock_df = unittest.mock.Mock(spec=pd.DataFrame)
        mock_read_csv = patch('pandas.read_csv').start()
        mock_concat = patch('pandas.concat').start()
        mock_read_csv.return_value = mock_df
        mock_concat.return_value = mock_df

        actual = url_preparator.load_data()

        mock_read_csv.assert_called_once_with(
            'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
            sep=';')
        mock_concat.assert_called_once_with([mock_df])
        self.assertEqual(actual['dataset'], mock_df)
        self.assertEqual(actual['features_names'], self._features_names)
        self.assertEqual(actual['targets_names'], self._targets_names)
