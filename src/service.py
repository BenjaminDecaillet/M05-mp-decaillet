import src.evaluator
from src import *


class Service:
    def run(self) -> None:
        evaluator = Evaluator()
        mae = evaluator.evaluate()

        print(f"MAE: {mae}")
