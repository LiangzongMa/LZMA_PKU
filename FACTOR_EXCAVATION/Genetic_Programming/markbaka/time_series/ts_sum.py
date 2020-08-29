import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_sum(x, window=10):
    """
    The moving window accumulative total of x along axis 0.

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
    ret = bn.move_sum(x, axis=0, window=window)
    return constructor_like(ret, x_)