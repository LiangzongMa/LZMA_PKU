from ..constructor_like import *
from ..is_matrix import *


def cs_demean(x):
    """
    x minus the avarage of x along axis 1

    Parameters
    ----------
    x: Matrix

    Returns
    -------
    Matrix

    """

    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)
    ret = x - np.nanmean(x, axis=1).reshape(-1, 1)
    return constructor_like(ret, x_)