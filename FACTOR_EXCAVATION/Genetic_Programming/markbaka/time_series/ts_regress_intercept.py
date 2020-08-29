import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_regress_intercept(x, y, window=10):
    """
    The moving window regression intercept of x and y.

    Parameters
    ----------
    y: Matrix
    x: Matrix
    window: default 10, integer

    Returns
    -------
    Matrix

    Notes
    -----
    * y is the explained variable.
    * To deal with `NAN`, the original version of function contains code as follows
      `x[np.isnan(y)] = np.nan`
      `y[np.isnan(x)] = np.nan`
      which has the hidden trouble of change the original value of x and y.
      The new version has already dealt with the problem.
    * Precision problem occurs and the code below solving the problem by comparing the absolute value of element with
      1e-5. Elements whose absolute value is smaller than 1e-5 is assigned to be 0.

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
    xx = x * x
    xy_ts_sum = bn.move_sum(xy, window=window, axis=0)
    x_bar = bn.move_mean(x, window=window, axis=0)
    y_bar = bn.move_mean(y, window=window, axis=0)
    xx_ts_sum = bn.move_sum(xx, window=window, axis=0)
    up = xy_ts_sum - window * x_bar * y_bar
    down = xx_ts_sum - window * x_bar * x_bar

    # deal with precision problem
    nan_down = np.isnan(down)
    down[nan_down] = 0
    down[np.abs(down) < 1e-5] = np.nan
    nan_up = np.isnan(up)
    up[nan_up] = 0
    up[np.abs(up) < 1e-5] = 0
    up[nan_up] = np.nan
    #

    beta_hat = up / down
    intercept_hat = y_bar - beta_hat * x_bar
    return constructor_like(intercept_hat, x_)
