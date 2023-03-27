from sklearn import preprocessing

from decm05.preprocessing import SkLearnPreprocessorBase


class MinMaxPreprocessor(SkLearnPreprocessorBase):
    @property
    def name(self) -> str:
        return "min-max"

    def _get_scaler(self):
        return preprocessing.MinMaxScaler()
