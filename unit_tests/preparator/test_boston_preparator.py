import unittest
from unittest.mock import patch

import pandas as pd

from src.preparator import BostonPreparator


class TestBostonPreparator(unittest.TestCase):
    def setUp(self):
        self._column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                              'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

    def test_constructor_file(self):
        file_preparator = BostonPreparator('file')

        self.assertIsNotNone(file_preparator)

    def test_constructor_url(self):
        file_preparator = BostonPreparator('url')

        self.assertIsNotNone(file_preparator)

    def test_load_from_file(self):
        file_preparator = BostonPreparator('file')

        actual = file_preparator.load_data()

        self.assertEqual(actual.shape, (506, 14))

    def test_load_data_from_url(self):
        url_preparator = BostonPreparator('url')
        expected = pd.read_csv('data/test-housing.data', delim_whitespace=True, names=self._column_names)

        with unittest.mock.patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.return_value = expected
            actual = url_preparator.load_data()

        mock_read_csv.assert_called_once_with(
            'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
            delim_whitespace=True,
            names=url_preparator._column_names)
        pd.testing.assert_frame_equal(actual.head(3), expected)

    def test_fails_if_file_not_found(self):
        url_preparator = BostonPreparator('url')
        with unittest.mock.patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.side_effect = FileNotFoundError()

            with self.assertRaisesRegex(FileNotFoundError, "File not found when trying to read boston houses data from url."):
                url_preparator.load_data()
