import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_kurt(x, window):
    """
    The moving winfow kurtosis of x along axis 0.

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
    ret = x.rolling(window).kurt()
    return constructor_like(ret, x_)