import numpy as np
import pandas as pd

def standardize(data):
    return (data - np.nanmean(data).reshape(-1, 1)) / np.nanstd(data).reshape(-1, 1)

print('Loading Data...')

OPEN = np.load('database/OpenPrice.npy')
CLOSE = np.load('database/ClosePrice.npy')
HIGH = np.load('database/HighPrice.npy')
LOW = np.load('database/LowPrice.npy')
VOLUME = np.load('database/StockVolume.npy')
AMOUNT = np.load('database/Amount.npy')

print('Standardize...')
OPEN = standardize(OPEN)
CLOSE = standardize(CLOSE)
HIGH = standardize(HIGH)
LOW = standardize(LOW)
VOLUME = standardize(VOLUME)
AMOUNT = standardize(AMOUNT)

print('Success!')

ret = pd.DataFrame(OPEN).pct_change(periods=1).values
ret[np.isinf(ret)] = np.nan
ret[:-2] = ret[2:]
ret[-2:] = np.nan

