from genetic_programming_settings import *


def standardize(data):
    """
    Standardize the data.

    Parameters
    ----------
    data

    Returns
    -------
    Matrix

    """
    return (data - np.nanmean(data).reshape(-1, 1)) / np.nanstd(data).reshape(-1, 1)


print('Loading Data...')

OPEN = np.load('database/OpenPrice.npy')
CLOSE = np.load('database/ClosePrice.npy')
HIGH = np.load('database/HighPrice.npy')
LOW = np.load('database/LowPrice.npy')
VOLUME = np.load('database/Volume.npy')
AMOUNT = np.load('database/StockAmount.npy')


''''
print('Standardize...')
OPEN = standardize(OPEN)
CLOSE = standardize(CLOSE)
HIGH = standardize(HIGH)
LOW = standardize(LOW)
VOLUME = standardize(VOLUME)
AMOUNT = standardize(AMOUNT)
'''

print('Success!')

ret = pd.DataFrame(OPEN).pct_change(periods=1).shift(-1).values
ret[np.isinf(ret)] = np.nan

OPEN = OPEN[date_range]
CLOSE = CLOSE[date_range]
HIGH = HIGH[date_range]
LOW = LOW[date_range]
VOLUME = VOLUME[date_range]
AMOUNT = AMOUNT[date_range]
ret = ret[date_range]

