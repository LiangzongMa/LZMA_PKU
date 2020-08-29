# module level doc-string
__doc__ = """
math - a collection of frequently-used functions for basic mathematical operations.
===================================================================================

**math** is a subpackage of *markbaka*, more information about the package structure
 can be found at the doc-string of *markbaka*.

"""

from .ABS import *
from .add import *
from .arctan import *
from .div import *
from .INV import *
from .mul import *
from .neg import *
from .sign_log import *
from .sign_power import *
from .sign_sqrt import *
from .SQUARE import *
from .sub import *


math_catalog = {
    'ABS': {1: 'matrix'},
    'add': {1: 'matrix', 2: 'both'},
    'arctan': {1: 'matrix'},
    'div': {1: 'matrix', 2: 'both'},
    'INV': {1: 'matrix'},
    'mul': {1: 'matrix', 2: 'both'},
    'neg': {1: 'matrix'},
    'sign_log': {1: 'matrix'},
    'sign_power': {1: 'matrix', 2: 'number'},
    'sign_sqrt': {1: 'matrix'},
    'SQUARE': {1: 'matrix'},
    'sub': {1: 'matrix', 2: 'both'}
}