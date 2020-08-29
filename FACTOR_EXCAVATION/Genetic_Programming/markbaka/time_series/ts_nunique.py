import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_nunique(x, window=10):
    """
    The moving number of different values of x along axis 0.

    Parameters
    ----------
    x: Matrix
    window: default 10

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
    ret = x.rolling(window).apply(lambda y: len(set(y)), raw=True)
    return constructor_like(ret, x_)