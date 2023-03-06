from random import randint

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from src.estimating import Estimator
from src.preprocessing import Preprocessor


class Evaluator():
    def __init__(self,
                 preprocessor: Preprocessor,
                 estimator: Estimator,
                 evaluation_count: int):
        if not isinstance(preprocessor, Preprocessor):
            raise TypeError("preprocessor must be a Preprocessor")
        self._preprocessor = preprocessor

        if not isinstance(estimator, Estimator):
            raise TypeError("estimator must be an Estimator")
        self._estimator = estimator

        if not isinstance(evaluation_count, int):
            raise TypeError("evaluation_count must be an int")
        if not evaluation_count >= 1:
            raise ValueError("evaluation_count must be >= 1")
        self._evaluation_count = evaluation_count

    def evaluate(self):
        dataset = self._prepare_data()
        mean_absolute_errors = [self._evaluate_once(**dataset) for _ in range(self._evaluation_count)]
        return sum(mean_absolute_errors) / len(mean_absolute_errors)

    def _evaluate_once(self, dataset: pd.DataFrame, features_names: list[str], targets_names: list[str]) -> float:
        """Trains and evaluates the model once.

        Returns:
            float: the mean absolute error of the model
        """
        assert isinstance(dataset, pd.DataFrame)
        assert isinstance(features_names, list) and all(name in dataset.columns for name in features_names)
        assert isinstance(targets_names, list) and all(name in dataset.columns for name in targets_names)

        training_set, test_set = train_test_split(dataset, test_size=0.5, random_state=randint(0, 1000))

        preprocessed_training_features = self._preprocessor.fit_transform(training_set[features_names])
        preprocessed_test_features = self._preprocessor.transform(test_set[features_names])

        self._estimator.fit(preprocessed_training_features, training_set[targets_names])
        predictions = self._estimator.predict(preprocessed_test_features)

        return mean_absolute_error(test_set[targets_names], predictions)

    # region placeholder private methods # TODO remove when corresponding IoD is implemented

    @classmethod
    def _prepare_data(cls):
        return {
            "dataset": pd.DataFrame(data={
                "foo": range(0, 5),
                "bar": range(5, 10),
                "baz": range(10, 15)
            }),
            "features_names": ["foo", "bar"],
            "targets_names": ["baz"]
        }

    # endregion placeholder private methods
