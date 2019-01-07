import matplotlib.pyplot as plt

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

    def show(self):

        assert self._noise is not None
        assert self._observation is not None
        assert self._seasonality is not None
        assert self._trend is not None

        x = range(len(self._noise))

        plt.subplot(411)
        plt.plot(x, self._observation)
        plt.ylabel('observation')
        plt.grid(True)
        plt.gca().xaxis.grid(True, which='minor')  # minor grid on too

        plt.subplot(412)
        plt.plot(x, self._seasonality)
        plt.ylabel('seasonality')
        plt.grid(True)
        plt.gca().xaxis.grid(True, which='minor')  # minor grid on too

        plt.subplot(413)
        plt.plot(x, self._trend)
        plt.ylabel('trend')
        plt.grid(True)
        plt.gca().xaxis.grid(True, which='minor')  # minor grid on too

        plt.subplot(414)
        plt.plot(x, self._noise)
        plt.ylabel('noise')
        plt.grid(True)
        plt.gca().xaxis.grid(True, which='minor')  # minor grid on too


        plt.tight_layout()
        plt.show()



