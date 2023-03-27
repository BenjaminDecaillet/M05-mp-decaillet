from random import seed as set_random_seed

import pandas as pd

from decm05 import ArgParser, Evaluator


class Service:
    """
    Entry point for the application, responsible for creating the necessary objects and inject
    them into the Evaluator class.

    Usage:

    * ``Service().run()``
    * ``Service(["--dataset=wines", "--seed=42"]).run()``
    * etc.
    """

    def __init__(self, argv=None) -> None:
        arg_parser = ArgParser(argv=argv)

        set_random_seed(arg_parser.seed)
        self._preparator_factory = arg_parser.preparator_factory
        self._preprocessor_factory = arg_parser.preprocessor_factory
        self._estimator_factory = arg_parser.estimator_factory
        self._evaluation_count = arg_parser.evaluation_count

    def run(self) -> None:
        """Run the application."""
        preparators = self._preparator_factory.create_many()
        preprocessors = self._preprocessor_factory.create_many()
        estimators = self._estimator_factory.create_many()

        mean_absolute_errors = []

        for preparator in preparators:
            for preprocessor in preprocessors:
                for estimator in estimators:
                    evaluator = Evaluator(preparator, preprocessor, estimator, self._evaluation_count)
                    mean_absolute_errors.append({
                        "dataset": preparator.name,
                        "preprocessor": preprocessor.name,
                        "estimator": estimator.name,
                        "evaluation count": self._evaluation_count,

                        "MEAN ABSOLUTE ERROR": evaluator.evaluate(),
                    })

        mean_absolute_errors = pd.DataFrame(mean_absolute_errors)

        # Even with fixed seed, MAEs can be slightly different when comparing execution of this code
        # on different OSes.
        # These are *tiny* differences (i.e. differences after the 5th decimal place, often even way
        # further) which I think are due to floating point arithmetic differences between OSes, but
        # I am not sure. As far as MAE is concerned, they are not significant at all.
        # However, left unchecked, they would cause automated tests to fail (especially when represented
        # as strings, and rounding-to-nearest trickles decimal places up). As a workaround, we round
        # the MAEs to 4 decimal places before printing them.
        mean_absolute_errors = mean_absolute_errors.round(4)

        print(mean_absolute_errors.to_string(index=False))
