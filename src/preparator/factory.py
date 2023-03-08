import src.preparator
from src.preparator import Preparator


class PreparatorFactory:
    def __init__(self, type: str):
        if type not in {"boston"}:
            raise ValueError(f"Unknown preparator type '{type}'")
        self._type = type

    def create(self) -> Preparator:
        if self._type == "boston":
            return src.preparator.BostonPreparator()
