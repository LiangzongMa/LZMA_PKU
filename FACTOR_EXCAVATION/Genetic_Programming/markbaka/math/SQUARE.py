from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def SQUARE(x):
    """
    x ^ 2

    Parameters
    ----------
    x

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    ret = np.square(x)
    return constructor_like(ret, x_)