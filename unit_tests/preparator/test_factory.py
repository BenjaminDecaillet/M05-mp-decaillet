import unittest.mock

from src.preparator import PreparatorFactory


class TestPreparatorFactory(unittest.TestCase):
    def test__can_init_red_wine_with_file(self):
        preparator_factory = PreparatorFactory("red-wine", 'file')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_white_wine_with_file(self):
        preparator_factory = PreparatorFactory("white-wine", 'file')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_wines_with_file(self):
        preparator_factory = PreparatorFactory("wines", 'file')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_boston_with_file(self):
        preparator_factory = PreparatorFactory("boston", 'file')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_red_wine_with_url(self):
        preparator_factory = PreparatorFactory("red-wine", 'url')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_white_wine_with_url(self):
        preparator_factory = PreparatorFactory("white-wine", 'url')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_wines_with_url(self):
        preparator_factory = PreparatorFactory("wines", 'url')
        self.assertIsNotNone(preparator_factory)

    def test__can_init_boston_with_url(self):
        preparator_factory = PreparatorFactory("boston", 'url')
        self.assertIsNotNone(preparator_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown preparator type 'foo'$"):
            PreparatorFactory("foo", 'file')

    def test__init_fails__on_bad_source(self):
        with self.assertRaisesRegex(ValueError, "^Unknown source type 'foo'$"):
            PreparatorFactory("boston", "foo")

    def test__can_create_white_wine(self):
        preparator_factory = PreparatorFactory("white-wine", 'file')

        with unittest.mock.patch("src.preparator.WhiteWinePreparator") as mock:
            preparator = preparator_factory.create()

        mock.assert_called_once_with('file')
        self.assertIsInstance(preparator, mock.return_value.__class__)

    def test__can_create_red_wine(self):
        preparator_factory = PreparatorFactory("red-wine", 'file')

        with unittest.mock.patch("src.preparator.RedWinePreparator") as mock:
            preparator = preparator_factory.create()

        mock.assert_called_once_with('file')
        self.assertIsInstance(preparator, mock.return_value.__class__)

    def test__can_create_wine(self):
        preparator_factory = PreparatorFactory("wines", 'file')

        with unittest.mock.patch("src.preparator.WinePreparator") as mock:
            preparator = preparator_factory.create()

        mock.assert_called_once_with('file')
        self.assertIsInstance(preparator, mock.return_value.__class__)

    def test__can_create_boston(self):
        preparator_factory = PreparatorFactory("boston", 'file')

        with unittest.mock.patch("src.preparator.BostonPreparator") as mock:
            preparator = preparator_factory.create()

        mock.assert_called_once_with('file')
        self.assertIsInstance(preparator, mock.return_value.__class__)
