from random import seed as set_random_seed

import pandas as pd

from src import ArgParser, Evaluator


class Service:
    """Entry point for the application.

    This class is responsible for creating the necessary objects and inject
    them into the Evaluator class.

    Usage: ``Service().run()``
    """

    def __init__(self) -> None:
        arg_parser = ArgParser()

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
                        # TODO: don't use __class__.__name__
                        "dataset": preparator.__class__.__name__,
                        "preprocessor": preprocessor.__class__.__name__,
                        "estimator": estimator.__class__.__name__,
                        "evaluation count": self._evaluation_count,

                        "MEAN ABSOLUTE ERROR": evaluator.evaluate(),
                    })

        mean_absolute_errors = pd.DataFrame(mean_absolute_errors)
        print(mean_absolute_errors.to_string(index=False))
