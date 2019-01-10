def lag_difference(time_serie, lag=1):

    return time_serie[lag:] - time_serie[:-lag]


