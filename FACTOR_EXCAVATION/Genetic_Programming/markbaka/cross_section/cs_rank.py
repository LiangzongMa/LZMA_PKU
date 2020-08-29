from ..constructor_like import *
from ..is_matrix import *
import bottleneck as bn


def cs_rank(x, ascending=True, pct=False):
    """
    Compute numerical data ranks along axis 1

    Parameters
    ----------
    x: Matrixs
    ascending: bool, default True
    * Whether or not the elements should be ranked in ascending order
    pct: bool, default False
    * Whether or not return the rank data as a percentage

    Returns
    -------
    Matrix

    Notes
    -----
    * If the group of records have the same value, the rank data of each member will be assigned the average rank of the
      group.

    """
    assert is_matrix(x)
    x_ = x.copy()
    x = constructor_like(x)  # change x into numpy.ndarray to speed up
    if pct:
        nan_matrix = np.isnan(x)
        not_nan = np.sum((~nan_matrix), axis=1).reshape(-1, 1)
        rank = bn.rankdata(x, axis=1)
        if ascending is False:
            rank = np.fliplr(rank)
        rank[nan_matrix] = np.nan
        rank = rank / not_nan
        return constructor_like(rank, x)
    else:
        nan_matrix = np.isnan(x)
        rank = bn.rankdata(x, axis=1)
        if ascending is False:
            rank = np.fliplr(rank)
        rank[nan_matrix] = np.nan
        return constructor_like(rank, x_)
