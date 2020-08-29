from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def sign_log(x):
    """
    x / abs(x) * log(abs(x))

    Parameters
    ----------
    x: Matrix

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    zero_matrix = (x == 0)
    x[zero_matrix] = np.nan
    ret = x / np.abs(x) * np.log(np.abs(x))
    return constructor_like(ret, x_)