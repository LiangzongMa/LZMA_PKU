import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *
from .ts_delay import *


def ts_pct(x, window=1):
    """
    Calculates the changing percentage of a DataFrame element compared with another element in the DataFrame of the same
    column with an optional variable `window`.

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
    temp = ts_delay(x, window)  # down
    temp[temp==0] = np.nan
    ret = x / temp - 1
    return constructor_like(ret, x_)