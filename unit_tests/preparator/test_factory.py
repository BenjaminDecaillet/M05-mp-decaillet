import unittest.mock

from src.preparator import PreparatorFactory


class TestPreparatorFactory(unittest.TestCase):
    def test__can_init_boston(self):
        preparator_factory = PreparatorFactory("boston")
        self.assertIsNotNone(preparator_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown preparator type 'foo'$"):
            PreparatorFactory("foo")

    def test__can_create_boston(self):
        preparator_factory = PreparatorFactory("boston")

        with unittest.mock.patch("src.preparator.BostonPreparator") as mock:
            preparator = preparator_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(preparator, mock.return_value.__class__)
