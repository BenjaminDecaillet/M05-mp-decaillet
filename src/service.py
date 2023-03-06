from random import seed as set_random_seed

import src.estimating
import src.preprocessing


class Service:
    def __init__(self) -> None:
        set_random_seed(42)
        self._preprocessor_factory = src.preprocessing.PreprocessorFactory("standard")
        self._estimator_factory = src.estimating.EstimatorFactory("dummy")
        self._evaluation_count = 3

    def run(self) -> None:
        evaluator = src.Evaluator(self._preprocessor_factory.create(),
                                  self._estimator_factory.create(),
                                  self._evaluation_count)
        mae = evaluator.evaluate()

        print(f"MAE: {mae}")
