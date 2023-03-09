from src.preparator import BasePreparator


class _BaseWinePreparator(BasePreparator):
    def __init__(self, source: str, include_red: bool, include_white: bool):
        assert include_red or include_white

        sources = []
        if source == 'file':
            if include_red:
                sources.append('data/winequality-red.csv')
            if include_white:
                sources.append('data/winequality-white.csv')
        else:
            if include_red:
                sources.append('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv')
            if include_white:
                sources.append('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv')

        features_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                          'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
        targets_names = ['quality']
        super().__init__(sources, features_names, targets_names, sep=';')


class RedWinePreparator(_BaseWinePreparator):
    def __init__(self, source: str):
        super().__init__(source, include_red=True, include_white=False)


class WhiteWinePreparator(_BaseWinePreparator):
    def __init__(self, source: str):
        super().__init__(source, include_red=False, include_white=True)


class WinePreparator(_BaseWinePreparator):
    def __init__(self, source: str):
        super().__init__(source, include_red=True, include_white=True)
