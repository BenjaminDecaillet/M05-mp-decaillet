from sklearn import preprocessing

from src.preprocessing import SkLearnPreprocessorBase


class PolynomialPreprocessor(SkLearnPreprocessorBase):
    def __init__(self, **polynomial_features_kwargs):
        super().__init__()
        self._polynomial_features_kwargs = polynomial_features_kwargs

    @property
    def name(self) -> str:
        return "polynomial"

    def _get_scaler(self):
        return preprocessing.PolynomialFeatures(**self._polynomial_features_kwargs)

    def _get_scaled_columns_names(self) -> list[str]:
        return self._scaler.get_feature_names_out(self._columns)
