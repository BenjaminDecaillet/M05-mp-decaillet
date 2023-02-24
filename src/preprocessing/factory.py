import src.preprocessing
from src.preprocessing import Preprocessor


class PreprocessorFactory:
    def __init__(self, type: str):
        if type not in {"dummy"}:
            raise ValueError(f"Unknown preprocessor type '{type}'")
        self._type = type

    def create(self) -> Preprocessor:
        if self._type == "dummy":
            return src.preprocessing.DummyPreprocessor()
