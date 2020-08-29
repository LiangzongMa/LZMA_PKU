import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *
from .ts_delay import *

def ts_delta(x, window=1):
    """
    Calculates the difference of a DataFrame element compared with another element in the DataFrame of the same column.

    Parameters
    ----------
    x: Matrix
    window: default 1, integer

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    assert window >= 1
    x_ = x.copy()
    x = constructor_like(x).astype(float)
    window = int(window)
    ret = x - ts_delay(x, window)
    return constructor_like(ret, x_)