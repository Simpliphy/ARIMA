import numpy as np
import matplotlib.pyplot as plt

class Components(object):

    def __init__(self):

        self._observation_values = None
        self._noise_values = None

    @property
    def observation_values(self):
        return self._observation_values

    @observation_values.setter
    def observation_values(self, value):
        self._observation_values = value

    @property
    def noise_values(self):
        return self._noise_values

    @noise_values.setter
    def noise_values(self, value):
        self._noise_values = value

    def initialize_to_zeros(self, number_of_observations):

        self._observation_values = np.zeros(number_of_observations)
        self._noise_values = np.zeros(number_of_observations)

    def get_observation_value_at_lag(self, current_index, lag):

        assert current_index < len(self.observation_values)
        assert lag > 0
        assert current_index > 0
        assert isinstance(lag, int)
        assert isinstance(current_index, int)

        index_to_get = current_index - lag
        if index_to_get < 0:
            return 0
        else:
            return self._observation_values[index_to_get]

    def get_noise_value_at_lag(self, current_index, lag):

        assert current_index < len(self._noise_values)
        assert lag > 0
        assert current_index > 0
        assert isinstance(lag, int)
        assert isinstance(current_index, int)

        index_to_get = current_index - lag
        if index_to_get < 0:
            return 0
        else:
            return self._noise_values[index_to_get]

    def remove_intial_values(self, initial_values_length):

        self._observation_values = self._observation_values[initial_values_length:]
        self._noise_values = self._noise_values[initial_values_length:]

    def show(self):

        assert self._noise_values is not None
        assert self._observation_values is not None

        x = range(len(self._noise_values))

        plt.subplot(211)
        plt.plot(x, self._observation_values)
        plt.ylabel('observation')
        plt.grid(True)
        plt.gca().xaxis.grid(True, which='minor')  # minor grid on too

        plt.subplot(212)
        plt.plot(x, self._noise_values)
        plt.ylabel('noise')
        plt.xlabel("time step")
        plt.grid(True)
        plt.gca().xaxis.grid(True, which='minor')  # minor grid on too

        plt.tight_layout()
        plt.show()
