import pytest

from time_series.AdditiveDecomposition.TimeSeriesSimulator import TimeSeriesSimulator

@pytest.fixture(scope='module')
def time_series_simulator():

    ts_simulator = TimeSeriesSimulator()
    ts_simulator.load_parameters(filename="parameters_set_1.json",
                                 path="/home/louis/Documents/codes/ARIMA_Box_Jenkins_method/")

    return ts_simulator


def test_inital_number_of_time_step(time_series_simulator):
    assert False # default value


def test_generate_time_series_not_none(time_series_simulator):

    time_series_simulator.generate_time_series()

    assert False

