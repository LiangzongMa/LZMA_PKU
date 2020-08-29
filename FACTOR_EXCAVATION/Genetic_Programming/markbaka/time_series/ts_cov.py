import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_cov(x, y, window=10):
    """
    The moving covariance of x and y along axis 0.

    Parameters
    ----------
    x: Matrix
    y: Matrix
    window: default 10, integer

    Returns
    -------
    Matrix

    Notes
    -----
    * Although it is feasible to use the command `x.rolling(window).cov(y)` to calculate, it is extremely slow.
    * Precision problem occurs and the code solves the problem by comparing the absolute value of element with
      1e-5. Elements whose absolute value is smaller than 1e-5 is assigned to be 0.
    * Biased covariance (sample covariance)
    * To deal with `NAN`, the original version of function contains code as follows
      `x[np.isnan(y)] = np.nan`
      `y[np.isnan(x)] = np.nan`
      which has the hidden trouble of changing the original value of x and y.
      The new version has already dealt with the problem.
    """
    # x[np.isnan(y)] = np.nan
    # y[np.isnan(x)] = np.nan
    assert is_matrix(x)
    assert is_matrix(y)
    assert window >= 1
    x_ = x.copy()
    window = int(window)
    x = constructor_like(x)
    y = constructor_like(y)

    x[np.isnan(y)] = np.nan
    y[np.isnan(x)] = np.nan
    xy = x * y
    xy_bar = bn.move_mean(xy, axis=0, window=window)
    x_bar = bn.move_mean(x, axis=0, window=window)
    y_bar = bn.move_mean(y, axis=0, window=window)

    ret = xy_bar - x_bar * y_bar

    # deal with precision problem
    nan_matrix = np.isnan(ret)
    ret[nan_matrix] = 0
    ret[np.abs(ret) < 1e-5] = 0
    ret[nan_matrix] = np.nan
    #

    return constructor_like(ret, x_)