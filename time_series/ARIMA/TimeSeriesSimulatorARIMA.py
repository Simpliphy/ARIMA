import numpy as np

from time_series.ARIMA.Components import Components
from time_series.ARIMA.TimeSeriesSimulatorParametersARIMA import TimeSeriesSimulatorParameters

class TimeSeriesSimulatorARIMA(object):

    def __init__(self):

        self._number_time_steps = 30
        self._time_steps = np.array(range(self._number_time_steps))
        self._components = Components()
        self._parameters = TimeSeriesSimulatorParameters()

    def load_parameters(self, filename, path):
        self._parameters.load(filename, path)

    def generate_time_series(self):

        assert self._parameters.isInitialised(), "The parameters must be initialized"

        self._components.initialize_to_zeros(self._number_time_steps)

        self._components.observation_values[0] = self._parameters.initial_value
        for current_time_index in range(1, self._number_time_steps):

            current_value = 0
            for autoregressive_part in self._parameters.autoregressive_lag_coefficients_pairs:

                lag = autoregressive_part["lag"]
                coefficient = autoregressive_part["coefficient"]

                value = coefficient * self._components.get_observation_value_at_lag(current_time_index, lag)

                current_value += value

            for moving_average_part in self._parameters.moving_average_lag_coefficients_pairs:

                lag = moving_average_part["lag"]
                coefficient = moving_average_part["coefficient"]

                value = coefficient * self._components.get_noise_value_at_lag(current_time_index, lag)

                current_value += value

            current_noise = np.random.normal(loc=0, scale=self._parameters.std_deviation, size=1)
            current_value += current_noise

            self._components.observation_values[current_time_index] = current_value
            self._components.noise_values[current_time_index] = current_noise

    @property
    def components(self):
        return self._components

    @property
    def parameters(self):
        return self._parameters



