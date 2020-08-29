import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_argmaxmin(x, window=10):
    """
    The difference between moving window index of maximum along axis 0 and moving window index of minimum along axis 0.

    Parameters
    ----------
    x: Matrix
    window: default 10, integer

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    assert window >= 1
    x_ = x.copy()
    window = int(window)
    ret = bn.move_argmin(x, window, axis=0) - bn.move_argmax(x, window, axis=0)
    return constructor_like(ret, x_)