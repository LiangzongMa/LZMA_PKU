import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *
from .ts_corr import *
from .ts_delay import *


def ts_autocorr(x, window=10, lag=1):
    """
    The correlation of the recent data of x and the past data of x.

    Parameters
    ----------
    x: Matrix
    y: Matrix
    window: default 10, integer
    lag: default 1, integer

    Returns
    -------
    Matrix

    Notes
    -----
    * Although it is feasible to use the command `x.rolling(window).corr(y)` to calculate, it is extremely slow.
    * Precision problem occurs and the code solves the problem by comparing the absolute value of element with
      1e-5. Elements whose absolute value is smaller than 1e-5 is assigned to be 0.
    * To deal with `NAN`, the original version of function contains code as follows
      `x[np.isnan(y)] = np.nan`
      `y[np.isnan(x)] = np.nan`
      which has the hidden trouble of changing the original value of x and y.
      The new version has already dealt with the problem.
    """

    assert is_matrix(x)
    assert window >= 1
    assert lag >= 1
    window = int(window)
    lag = int(lag)
    return ts_corr(x, ts_delay(x, lag), window=window)