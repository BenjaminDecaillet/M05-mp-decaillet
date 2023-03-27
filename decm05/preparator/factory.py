import decm05.preparator
from decm05.preparator import Preparator


class PreparatorFactory:
    def __init__(self, type: str, file_or_url: str):
        if type not in self.allowed_types:
            raise ValueError(f"Unknown preparator type '{type}'")
        if file_or_url not in self.allowed_file_or_url:
            raise ValueError(f"Unknown source type '{file_or_url}'")
        self._types = self.allowed_types if type == "*" else [type]
        self._file_or_url = file_or_url

    def create_many(self) -> list[Preparator]:
        preparators = []
        for type in self._types:
            if type == "boston":
                preparators.append(decm05.preparator.BostonPreparator(self._file_or_url))
                continue
            if type == "red-wine":
                preparators.append(decm05.preparator.RedWinePreparator(self._file_or_url))
                continue
            if type == "white-wine":
                preparators.append(decm05.preparator.WhiteWinePreparator(self._file_or_url))
                continue
            if type == "wines":
                preparators.append(decm05.preparator.WinePreparator(self._file_or_url))
                continue
        return preparators

    @classmethod
    @property
    def allowed_types(cls) -> list[str]:
        return ["boston", "red-wine", "white-wine", "wines", "*"]

    @classmethod
    @property
    def allowed_file_or_url(cls) -> list[str]:
        return ["file", "url"]
