from ..constructor_like import *
from ..is_matrix import *


def mean(x, y):
    """
    Calculate the average of x and y.

    Parameters
    ----------
    x: Matrix
    y: Matrix

    Returns
    -------
    A matrix containing the element-wise average.

    """
    assert is_matrix(x)
    assert is_matrix(y)
    x_ = x.copy()
    x = constructor_like(x)
    y = constructor_like(y)
    ret = (x + y) / 2.0
    return constructor_like(ret, x_)