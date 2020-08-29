from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def mul(x, y):
    """
    x * y

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
    ret = x * y
    return constructor_like(ret, x_)