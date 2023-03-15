import src.preparator
from src.preparator import Preparator


class PreparatorFactory:
    def __init__(self, type: str, source: str):
        if type not in self.allowed_types:
            raise ValueError(f"Unknown preparator type '{type}'")
        if source not in self.allowed_sources:
            raise ValueError(f"Unknown source type '{source}'")
        self._types = [type]
        self._source = source

    def create_many(self) -> list[Preparator]:
        preparators = []
        for type in self._types:
            if type == "boston":
                preparators.append(src.preparator.BostonPreparator(self._source))
                continue
            if type == "red-wine":
                preparators.append(src.preparator.RedWinePreparator(self._source))
                continue
            if type == "white-wine":
                preparators.append(src.preparator.WhiteWinePreparator(self._source))
                continue
            if type == "wines":
                preparators.append(src.preparator.WinePreparator(self._source))
                continue
        return preparators

    @classmethod
    @property
    def allowed_types(cls) -> list[str]:
        return ["boston", "red-wine", "white-wine", "wines"]

    @classmethod
    @property
    def allowed_sources(cls) -> list[str]:
        return ["file", "url"]
