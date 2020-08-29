import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_zscore(x, window=10):
    """
    The moving window zscore of x along axis 0.

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
    x = constructor_like(x)

    temp_mean = bn.move_mean(x, window=window, axis=0)
    temp = x - temp_mean
    temp_std = bn.move_std(x, window=window, axis=0)
    temp_std[temp_std==0] = np.nan
    ret = temp / temp_std
    return constructor_like(ret, x_)