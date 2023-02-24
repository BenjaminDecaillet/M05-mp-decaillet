class Evaluator():
    def __init__(self):
        pass

    def evaluate(self):
        self._prepare_data()

        self._preprocess_data()

        self._train_model()

        return self._evaluate_model()

    # region placeholder private methods # TODO remove when corresponding IoD is implemented

    @classmethod
    def _prepare_data(cls):
        pass

    @classmethod
    def _preprocess_data(cls):
        pass

    @classmethod
    def _train_model(cls):
        pass

    @classmethod
    def _evaluate_model(cls):
        return 42

    # endregion placeholder private methods
