from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def sign_power(x, y):
    """
    x ^ y

    Parameters
    ----------
    x: Matrix
    y: Number

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    assert y >= 0
    x_ = x.copy()
    x = constructor_like(x)
    ret = x / np.abs(x) * np.power(np.abs(x), y)
    return constructor_like(ret, x_)