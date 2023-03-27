import unittest.mock

from decm05.preprocessing import PreprocessorFactory


class TestPreprocessorFactory(unittest.TestCase):
    def test__can_init_min_max(self):
        preprocessor_factory = PreprocessorFactory("min-max")
        self.assertIsNotNone(preprocessor_factory)

    def test__can_init_standard(self):
        preprocessor_factory = PreprocessorFactory("standard")
        self.assertIsNotNone(preprocessor_factory)

    def test__can_init_polynomial_without_kwargs(self):
        preprocessor_factory = PreprocessorFactory("polynomial")
        self.assertIsNotNone(preprocessor_factory)

    def test__can_init_polynomial_with_kwargs(self):
        preprocessor_factory = PreprocessorFactory("polynomial", {"foo": "bar"})
        self.assertIsNotNone(preprocessor_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown preprocessor type 'foo'$"):
            PreprocessorFactory("foo")

    def test__init_fails__on_polynomial_kwargs_for_non_polynomial(self):
        with self.assertRaisesRegex(ValueError, "^polynomial_kwargs should be None for non-polynomial preprocessors$"):
            PreprocessorFactory("standard", {})
        with self.assertRaisesRegex(ValueError, "^polynomial_kwargs should be None for non-polynomial preprocessors$"):
            PreprocessorFactory("min-max", {})

    def test__init_fails__on_invalid_polynomial_kwargs(self):
        with self.assertRaisesRegex(TypeError, "^polynomial_kwargs should be a dict$"):
            PreprocessorFactory("polynomial", "foo")

    def test__can_create_min_max(self):
        preprocessor_factory = PreprocessorFactory("min-max")

        with unittest.mock.patch("decm05.preprocessing.MinMaxPreprocessor") as mock:
            actual = preprocessor_factory.create_many()

        mock.assert_called_once_with()
        self.assertEquals(actual, [mock.return_value])

    def test__can_create_standard(self):
        preprocessor_factory = PreprocessorFactory("standard")

        with unittest.mock.patch("decm05.preprocessing.StandardPreprocessor") as mock:
            actual = preprocessor_factory.create_many()

        mock.assert_called_once_with()
        self.assertEquals(actual, [mock.return_value])

    def test__can_create_polynomial(self):
        preprocessor_factory = PreprocessorFactory("polynomial", {"foo": "bar"})

        with unittest.mock.patch("decm05.preprocessing.PolynomialPreprocessor") as mock:
            actual = preprocessor_factory.create_many()

        mock.assert_called_once_with(foo="bar")
        self.assertEquals(actual, [mock.return_value])
