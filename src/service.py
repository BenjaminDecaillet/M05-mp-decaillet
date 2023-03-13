from random import seed as set_random_seed

import src.estimating
import src.preparator
import src.preprocessing


class Service:
    def __init__(self) -> None:
        set_random_seed(42)
        self._preprocessor_factory = src.preprocessing.PreprocessorFactory("standard")
        self._preparator_factory = src.preparator.PreparatorFactory("wines", "file")
        self._estimator_factory = src.estimating.EstimatorFactory("regression")
        self._evaluation_count = 3

    def run(self) -> None:
        evaluator = src.Evaluator(self._preparator_factory.create(),
                                  self._preprocessor_factory.create(),
                                  self._estimator_factory.create(),
                                  self._evaluation_count)
        mae = evaluator.evaluate()
        print(f"MAE: {mae}")
