from statsmodels.tsa.stattools import adfuller

def show_adfuller_analysis(time_serie):

    adfuller_result = adfuller(time_serie)

    print('ADF Statistic: %f' % adfuller_result[0])
    print('p-value: %f' % adfuller_result[1])
    print('Critical Values:')
    for key, value in adfuller_result[4].items():
        print('\t%s: %.3f' % (key, value))

