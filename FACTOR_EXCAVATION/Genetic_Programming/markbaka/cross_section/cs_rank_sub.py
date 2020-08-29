from ..constructor_like import *
from ..is_matrix import *
import bottleneck as bn
from .cs_rank import *


def cs_rank_sub(x, y, ascending=True, pct=False):
    """
    Calculate the difference between rank data of x and y along axis 1

    Parameters
    ----------
    x: Matrix
    y: Matrix
    ascending: bool, default True
    * Whether or not the elements should be ranked in ascending order
    pct: bool, default False
    * Whether or not calculate the rank data as a percentage

    Returns
    -------
    Matrix

    Notes
    -----
    * If the group of records have the same value, the rank data of each member will be assigned the average rank of the
      group.

    """
    assert is_matrix(x)
    assert is_matrix(y)
    x_ = x.copy()
    x = constructor_like(x)
    y = constructor_like(y)

    x_rank = cs_rank(x, ascending, pct)
    y_rank = cs_rank(y, ascending, pct)

    ret = x_rank - y_rank

    return constructor_like(ret, x_)