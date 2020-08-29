# module level doc-string
__doc__ = """
time_series - a collection of frequently-used functions for operations related to time series data.
===================================================================================================

**time_series** is a subpackage of *markbaka*, more information about the package structure can be 
 found at the doc-string of *markbaka*.

"""

from .ts_argmax import *
from .ts_argmaxmin import *
from .ts_argmin import *
from .ts_autocorr import *
from .ts_corr import *
from .ts_cov import *
from .ts_delay import *
from .ts_delta import *
from .ts_highday import *
from .ts_incv import *
from .ts_kurt import *
from .ts_lowday import *
from .ts_max import *
from .ts_maxmin_norm import *
from .ts_mean import *
from .ts_median import *
from .ts_min import *
from .ts_nunique import *
from .ts_pct import *
from .ts_prod import *
from .ts_rank import *
from .ts_regress_beta import *
from .ts_regress_intercept import *
from .ts_regress_residual import *
from .ts_skew import *
from .ts_std import *
from .ts_sum import *
from .ts_var import *
from .ts_zscore import *
from .ts_wma import *


time_series_catalog = {
    'ts_argmax': {1: 'matrix', 2: 'number'},
    'ts_argmaxmin': {1: 'matrix', 2: 'number'},
    'ts_argmin': {1: 'matrix', 2: 'number'},
    'ts_autocorr': {1: 'matrix', 2: 'number', 3: 'number'},
    'ts_corr': {1: 'matrix', 2: 'matrix', 3: 'number'},
    'ts_cov': {1: 'matrix', 2: 'matrix', 3: 'number'},
    'ts_delay': {1: 'matrix', 2: 'number'},
    'ts_delta': {1: 'matrix', 2: 'number'},
    'ts_highday': {1: 'matrix', 2: 'number'},
    'ts_incv': {1: 'matrix', 2: 'number'},
    'ts_kurt': {1: 'matrix', 2: 'number'},
    'ts_lowday': {1: 'matrix', 2: 'number'},
    'ts_max': {1: 'matrix', 2: 'number'},
    'ts_maxmin_norm': {1: 'matrix', 2: 'number'},
    'ts_mean': {1: 'matrix', 2: 'number'},
    'ts_median': {1: 'matrix', 2: 'number'},
    'ts_min': {1: 'matrix', 2: 'number'},
    'ts_nunique': {1: 'matrix', 2: 'number'},
    'ts_pct': {1: 'matrix', 2: 'number'},
    'ts_prod': {1: 'matrix', 2: 'number'},
    'ts_rank': {1: 'matrix', 2: 'number'},
    'ts_regress_beta': {1: 'matrix', 2: 'matrix', 3: 'number'},
    'ts_regress_intercept': {1: 'matrix', 2: 'matrix', 3: 'number'},
    'ts_regress_residual': {1: 'matrix', 2: 'matrix', 3: 'number'},
    'ts_skew': {1: 'matrix', 2: 'number'},
    'ts_std': {1: 'matrix', 2: 'number'},
    'ts_sum': {1: 'matrix', 2: 'number'},
    'ts_var': {1: 'matrix', 2: 'number'},
    'ts_wma': {1: 'matrix', 2: 'number'},
    'ts_zscore': {1: 'matrix', 2: 'number'}
}
