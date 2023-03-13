import argparse


class ArgParser:
    def __init__(self, argv=None):
        parser = argparse.ArgumentParser(
            description="M05-mp-decaillet (https://github.com/master-ai-batch5/M05-mp-decaillet)")

        parser.add_argument("--seed",
                            help="seed to lock random number generation",
                            type=int, default=None)

        args = parser.parse_args(argv)

        self._seed = args.seed

    @property
    def seed(self) -> int:
        return self._seed
