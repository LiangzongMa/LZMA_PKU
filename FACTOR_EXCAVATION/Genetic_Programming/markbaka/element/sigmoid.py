from ..constructor_like import *
from ..is_matrix import *


def sigmoid(x):
    """
    Sigmoid function.

    Parameters
    ----------
    x: Matrix

    Returns
    -------
    Matrix
    
    Notes
    -----
    * Sigmoid of x is defined as `1.0 / (1.0 + np.exp(-x))`,
      which may cause `RuntimeWarning: overflow encountered in exp`.
    * Calculate `.5 * (1.0 + np.tanh(.5 * x))` instead.

    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    ret = .5 * (1.0 + np.tanh(.5 * x))
    return constructor_like(ret, x_)