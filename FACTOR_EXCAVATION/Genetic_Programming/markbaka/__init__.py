# module level doc-string
__doc__ = """
markbaka - a collection of frequently-used functions for quantitative finance based on Python
=============================================================================================

**markbaka** is a Python package providing frequently-used functions for quantitative research.
Nowadays, workload related to quantitative finance is fundamentally based on math and computer 
science, especially code. An essential part of quantitative work is selecting stocks to hold in
order to get the highest return. Based on this purpose, using time series and cross section data
to calculate some indexes used to select stocks is an indispensable part. The package contains 
some frequently-used operations which will absolutely help the researchers simplify their program.


Designer
--------
Liangzong Ma, Department of Finance, School of Economics, Peking University
E-mail: lzma@pku.edu.cn


Main Features
-------------
Here are just a few of the things that markbaka does well:

   - Calculate the correlation and covariance both on cross section data and time series data in
     high efficiency
   - Exert OLS on time series data in high efficiency
   - Contain basic mathematical operations
   - Contain sorting operations on both cross section data and time series data
   - Contain elementwise operations


Function Parameters
-------------------
* Function parameters are composed of two mathematical elements, number and matrix. Parameters in 
* matrix form support both numpy.ndarray and pandas.DataFrame. Remember to change the matrix like 
  parameters into 2-dimension.
* If you want to get the information about all the functions of a subpackage, you can load the certain
  package and get the information.
  'matrix' means the parameter is numpy.ndarray or pandas.DataFrame.
  'number' means the parameter is an integer or float.
  'both' means the parameter can be both matrix and number.

  Example:
  >>> from markbaka.cross_section import *
  >>> cross_section_catalog
  >>> 
  {'cs_demean': {1: 'matrix'},
   'cs_rank': {1: 'matrix'},
   'cs_rank_div': {1: 'matrix', 2: 'matrix'},
   'cs_rank_sub': {1: 'matrix', 2: 'matrix'},
   'cs_scale': {1: 'matrix', 2: 'number'}
   }


Functions (Essential)
---------------------
The package is composed of 4 subpackages, cross_section, time_series, element, math.
The subpackages contain certain type of functions as follows:
    - cross_section: operations on cross section data
    - time_series: operations on time_series data
    - element: operations on elementwise data
    - math: basic mathematical operations
*** If you want to add some functions to the package, do remember to put the functions in right
    subpackage and fulfill the dictionary contains the information of all the functions. This is
    extremely important.

    
Packages Required (Essential)
-----------------------------
Four python packages related to data processing, numpy, pandas, bottleneck, talib, are required.
Other basic Python packages such as os is required.
Do remember to use `pip` and `pip3` to install packages if some errors about missing packages occur. 


Notes
-----
* Some problems still need to be solved, such as dealing with the precision problem (ts_corr, etc).
* Some improvement can be added to the functions contained by the package, such as rewrite the functions
  to make high dimensional data (over 2) available to be parameters.
Although much work needed to be handled with, the functions contained by the package can fulfill daily 
quantitative use.


Contact Me
----------
If you have some ideas, you are highly welcomed to send e-mails to me and have a short discussion.


"""

from .constructor_like import *
from .is_matrix import *


__all__ = ['cross_section', 'element', 'math', 'time_series']

