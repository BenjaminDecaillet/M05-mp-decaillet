import src.preprocessing


class Service:
    def __init__(self) -> None:
        self._preprocessor_factory = src.preprocessing.PreprocessorFactory("dummy")

    def run(self) -> None:
        evaluator = src.Evaluator(self._preprocessor_factory.create())
        mae = evaluator.evaluate()

        print(f"MAE: {mae}")
