import argparse

from src.estimating import EstimatorFactory
from src.preprocessing import PreprocessorFactory


class ArgParser:
    def __init__(self, argv=None):
        parser = argparse.ArgumentParser(
            description="M05-mp-decaillet (https://github.com/master-ai-batch5/M05-mp-decaillet)")

        parser.add_argument("--seed",
                            help="seed to lock random number generation",
                            type=int, default=None)
        parser.add_argument("--preprocessor-type",
                            help="type of preprocessor to use",
                            choices=PreprocessorFactory.allowed_types, default="standard")
        parser.add_argument("--estimator-type",
                            help="type of estimator to use",
                            choices=EstimatorFactory.allowed_types, default="decision-tree")
        parser.add_argument("--evaluation-count",
                            help="number of times to evaluate the model",
                            type=self._strictly_positive_int, default=3)

        args = parser.parse_args(argv)

        self._seed = args.seed
        self._preprocessor_factory = PreprocessorFactory(args.preprocessor_type)
        self._estimator_factory = EstimatorFactory(args.estimator_type)
        self._evaluation_count = args.evaluation_count

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def preprocessor_factory(self) -> PreprocessorFactory:
        return self._preprocessor_factory

    @property
    def estimator_factory(self) -> EstimatorFactory:
        return self._estimator_factory

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
