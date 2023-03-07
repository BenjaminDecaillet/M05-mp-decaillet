import unittest
from unittest.mock import patch

import pandas as pd

from src.preparator import RedWinePreparator


class TestRedWinePreparator(unittest.TestCase):
    def setUp(self):
        self._column_names = [
            'fixed acidity',
            'volatile acidity',
            'citric acid',
            'residual sugar',
            'chlorides',
            'free sulfur dioxide',
            'total sulfur dioxide',
            'density',
            'pH',
            'sulphates',
            'alcohol',
            'quality']

    def test_constructor_file(self):
        file_preparator = RedWinePreparator('file')

        self.assertIsNotNone(file_preparator)

    def test_constructor_url(self):
        url_preparator = RedWinePreparator('url')

        self.assertIsNotNone(url_preparator)

    def test_load_from_file(self):
        file_preparator = RedWinePreparator('file')

        actual = file_preparator.load_data()

        self.assertEqual(actual.shape, (1600, 12))

    def test_load_data_from_url(self):
        url_preparator = RedWinePreparator('url')
        expected = pd.read_csv('data/test-winequality-red.csv', sep=';')

        with unittest.mock.patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.return_value = expected
            actual = url_preparator.load_data()

        mock_read_csv.assert_called_once_with(
            'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
            sep=';',
            delim_whitespace=False,
            names=url_preparator._column_names)
        pd.testing.assert_frame_equal(actual.head(2), expected)

    def test_fails_if_file_not_found(self):
        url_preparator = RedWinePreparator('url')
        with unittest.mock.patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.side_effect = FileNotFoundError()

            with self.assertRaisesRegex(FileNotFoundError, "File not found when trying to read red wine data from url."):
                url_preparator.load_data()