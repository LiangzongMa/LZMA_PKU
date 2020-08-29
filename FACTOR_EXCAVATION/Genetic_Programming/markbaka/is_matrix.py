import numpy as np
import pandas as pd


def is_matrix(x):
    """
    Judge whether the mathematical type of x is matrix.

    Parameters
    ----------
    x

    Returns
    -------
    True / False
    """
    if isinstance(x, np.ndarray) or isinstance(x, pd.DataFrame):
        return True
    else:
        return False
