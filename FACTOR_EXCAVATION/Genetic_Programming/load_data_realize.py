from markbaka.math import *
from markbaka.cross_section import *
from markbaka.element import *
from markbaka.time_series import *
import scipy.io as sio
import time


def data_realize(GP_Index, Expression_Index):
    """
    Realize the expression and save the data in `.mat` form.

    Parameters
    ----------
    GP_Index: the index of GP according to the result csv
    Expression_Index: the index of expression according to the result csv

    """
    start_time = time.time()
    ret = factor_record.loc[GP_Index].loc[Expression_Index]['Expressions']
    print('Ready to realize `%s`...' % ret)
    factor = eval(ret)
    end_time_realize = time.time()
    print('Success.')
    print('Factor:')
    print(factor)
    print('Time cost: %.2fs' % (end_time_realize-start_time))
    print('Ready to save factor...')
    sio.savemat('factor_result/factor_' + str(GP_Index) + '_' + str(Expression_Index) + '.mat',
                {'factor_' + str(GP_Index) + '_' + str(Expression_Index): factor})
    print('Success.')
    end_time = time.time()
    print('Total time cost: %.2fs\n' % (end_time-start_time))


factor_record = pd.read_csv('factor_result/Factor_Expressions.csv', index_col=['GP_Index', 'Expression_Index'],
                            parse_dates=['Date'])
OPEN = np.load('database/OpenPrice.npy')
CLOSE = np.load('database/ClosePrice.npy')
HIGH = np.load('database/HighPrice.npy')
LOW = np.load('database/LowPrice.npy')
VOLUME = np.load('database/Volume.npy')
AMOUNT = np.load('database/StockAmount.npy')