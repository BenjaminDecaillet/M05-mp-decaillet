from src import Evaluator
from src.preprocessing import DummyPreprocessor


class Service:
    def run(self) -> None:
        evaluator = Evaluator(DummyPreprocessor())
        mae = evaluator.evaluate()

        print(f"MAE: {mae}")
