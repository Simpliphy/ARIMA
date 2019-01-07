import json

class TimeSeriesSimulatorParameters(object):

    def __init__(self):

        self._growth_rate = None
        self._initial_value = None
        self._std_deviation = None
        self._seasonal_template = None

    def load(self, filename, path):

        with open(path + filename, "r") as read_file:
            parameters_dict = json.load(read_file)

        self._growth_rate = parameters_dict["growth_rate"]
        self._initial_value = parameters_dict["initial_value"]
        self._std_deviation = parameters_dict["std_deviation"]
        self._seasonal_template = parameters_dict["seasonal_template"]

    @property
    def growth_rate(self):
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value):
        assert isinstance(value, numbers.Real), "The growth rate need to be a real number."

        self._growth_rate = value

    @property
    def initial_value(self):
        return self._initial_value

    @initial_value.setter
    def initial_value(self, value):
        assert isinstance(value, numbers.Real), "The initial value need to be a real number."

        self._initial_value = value

    @property
    def std_deviation(self):
        return self._std_deviation

    @std_deviation.setter
    def std_deviation(self, value):
        assert isinstance(value, numbers.Real), "The std deviation need to be a real number."
        assert value >= 0, "The standard deviation of the noise must be positive."

        self._std_deviation = value

    @property
    def seasonal_template(self):
        return self._seasonal_template

    @seasonal_template.setter
    def seasonal_template(self, value):

        try:
            _ = iter(value)

        except TypeError:
            raise TypeError("The seasonal template must be iterable.")

        else:
            self._seasonal_template = value