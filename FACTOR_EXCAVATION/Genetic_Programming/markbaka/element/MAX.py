from ..constructor_like import *
from ..is_matrix import *


def MAX(x, y):
    """
    Calculate the maximum of x and y.

    Parameters
    ----------
    x: Matrix
    y: Matrix

    Returns
    -------
    A matrix containing the element-wise maximum.

    """
    assert is_matrix(x)
    assert is_matrix(y)
    x_ = x.copy()
    x = constructor_like(x)
    y = constructor_like(y)
    ret = np.maximum(x, y)
    return constructor_like(ret, x_)