import unittest.mock

from src.preprocessing import PreprocessorFactory


class TestPreprocessorFactory(unittest.TestCase):
    def test__can_init_dummy(self):
        preprocessor_factory = PreprocessorFactory("dummy")
        self.assertIsNotNone(preprocessor_factory)

    def test__can_init_min_max(self):
        preprocessor_factory = PreprocessorFactory("min-max")
        self.assertIsNotNone(preprocessor_factory)

    def test__can_init_standard(self):
        preprocessor_factory = PreprocessorFactory("standard")
        self.assertIsNotNone(preprocessor_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown preprocessor type 'foo'$"):
            PreprocessorFactory("foo")

    def test__can_create_dummy(self):
        preprocessor_factory = PreprocessorFactory("dummy")

        with unittest.mock.patch("src.preprocessing.DummyPreprocessor") as mock:
            preprocessor = preprocessor_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(preprocessor, mock.return_value.__class__)

    def test__can_create_min_max(self):
        preprocessor_factory = PreprocessorFactory("min-max")

        with unittest.mock.patch("src.preprocessing.MinMaxPreprocessor") as mock:
            preprocessor = preprocessor_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(preprocessor, mock.return_value.__class__)

    def test__can_create_standard(self):
        preprocessor_factory = PreprocessorFactory("standard")

        with unittest.mock.patch("src.preprocessing.StandardPreprocessor") as mock:
            preprocessor = preprocessor_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(preprocessor, mock.return_value.__class__)
