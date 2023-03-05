import unittest.mock

import pandas as pd

from src.preprocessing import MinMaxPreprocessor


class TestMinMaxPreprocessor(unittest.TestCase):
    def test__happy_path(self):
        preprocessor = MinMaxPreprocessor()

        with self.subTest("fit_transform"):
            training_features = pd.DataFrame(data={
                "feature 1": [1, 2, 3, 4, 5],
                "feature 2": [5, 4, 3, 2, 1]
            })
            expected = pd.DataFrame(data={
                "feature 1 (scaled)": [0, 0.25, 0.5, 0.75, 1],
                "feature 2 (scaled)": [1, 0.75, 0.5, 0.25, 0]
            })

            actual = preprocessor.fit_transform(training_features)

            pd.testing.assert_frame_equal(actual, expected)

        with self.subTest("transform"):
            test_features = pd.DataFrame(data={
                "feature 1": [0, 3, 5],
                "feature 2": [5, 2, 1]
            })
            expected = pd.DataFrame(data={
                "feature 1 (scaled)": [-0.25, 0.5, 1],
                "feature 2 (scaled)": [1, 0.25, 0]
            })

            actual = preprocessor.transform(test_features)

            pd.testing.assert_frame_equal(actual, expected)

    def test__fails_if_not_fit(self):
        preprocessor = MinMaxPreprocessor()
        test_features = pd.DataFrame(data={"feature 1": [0, 3, 5]})

        with self.assertRaisesRegex(RuntimeError, "^Preprocessor has not been fit yet.$"):
            preprocessor.transform(test_features)

    def test__fails_if_columns_dont_match(self):
        preprocessor = MinMaxPreprocessor()
        training_features = pd.DataFrame(data={
            "feature 1": [1, 2, 3, 4, 5],
            "feature 2": [5, 4, 3, 2, 1]
        })
        test_features = pd.DataFrame(data={
            # wrong order
            "feature 2": [0, 3, 5],
            "feature 1": [5, 2, 1]
        })

        preprocessor.fit_transform(training_features)

        with self.assertRaisesRegex(ValueError, "^Features have different columns than training features.$"):
            preprocessor.transform(test_features)
