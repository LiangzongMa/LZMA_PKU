import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_skew(x, window=10):
    """
    The moving window skewness of x along axis 0.

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
    if isinstance(x, np.ndarray):
        x = pd.DataFrame(x)
    ret = x.rolling(window).skew()
    return constructor_like(ret, x_)