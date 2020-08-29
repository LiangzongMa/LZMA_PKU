import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *
import talib


def ts_wma(x, window=10):
    """
    The moving window average of x with weight along axis 0.

    Parameters
    ----------
    x: Matrix
    window: default 10, integer

    Returns
    -------
    Matrix

    Notes
    -----
    Linear weighted sum.

    """
    import talib
    assert is_matrix(x)
    assert window >= 1
    x_ = x.copy()
    window = int(window)
    if window != 1:
        if isinstance(x, np.ndarray):
            x = pd.DataFrame(x)
        ret = x.rolling(window).apply(lambda y: talib.WMA(y, timeperiod=window)[-1], raw=True)
    else:
        ret = x
    return constructor_like(ret, x_)