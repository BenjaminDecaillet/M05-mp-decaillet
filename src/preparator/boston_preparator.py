from src.preparator import BasePreparator


class BostonPreparator(BasePreparator):
    def __init__(self, source: str):
        sep = None
        sources = []
        if source == 'file':
            sources.append('data/housing.data')
        else:
            sources.append(
                'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data')
        column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                        'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
        delim_whitespace = True
        super().__init__(sources=sources, sep=sep, src_type=source, type='boston houses',
                         columns=column_names, delim_whitespace=delim_whitespace)
