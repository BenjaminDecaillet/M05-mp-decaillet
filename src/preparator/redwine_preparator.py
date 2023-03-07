from src.preparator import BasePreparator


class RedWinePreparator(BasePreparator):
    def __init__(self, source: str):
        sep = ';'
        sources = []
        if source == 'file':
            sources.append('data/winequality-red.csv')
        else:
            sources.append(
                'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv')
        column_names = [
            'fixed acidity',
            'volatile acidity',
            'citric acid',
            'residual sugar',
            'chlorides',
            'free sulfur dioxide',
            'total sulfur dioxide',
            'density',
            'pH',
            'sulphates',
            'alcohol',
            'quality']
        delim_whitespace = False
        super().__init__(sources=sources, sep=sep, src_type=source, type='red wine',
                         columns=column_names, delim_whitespace=delim_whitespace)
