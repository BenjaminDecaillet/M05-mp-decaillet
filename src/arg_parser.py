import argparse


class ArgParser:
    def __init__(self, argv=None):
        parser = argparse.ArgumentParser(
            description="M05-mp-decaillet (https://github.com/master-ai-batch5/M05-mp-decaillet)")

        parser.add_argument("--seed",
                            help="seed to lock random number generation",
                            type=int, default=None)
        parser.add_argument("--evaluation-count",
                            help="number of times to evaluate the model",
                            type=self._strictly_positive_int, default=3)

        args = parser.parse_args(argv)

        self._seed = args.seed
        self._evaluation_count = args.evaluation_count

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def evaluation_count(self) -> int:
        return self._evaluation_count

    @classmethod
    def _strictly_positive_int(cls, str_value) -> bool:
        try:
            int_value = int(str_value)
            if int_value > 0:
                return int_value
            raise ValueError
        except ValueError:
            pass
        raise argparse.ArgumentTypeError(f"{str_value} is not a positive integer")
