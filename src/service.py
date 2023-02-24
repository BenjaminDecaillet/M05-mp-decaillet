from src import Evaluator
from src.preprocessing import PreprocessorFactory


class Service:
    def __init__(self) -> None:
        self._preprocessor_factory = PreprocessorFactory("dummy")

    def run(self) -> None:
        evaluator = Evaluator(self._preprocessor_factory.create())
        mae = evaluator.evaluate()

        print(f"MAE: {mae}")
