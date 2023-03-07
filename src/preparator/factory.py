import src.preparator
from src.preparator import Preparator


class PreparatorFactory:
    def __init__(self, type: str, source: str):
        if type not in {"wines", "white-wine", "red-wine", "boston"}:
            raise ValueError(f"Unknown preparator type '{type}'")
        if source not in {"file", "url"}:
            raise ValueError(f"Unknown source type '{source}'")
        self._source = source
        self._type = type

    def create(self) -> Preparator:
        if self._type == "white-wine":
            return src.preparator.WhiteWinePreparator(self._source)
        if self._type == "red-wine":
            return src.preparator.RedWinePreparator(self._source)
        if self._type == "wines":
            return src.preparator.WinePreparator(self._source)
        if self._type == "boston":
            return src.preparator.BostonPreparator(self._source)
