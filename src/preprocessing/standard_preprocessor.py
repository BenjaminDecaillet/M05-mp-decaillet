from sklearn import preprocessing

from src.preprocessing import SkLearnPreprocessorBase


class StandardPreprocessor(SkLearnPreprocessorBase):
    def _get_scaler(self):
        return preprocessing.StandardScaler()
