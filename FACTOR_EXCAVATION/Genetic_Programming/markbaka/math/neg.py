from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def neg(x):
    """
    -x

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
    ret = -x
    return constructor_like(ret, x_)