
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