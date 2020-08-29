from markbaka.math import *
from markbaka.time_series import *
from markbaka.cross_section import *
from markbaka.element import *

operator = list(math_catalog.keys()) + list(time_series_catalog.keys()) + list(cross_section_catalog.keys()) \
           + list(element_catalog.keys())
operator.remove('MAX')
operator.remove('MIN')
operator.remove('ts_nunique')
# too slow, the function calculates the different value along time series of a certain window
matrix = ['CLOSE', 'OPEN', 'HIGH', 'LOW', 'AMOUNT', 'VOLUME']
number = [2, 3, 5, 8, 13, 21, 60]
operator_max = 10
operator_min = 5
survive_rate = 0.5
variation_rate = 0.5
generations = 2
expression_number = 32
date_range = list(range(-729, 0, 1))

# timestamp setting, some problems may occur
step = 1
