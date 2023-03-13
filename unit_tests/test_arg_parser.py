import unittest.mock

from src import ArgParser


class TestArgParser(unittest.TestCase):
    def test__has_defaults(self) -> None:
        argv = []

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, None)

    def test__can_set_values(self) -> None:
        argv = ['--seed', '-12']

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, -12)

    def test__seed_must_be_int(self) -> None:
        argv = ['--seed', '1.3']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--seed', 'forty-two']
        with self.assertRaises(SystemExit):
            ArgParser(argv)
