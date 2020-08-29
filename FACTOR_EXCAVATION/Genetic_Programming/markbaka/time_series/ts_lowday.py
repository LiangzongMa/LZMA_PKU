import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_lowday(x, window=10):
    """
    The difference between moving window index of minimum along axis 0 and the position of the element.

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
    ret = bn.move_argmin(x, window, axis=0) + 1
    return constructor_like(ret, x_)
