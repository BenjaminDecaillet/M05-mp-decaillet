import pkg_resources

from decm05.preparator import BasePreparator


class _BaseWinePreparator(BasePreparator):
    def __init__(self, file_or_url: str, include_red: bool, include_white: bool):
        assert include_red or include_white

        sources = []
        if file_or_url == 'file':
            if include_red:
                sources.append(pkg_resources.resource_filename('decm05', 'data/winequality-red.csv'))
            if include_white:
                sources.append(pkg_resources.resource_filename('decm05', 'data/winequality-white.csv'))
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
    def __init__(self, file_or_url: str):
        super().__init__(file_or_url, include_red=True, include_white=False)

    @property
    def name(self) -> str:
        return "red-wine"


class WhiteWinePreparator(_BaseWinePreparator):
    def __init__(self, file_or_url: str):
        super().__init__(file_or_url, include_red=False, include_white=True)

    @property
    def name(self) -> str:
        return "white-wine"


class WinePreparator(_BaseWinePreparator):
    def __init__(self, file_or_url: str):
        super().__init__(file_or_url, include_red=True, include_white=True)

    @property
    def name(self) -> str:
        return "wines"
