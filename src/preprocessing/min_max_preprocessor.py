from sklearn import preprocessing

from src.preprocessing import SkLearnPreprocessorBase


class MinMaxPreprocessor(SkLearnPreprocessorBase):
    @property
    def name(self) -> str:
        return "min-max"

    def _get_scaler(self):
        return preprocessing.MinMaxScaler()
