import pandas as pd
import numpy as np


def constructor_like(x, target=np.array([])):
    """
    Change the object type of x into the same type of target.

    Parameters
    ----------
    x: numpy.ndarray or pandas.DataFrame
    target: default numpy.ndarray, numpy.ndarray or pandas.DataFrame

    Returns
    -------
    Matrix in target form

    Notes
    -----
    * Only type changing process between np.ndarray and pd.DataFrame is available.
    * If type of x is np.ndarray and is ought to be changed into pd.DataFrame, the
      index and columns should be the same as of target.
    * Input should be 2-dimension.

    """
    assert isinstance(x, np.ndarray) or isinstance(x, pd.DataFrame)
    assert isinstance(target, np.ndarray) or isinstance(target, pd.DataFrame)
    x = x * 1.0

    if type(x) == type(target):
        return x.copy()
    elif isinstance(x, np.ndarray):
        return pd.DataFrame(x, index=target.index, columns=target.columns)
    else:
        return x.values
