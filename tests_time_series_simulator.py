from time_series_simulator import TimeSeriesSimulator

import pytest

@pytest.fixture(scope='module')
def time_series_simulator():

    ts_simulator = TimeSeriesSimulator()
    ts_simulator.load_parameters(filename="parameters_set_1.json",
                                 path="/home/louis/Documents/codes/ARIMA_Box_Jenkins_method/")

    return ts_simulator


def test_inital_number_of_time_step(time_series_simulator):
    assert time_series_simulator._number_time_steps == 1000


def test_generate_time_series_not_none(time_series_simulator):

    time_series_simulator.generate_time_series()

    assert time_series_simulator._components.trend is not None
    assert time_series_simulator._components.noise is not None
    assert time_series_simulator._components.seasonality is not None
    assert time_series_simulator._components.observation is not None

