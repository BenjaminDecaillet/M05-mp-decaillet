import src.preprocessing
from src.preprocessing import Preprocessor


class PreprocessorFactory:
    def __init__(self, type: str, polynomial_kwargs: dict = None):
        if type not in self.allowed_types:
            raise ValueError(f"Unknown preprocessor type '{type}'")
        if type != "polynomial" and polynomial_kwargs is not None:
            raise ValueError("polynomial_kwargs should be None for non-polynomial preprocessors")
        if polynomial_kwargs is None:
            polynomial_kwargs = {}
        if not isinstance(polynomial_kwargs, dict):
            raise TypeError("polynomial_kwargs should be a dict")
        self._types = [type]
        self._polynomial_kwargs = polynomial_kwargs

    def create_many(self) -> list[Preprocessor]:
        preprocessors = []
        for type in self._types:
            if type == "min-max":
                preprocessors.append(src.preprocessing.MinMaxPreprocessor())
                continue
            if type == "standard":
                preprocessors.append(src.preprocessing.StandardPreprocessor())
                continue
            if type == "polynomial":
                preprocessors.append(src.preprocessing.PolynomialPreprocessor(**self._polynomial_kwargs))
                continue
        return preprocessors

    @classmethod
    @property
    def allowed_types(cls) -> list[str]:
        return ["min-max", "standard", "polynomial"]
