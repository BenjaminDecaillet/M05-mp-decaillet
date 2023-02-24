import unittest.mock

from src import *


class TestService(unittest.TestCase):
    def test_runs(self) -> None:
        service = Service()

        with unittest.mock.patch('builtins.print') as mock_print:
            service.run()

        mock_print.assert_called_once_with('MAE: 42')
