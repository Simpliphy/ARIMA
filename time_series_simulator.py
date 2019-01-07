import json
import numbers
import numpy as np

class TimeSeriesSimulator(object):

    def __init__(self):

        """
        Initial implementation:

        -one seasonal component
        -gaussian noise
        -linear trend
        -additive components
        """

        self._number_time_steps = 1000
        self._time_steps = np.linspace(0, 100, self._number_time_steps)
        self._components = TimeSeriesComponents()
        self._parameters = TimeSeriesSimulatorParameters()

    def _generate_linear_trend(self):

        self._components.trend = self._parameters.initial_value + self._time_steps*self._parameters.growth_rate

    def _generate_gaussian_noise(self):

        self._components.noise = np.random.normal(0, self._parameters.std_deviation, self._number_time_steps)

    def _generate_seasonal_component(self):

        seasonal_component_list = list()

        for index_time_step in range(self._number_time_steps):

            seasonal_period = len(self._parameters.seasonal_template)
            index_in_season = index_time_step % seasonal_period
            value = self._parameters.seasonal_template[index_in_season]

            seasonal_component_list.append(value)

        self._components.seasonality = np.array(seasonal_component_list)

    def generate_time_series(self):

        self._generate_linear_trend()
        self._generate_gaussian_noise()
        self._generate_seasonal_component()
        self._sum_all_components()

    def _sum_all_components(self):

        self._components.observation = self._components.trend + self._components.seasonality + self._components.noise

    def load_parameters(self, filename, path):

        self._parameters.load(filename, path)



class TimeSeriesComponents(object):


    def __init__(self):

        self._trend = None
        self._seasonality = None
        self._noise = None
        self._observation = None

    @property
    def observation(self):
        return self._observation

    @observation.setter
    def observation(self, value):
        self._observation = value

    @property
    def trend(self):
        return self._trend

    @trend.setter
    def trend(self, value):
        self._trend = value

    @property
    def seasonality(self):
        return self._seasonality

    @seasonality.setter
    def seasonality(self, value):
        self._seasonality = value

    @property
    def noise(self):
        return self._noise

    @noise.setter
    def noise(self, value):
        self._noise = value


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