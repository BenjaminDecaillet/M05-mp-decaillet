import unittest.mock

from src import ArgParser


class TestArgParser(unittest.TestCase):
    def test__has_defaults(self) -> None:
        argv = []

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, None)
        self.assertEqual(arg_parser.evaluation_count, 3)

    def test__can_set_values(self) -> None:
        argv = ['--seed', '-12',
                '--evaluation-count', '15']

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, -12)
        self.assertEqual(arg_parser.evaluation_count, 15)

    def test__seed_must_be_int(self) -> None:
        argv = ['--seed', '1.3']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--seed', 'forty-two']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__evaluation_count_must_be_positive(self) -> None:
        argv = ['--evaluation-count', '0']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--evaluation-count', '-1']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--evaluation-count', '12.8']
        with self.assertRaises(SystemExit):
            ArgParser(argv)
