# Define the fitness function of Genetic Programming
import numpy as np
import pandas as pd
from markbaka import constructor_like
from markbaka import is_matrix
import warnings
warnings.filterwarnings('ignore')

def fitness_icir(matrix, ret):
    """
    Use abs(IC_IR) as the fitness function of Genetic Programming.

    Parameters
    ----------
    matrix: numpy.ndarray or pandas.DataFrame
    ret: numpy.ndarray or pandas.DataFrame, refers to stock return

    Returns
    -------
    abs(IC_IR)

    Notes
    -----
    * `ret` refers to stock return matrix. Day's return should match the value of the day's factor.
      Example:
      For 1-day stock return matrix, line T is the stock return calculated between T and T+1, not T-1 and T.

    """
    assert is_matrix(matrix)
    assert is_matrix(ret)
    matrix = constructor_like(matrix)
    ret = constructor_like(ret)

    matrix[np.isnan(ret)] = np.nan
    ret[np.isnan(matrix)] = np.nan

    up = np.nanmean(matrix * ret, axis=1) - np.nanmean(matrix, axis=1) * np.nanmean(ret, axis=1)
    down = np.nanstd(matrix, axis=1, ddof=0) * np.nanstd(ret, axis=1, ddof=0)
    ic = up / down

    ir = np.nanmean(ic) / np.nanstd(ic) * np.sqrt(243)
    return np.abs(ir)

