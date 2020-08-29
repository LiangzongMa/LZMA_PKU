import bottleneck as bn  # a package using C++ to calculate, which is faster compared by python
from ..is_matrix import *
from ..constructor_like import *


def ts_prod(x, window=3):
    """
    The moving window cumulative product of x along axis 0.

    Parameters
    ----------
    x: Matrix
    window: default 3, integer

    Returns
    -------
    Matrix

    """

    def _rwindows(a, window):
        # https://stackoverflow.com/questions/45254174/how-do-pandas-rolling-objects-work
        if a.ndim == 1:
            a = a.reshape(-1, 1)
        shape = a.shape[0] - window + 1, window, a.shape[-1]
        strides = (a.strides[0],) + a.strides
        windows = np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides, writeable=False)
        return np.squeeze(windows)

    def get_rolling(x, window, fill_value):
        shape_0 = x.shape[0] + window - 1
        shape = (shape_0, x.shape[1]) if x.ndim == 2 else (shape_0,)

        z = np.full(shape, fill_value)
        z[window - 1:] = x  # feasible for both pandas and numpy
        return _rwindows(z, window)

    assert is_matrix(x)
    assert window >= 1
    x_ = x.copy()
    window = int(window)

    if window > 1:
        ret = get_rolling(x, window, np.nan)
        ret = ret.prod(axis=1)
    else:
        ret = x
    return constructor_like(ret, x_)