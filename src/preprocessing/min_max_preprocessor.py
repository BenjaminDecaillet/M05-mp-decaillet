from sklearn import preprocessing

from src.preprocessing import SkLearnPreprocessorBase


class MinMaxPreprocessor(SkLearnPreprocessorBase):
    def _get_scaler(self):
        return preprocessing.MinMaxScaler()
