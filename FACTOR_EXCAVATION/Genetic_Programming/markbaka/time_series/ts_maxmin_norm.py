import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_maxmin_norm(x, window=10):
    """
    The moving window adjusted zscore of x along axis 0.
    The meaning of adjusted zscore is noted in `Notes`.

    Parameters
    ----------
    x: Matrix
    window: default 10, integer

    Returns
    -------
    Matrix

    Notes
    -----
    * Adjusted score is defined as
      `(x-ts_min(x, window)) / (ts_max(x, window) - ts_min(x, window))`
    * The meaning of function `ts_min` and `ts_max` can be found in the doc of the two functions.

    """
    assert is_matrix(x)
    assert window >= 1
    x_ = x.copy()
    x = constructor_like(x)
    window = int(window)
    temp_1 = bn.move_max(x, window=window, axis=0)
    temp_2 = bn.move_min(x, window=window, axis=0)
    temp_2[temp_2==0] = np.nan
    ret = (x - temp_2) / (temp_1 - temp_2)
    return constructor_like(ret, x_)
