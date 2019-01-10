import json

class TimeSeriesSimulatorParameters(object):

    def __init__(self):

        self._autoregressive_lag_coefficients_pairs = None
        self._moving_average_lag_coefficients_pairs = None
        self._initial_values = None

    def load(self, filename, path):

        with open(path + filename, "r") as read_file:
            parameters_dict = json.load(read_file)

        self._autoregressive_lag_coefficients_pairs = parameters_dict["autoregressive_lag_coefficients_pairs"]
        self._moving_average_lag_coefficients_pairs = parameters_dict["moving_average_lag_coefficients_pairs"]
        self._initial_values = parameters_dict["initial_values"]
        self._std_deviation = parameters_dict["std_deviation"]

    @property
    def autoregressive_lag_coefficients_pairs(self):
        return self._autoregressive_lag_coefficients_pairs

    @property
    def moving_average_lag_coefficients_pairs(self):
        return self._moving_average_lag_coefficients_pairs

    @property
    def initial_values(self):
        return self._initial_values

    @property
    def std_deviation(self):
        return self._std_deviation

    def isInitialised(self):

        if self._autoregressive_lag_coefficients_pairs is None:
            return False
        elif self._moving_average_lag_coefficients_pairs is None:
            return False
        elif self._initial_values is None:
            return False
        elif self._std_deviation is None:
            return False
        else:
            return True


"""
class LagCoefficientsPair(object):


    def __init__(self):

        self._lag = None
        self._coefficient = None

    @property
    def lag(self):
        return self._lag

    @lag.setter
    def lag(self, value):

        assert isinstance(value, int) , "the lag value provided must be an integer"
        assert value > 0, "the lag value provided must be greater than zero"

        self._lag = value

    @property
    def coefficient(self):
        return self._coefficient

    @coefficient.setter
    def coefficient(self, value):
        assert isinstance(value, numbers.Real), "the coefficient value provided must be a real number"

        self._coefficient = value
"""