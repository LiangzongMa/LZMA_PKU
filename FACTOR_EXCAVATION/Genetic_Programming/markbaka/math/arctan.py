from ..constructor_like import *
from ..is_matrix import *
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def arctan(x):
    """
    arctan(x)

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
    ret = np.arctan(x)
    return constructor_like(ret, x_)