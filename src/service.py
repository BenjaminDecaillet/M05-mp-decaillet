from random import seed as set_random_seed

import src.estimating
import src.preparator
import src.preprocessing


class Service:
    """Entry point for the application.

    This class is responsible for creating the necessary objects and inject
    them into the Evaluator class.

    Usage: ``Service().run()``
    """

    def __init__(self) -> None:
        arg_parser = src.ArgParser()

        set_random_seed(arg_parser.seed)
        self._preprocessor_factory = src.preprocessing.PreprocessorFactory("standard")
        self._preparator_factory = src.preparator.PreparatorFactory("wines", "file")
        self._estimator_factory = src.estimating.EstimatorFactory("decision-tree")
        self._evaluation_count = arg_parser.evaluation_count

    def run(self) -> None:
        """Run the application."""
        evaluator = src.Evaluator(self._preparator_factory.create(),
                                  self._preprocessor_factory.create(),
                                  self._estimator_factory.create(),
                                  self._evaluation_count)
        mae = evaluator.evaluate()
        print(f"MAE: {mae}")
