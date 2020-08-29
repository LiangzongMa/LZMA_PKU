# module level doc-string
__doc__ = """
element - a collection of frequently-used functions for operations related to elementwise data.
===============================================================================================

**element** is a subpackage of *markbaka*, more information about the package structure can be 
 found at the doc-string of *markbaka*.

"""

from .MAX import *
from .MIN import *
from .mean import *
from .sigmoid import *

element_catalog = {
    'MAX': {1: 'matrix', 2: 'matrix'},
    'MIN': {1: 'matrix', 2: 'matrix'},
    'mean': {1: 'matrix', 2: 'matrix'},
    'sigmoid': {1: 'matrix'}
}
