# variation of the expression
from create_expression import *
from exchange_expression import *


def variation(expression, operator, matrix, number, operator_max, operator_min):
    """
    Variate the parts of the expression.

    Parameters
    ----------
    expression: string
    operator: list of operators
    matrix: list of matrix
    number: list of number data
    operator_max: max number of operators contained in the temp expression
    operator_min: min number of operators contained in the temp expression

    Returns
    -------
    an expression after variation

    Notes
    -----
    * Here, a temp expression is created to help the variation process of the target expression.
    * An error might occur if no bracket is contained in the expression.

    """
    temp = create_expression(operator, matrix, number, operator_max, operator_min)
    ret, temp = exchange_expression(expression, temp)
    return ret