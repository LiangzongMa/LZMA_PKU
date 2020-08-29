import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_rank(x, window=10):
    """
    The moving window rank of x along axis 0.

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
    ret = x.rolling(window).apply(lambda x: bn.rankdata(x, axis=0)[-1], raw=True)
    return constructor_like(ret, x_)