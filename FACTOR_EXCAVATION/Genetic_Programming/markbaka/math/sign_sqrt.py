from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def sign_sqrt(x):
    """
    x / abs(x) * sqrt(abs(x))

    Parameters
    ----------
    x: matrix

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    zero_matrix = (x == 0)
    x[zero_matrix] = np.nan
    ret = x / abs(x) * np.sqrt(np.abs(x))
    ret[zero_matrix] = 0
    return constructor_like(ret, x_)