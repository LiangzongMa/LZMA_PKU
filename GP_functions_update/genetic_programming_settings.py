from markbaka.math import *
from markbaka.time_series import *
from markbaka.cross_section import *
from markbaka.element import *

operator = list(math_catalog.keys()) + list(time_series_catalog.keys()) + list(cross_section_catalog.keys())\
           + list(element_catalog.keys())
matrix = ['CLOSE', 'OPEN', 'HIGH', 'LOW', 'AMOUNT', 'VOLUME']
number = [1, 2, 3, 5, 8, 13, 21]
operator_max = 20
operator_min = 5
survive_rate = 0.5
variation_rate = 0.5
generations = 3
expression_number = 640
