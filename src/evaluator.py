import pandas as pd

from src.estimating import Estimator
from src.preprocessing import Preprocessor


class Evaluator():
    def __init__(self,
                 preprocessor: Preprocessor,
                 estimator: Estimator):
        if not isinstance(preprocessor, Preprocessor):
            raise TypeError("preprocessor must be a Preprocessor")
        self._preprocessor = preprocessor

        if not isinstance(estimator, Estimator):
            raise TypeError("estimator must be an Estimator")
        self._estimator = estimator

    def evaluate(self):
        self._prepare_data()

        training_features = pd.DataFrame(data=[1], columns=["foo"])
        training_targets = pd.DataFrame(data=[1], columns=["bar"])
        test_features = pd.DataFrame(data=[2], columns=["foo"])
        test_targets = pd.DataFrame(data=[2], columns=["bar"])

        preprocessed_training_features = self._preprocessor.fit_transform(training_features)
        preprocessed_test_features = self._preprocessor.transform(test_features)

        self._estimator.fit(preprocessed_training_features, training_targets)
        predictions = self._estimator.predict(preprocessed_test_features)

        return self._evaluate_model()

    # region placeholder private methods # TODO remove when corresponding IoD is implemented

    @classmethod
    def _prepare_data(cls):
        pass

    @classmethod
    def _evaluate_model(cls):
        return 42

    # endregion placeholder private methods
