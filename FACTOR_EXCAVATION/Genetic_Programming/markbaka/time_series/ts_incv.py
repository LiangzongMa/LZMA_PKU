import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_incv(x, window=10):
    """
    The moving window reciprocal of coefficient of variation of x.

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
    temp = bn.move_mean(x, axis=0, window=window)
    temp_ = bn.move_std(x, axis=0, window=window)
    temp_[temp_==0] = np.nan
    ret = temp / temp_
    return constructor_like(ret, x_)