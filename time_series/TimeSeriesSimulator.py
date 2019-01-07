import numbers
import numpy as np

from time_series.TimeSeriesComponents import TimeSeriesComponents
from time_series.TimeSeriesSimulatorParameters import TimeSeriesSimulatorParameters

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
