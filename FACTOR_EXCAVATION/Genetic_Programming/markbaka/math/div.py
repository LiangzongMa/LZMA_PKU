from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def div(x, y):
    """
    x / y

    Parameters
    ----------
    x: Matrix
    y: Matrix or Number

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    if is_matrix(y):
        y = constructor_like(y)
        y[y==0] = np.nan
    elif y == 0:
        y = np.nan
    ret = x / y
    return constructor_like(ret, x_)