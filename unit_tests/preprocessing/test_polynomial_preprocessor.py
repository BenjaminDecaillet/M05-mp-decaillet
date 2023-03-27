import unittest.mock

import pandas as pd

from decm05.preprocessing import PolynomialPreprocessor


class TestPolynomialPreprocessor(unittest.TestCase):
    def test__happy_path_with_default_params(self):
        preprocessor = PolynomialPreprocessor()

        with self.subTest("fit_transform"):
            training_features = pd.DataFrame(data={"feature 1": [1, 2, 3, 4, 5]})
            expected = pd.DataFrame(data={
                "1": [1.0, 1.0, 1.0, 1.0, 1.0],
                "feature 1": [1.0, 2.0, 3.0, 4.0, 5.0],
                "feature 1^2": [1.0, 4.0, 9.0, 16.0, 25.0],
            })

            actual = preprocessor.fit_transform(training_features)

            pd.testing.assert_frame_equal(actual, expected)

        with self.subTest("transform"):
            test_features = pd.DataFrame(data={"feature 1": [0, 3, 5]})
            expected = pd.DataFrame(data={
                "1": [1.0, 1.0, 1.0],
                "feature 1": [0.0, 3.0, 5.0],
                "feature 1^2": [0.0, 9.0, 25.0],
            })

            actual = preprocessor.transform(test_features)

            pd.testing.assert_frame_equal(actual, expected)

    def test__name(self):
        actual = PolynomialPreprocessor().name

        self.assertEqual(actual, "polynomial")

    def test__happy_path_with_custom_params(self):
        preprocessor = PolynomialPreprocessor(degree=(3, 4), include_bias=False)

        with self.subTest("fit_transform"):
            training_features = pd.DataFrame(data={"feature 1": [1, 2, 3, 4, 5]})
            expected = pd.DataFrame(data={
                "feature 1^3": [1.0, 8.0, 27.0, 64.0, 125.0],
                "feature 1^4": [1.0, 16.0, 81.0, 256.0, 625.0],
            })

            actual = preprocessor.fit_transform(training_features)

            pd.testing.assert_frame_equal(actual, expected)

        with self.subTest("transform"):
            test_features = pd.DataFrame(data={"feature 1": [0, 3, 5]})
            expected = pd.DataFrame(data={
                "feature 1^3": [0.0, 27.0, 125.0],
                "feature 1^4": [0.0, 81.0, 625.0],
            })

            actual = preprocessor.transform(test_features)

            pd.testing.assert_frame_equal(actual, expected)

    def test__fails_if_not_fit(self):
        preprocessor = PolynomialPreprocessor()
        test_features = pd.DataFrame(data={"feature 1": [0, 3, 5]})

        with self.assertRaisesRegex(RuntimeError, "^Preprocessor has not been fitted yet.$"):
            preprocessor.transform(test_features)

    def test__fails_if_columns_dont_match(self):
        preprocessor = PolynomialPreprocessor()
        training_features = pd.DataFrame(data={"feature 1": [1, 2, 3, 4, 5]})
        test_features = pd.DataFrame(data={"feature 2": [0, 3, 5]})

        preprocessor.fit_transform(training_features)

        with self.assertRaisesRegex(ValueError, "^Features have different columns than training features.$"):
            preprocessor.transform(test_features)

    def test__fails_with_invalid_custom_params(self):
        preprocessor = PolynomialPreprocessor(foo="bar")

        with self.assertRaisesRegex(TypeError, r"^PolynomialFeatures.__init__\(\) got an unexpected keyword argument 'foo'$"):
            preprocessor.fit_transform(pd.DataFrame(data={"feature 1": [1, 2, 3, 4, 5]}))
