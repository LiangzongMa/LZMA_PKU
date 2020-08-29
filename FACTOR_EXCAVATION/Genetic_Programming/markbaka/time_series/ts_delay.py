import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_delay(x, window=1):
    """
    Shift index by desired number of periods with an optional time `window`.

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
    x[window:, :] = x[:-window, :]
    x[:window, :] = np.nan
    return constructor_like(x, x_)
