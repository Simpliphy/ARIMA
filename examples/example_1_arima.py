from time_series.ARIMA.TimeSeriesSimulatorARIMA import TimeSeriesSimulatorARIMA


if __name__ == "__main__":

    ts_simulator = TimeSeriesSimulatorARIMA()
    ts_simulator.load_parameters(filename="parameters_set_1_arima.json",
                                     path="/home/louis/Documents/codes/ARIMA_Box_Jenkins_method/")

    ts_simulator.generate_time_series()
    ts_simulator.components.show()
