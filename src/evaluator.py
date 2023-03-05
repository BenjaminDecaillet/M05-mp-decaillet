import pandas as pd

from src.preprocessing import Preprocessor


class Evaluator():
    def __init__(self, preprocessor: Preprocessor):
        if not isinstance(preprocessor, Preprocessor):
            raise TypeError("preprocessor must be a Preprocessor")
        self._preprocessor = preprocessor

    def evaluate(self):
        self._prepare_data()

        training_features = pd.DataFrame(data=[1], columns=["foo"])
        test_features = pd.DataFrame(data=[2], columns=["foo"])
        _ = self._preprocessor.fit_transform(training_features)
        _ = self._preprocessor.transform(test_features)

        self._train_model()

        return self._evaluate_model()

    # region placeholder private methods # TODO remove when corresponding IoD is implemented

    @classmethod
    def _prepare_data(cls):
        pass

    @classmethod
    def _train_model(cls):
        pass

    @classmethod
    def _evaluate_model(cls):
        return 42

    # endregion placeholder private methods
