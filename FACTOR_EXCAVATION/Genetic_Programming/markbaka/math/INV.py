from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def INV(x):
    """
    1 / x

    Parameters
    ----------
    x: matrix

    Returns
    -------
    Matrix

    Notes
    -----
    0 needs attention.
    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    x[x==0] = np.nan
    ret = 1 / x
    return constructor_like(ret, x_)