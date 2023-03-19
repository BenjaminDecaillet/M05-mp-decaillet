import unittest.mock

import pandas as pd

from src.preprocessing import StandardPreprocessor


class TestStandardPreprocessor(unittest.TestCase):
    def test__happy_path(self):
        preprocessor = StandardPreprocessor()

        with self.subTest("fit_transform"):
            training_features = pd.DataFrame(data={
                "feature 1": [1, 2, 3, 4, 5],
                "feature 2": [5, 4, 3, 2, 1]
            })
            expected = pd.DataFrame(data={
                "feature 1 (scaled)": [-1.41421, -0.70711, 0.0, 0.70711, 1.41421],
                "feature 2 (scaled)": [1.41421, 0.70711, 0.0, -0.70711, -1.41421]
            })

            actual = preprocessor.fit_transform(training_features)

            pd.testing.assert_frame_equal(actual, expected)

        with self.subTest("transform"):
            test_features = pd.DataFrame(data={
                "feature 1": [0, 3, 5],
                "feature 2": [5, 2, 1]
            })
            expected = pd.DataFrame(data={
                "feature 1 (scaled)": [-2.12132, 0.0, 1.41421],
                "feature 2 (scaled)": [1.41421, -0.70711, -1.41421]
            })

            actual = preprocessor.transform(test_features)

            pd.testing.assert_frame_equal(actual, expected)

    def test__name(self):
        actual = StandardPreprocessor().name

        self.assertEqual(actual, "standard")

    def test__fails_if_not_fit(self):
        preprocessor = StandardPreprocessor()
        test_features = pd.DataFrame(data={"feature 1": [0, 3, 5]})

        with self.assertRaisesRegex(RuntimeError, "^Preprocessor has not been fitted yet.$"):
            preprocessor.transform(test_features)

    def test__fails_if_columns_dont_match(self):
        preprocessor = StandardPreprocessor()
        training_features = pd.DataFrame(data={
            "feature 1": [1, 2, 3, 4, 5],
            "feature 2": [5, 4, 3, 2, 1]
        })
        test_features = pd.DataFrame(data={
            "feature 1": [0, 3, 5],
            "feature 3": [5, 2, 1]  # <-- different column name
        })

        preprocessor.fit_transform(training_features)

        with self.assertRaisesRegex(ValueError, "^Features have different columns than training features.$"):
            preprocessor.transform(test_features)
