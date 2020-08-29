# Define the fitness function of Genetic Programming
from .path_settings import *
import numpy as np
from markbaka import constructor_like
from markbaka import is_matrix
import bottleneck as bn
import warnings
warnings.filterwarnings('ignore')


def fitness_icir(matrix, ret, step):
    """
    Use abs(IC_IR) as the fitness function of Genetic Programming.

    Parameters
    ----------
    matrix: numpy.ndarray or pandas.DataFrame
    ret: numpy.ndarray or pandas.DataFrame, refers to stock return
    step: number, refers to the holding days

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

    nan_matrix = (np.isnan(matrix))
    matrix = bn.rankdata(matrix, axis=1)
    matrix[nan_matrix] = np.nan
    ret = bn.rankdata(ret, axis=1)
    ret[nan_matrix] = np.nan

    up = np.nanmean(matrix * ret, axis=1) - np.nanmean(matrix, axis=1) * np.nanmean(ret, axis=1)
    down = np.nanstd(matrix, axis=1, ddof=0) * np.nanstd(ret, axis=1, ddof=0)
    down[down == 0] = np.nan
    ic = up / down

    ir = np.nanmean(ic) / np.nanstd(ic) * np.sqrt(243 / step)
    return ir

