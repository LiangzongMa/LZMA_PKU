from ..constructor_like import *
from ..is_matrix import *
import bottleneck as bn


def cs_scale(x, k=1):
    """
    Scale x along axis 1 to make the sum of the abs of x along axis 1 equals to k

    Parameters
    ----------
    x: Matrix
    k: Number

    Returns
    -------
    Matrix

    """
    assert is_matrix(x)
    assert not is_matrix(k)
    x_ = x.copy()
    x = constructor_like(x)
    temp = np.nansum(np.abs(x), axis=1).reshape(-1, 1)
    temp[temp==0] = np.nan
    ret = k * x / temp
    return constructor_like(ret, x_)