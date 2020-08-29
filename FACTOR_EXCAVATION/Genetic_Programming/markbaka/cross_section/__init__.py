# module level doc-string
__doc__ = """
cross_section - a collection of frequently-used functions for operations related to cross section data.
=======================================================================================================

**cross_section** is a subpackage of *markbaka*, more information about the package structure can be 
 found at the doc-string of *markbaka*.

"""

from .cs_demean import *
from .cs_rank import *
from .cs_rank_div import *
from .cs_rank_sub import *
from .cs_scale import *


cross_section_catalog = {
    'cs_demean': {1: 'matrix'},
    'cs_rank': {1: 'matrix'},
    'cs_rank_div': {1: 'matrix', 2: 'matrix'},
    'cs_rank_sub': {1: 'matrix', 2: 'matrix'},
    'cs_scale': {1: 'matrix', 2: 'number'}
}
