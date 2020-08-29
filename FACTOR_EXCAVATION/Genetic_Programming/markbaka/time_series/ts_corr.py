import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_corr(x, y, window=10):
    """
    The moving correlation of x and y along axis 0.

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
    * Although it is feasible to use the command `x.rolling(window).corr(y)` to calculate, it is extremely slow.
    * Precision problem occurs and the code solves the problem by comparing the absolute value of element with
      1e-5. Elements whose absolute value is smaller than 1e-5 is assigned to be 0.
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
    x_bar = bn.move_mean(x, window=window, axis=0)
    y_bar = bn.move_mean(y, window=window, axis=0)
    xx = x * x
    yy = y * y
    xx_ts_sum = bn.move_sum(xx, window=window, axis=0)
    yy_ts_sum = bn.move_sum(yy, window=window, axis=0)
    xy_ts_sum = bn.move_sum(xy, window=window, axis=0)

    temp_1 = xx_ts_sum - window * x_bar * x_bar
    temp_2 = yy_ts_sum - window * y_bar * y_bar
    down_temp = temp_1 * temp_2

    # deal with precision problem
    down_temp[np.isnan(down_temp)] = 0  # a warning might occurs if directly run the code below
    down_temp[np.abs(down_temp) < 1e-5] = np.nan
    #

    down = np.sqrt(down_temp)

    up = xy_ts_sum - window * x_bar * y_bar
    # deal with precision problem
    nan_matrix = (np.isnan(up))
    up[nan_matrix] = 0  # a warning might occurs if directly run the code below
    up[np.abs(up) < 1e-5] = 0
    up[nan_matrix] = np.nan
    #

    ret = up / down
    return constructor_like(ret, x_)