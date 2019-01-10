import pytest

from time_series.ARIMA.TimeSeriesSimulatorARIMA import TimeSeriesSimulatorARIMA

@pytest.fixture(scope='module')
def time_series_simulator():

    ts_simulator = TimeSeriesSimulatorARIMA()
    ts_simulator.load_parameters(filename="parameters_set_1_arima.json",
                                 path="/home/louis/Documents/codes/ARIMA_Box_Jenkins_method/")

    return ts_simulator


def test_inital_reading_parameters(time_series_simulator):

    assert time_series_simulator.parameters.std_deviation == 40
    assert time_series_simulator.parameters.initial_values is not None


def test_generate_time_series_not_none(time_series_simulator):

    time_series_simulator.generate_time_series()

    assert time_series_simulator.components.noise_values is not None
    assert time_series_simulator.components.observation_values is not None

