# Create an expression
import random
from markbaka.cross_section import *
from markbaka.element import *
from markbaka.time_series import *
from markbaka.math import *

operator_dict = {}
operator_dict.update(cross_section_catalog)
operator_dict.update(math_catalog)
operator_dict.update(time_series_catalog)
operator_dict.update(element_catalog)


def create_expression(operator, matrix, number, operator_max, operator_min):
    """
    Create an expression randomly.

    Parameters
    ----------
    operator: list of operators
    matrix: list of data of matrix form
    number: list of number
    operator_max: max number of operators contained in the expression
    operator_min: min number of operators contained in the expression

    Returns
    -------
    A string, which refers to an expression

    """
    assert isinstance(operator_max, int)
    expression = []
    operator_size = len(operator)  # the number of operators
    number_size = len(number)  # the size of the list of number
    matrix_size = len(matrix)  # the size of the list of matrix
    while True:
        for i in range(operator_max):
            operator_index = random.randint(0,
                                            operator_size - 1)  # choose an operator to add to the expression randomly
            operator_name = operator[operator_index]
            operator_information = operator_dict[operator_name]
            parameter_collection = []
            if len(expression) == 0:  # add operator to the expression for the first time
                for parameter in operator_information.keys():
                    if operator_information[parameter] == 'matrix':  # add matrix
                        parameter_index = random.randint(0, matrix_size - 1)
                        parameter_collection.append(matrix[parameter_index])
                    elif operator_information[parameter] == 'number':  # add number
                        parameter_index = random.randint(0, number_size - 1)
                        parameter_collection.append(number[parameter_index])
                    elif operator_information[parameter] == 'both':  # both matrix and number are ok
                        matrix_judge = random.randint(0, 1)
                        if matrix_judge == 1:  # add matrix
                            parameter_index = random.randint(0, matrix_size - 1)
                            parameter_collection.append(matrix[parameter_index])
                        else:  # add number
                            parameter_index = random.randint(0, number_size - 1)
                            parameter_collection.append(number[parameter_index])
            else:  # not the first time
                for parameter in operator_information.keys():
                    if operator_information[parameter] == 'matrix':  # add matrix
                        matrix_expression_judge = random.randint(0, 1)
                        # judge whether choose a matrix from expressions before
                        if matrix_expression_judge == 1:
                            parameter_index = random.randint(0, len(expression) - 1)
                            parameter_collection.append(expression[parameter_index])
                        else:
                            parameter_index = random.randint(0, matrix_size - 1)
                            parameter_collection.append(matrix[parameter_index])
                    elif operator_information[parameter] == 'number':  # add number
                        parameter_index = random.randint(0, number_size - 1)
                        parameter_collection.append(number[parameter_index])
                    elif operator_information[parameter] == 'both':  # both matrix and number are ok
                        matrix_judge = random.randint(0, 1)
                        if matrix_judge == 1:  # add matrix
                            matrix_expression_judge = random.randint(0, 1)
                            # judge whether choose a matrix from expressions before
                            if matrix_expression_judge == 1:
                                parameter_index = random.randint(0, len(expression) - 1)
                                parameter_collection.append(expression[parameter_index])
                            else:
                                parameter_index = random.randint(0, matrix_size - 1)
                                parameter_collection.append(matrix[parameter_index])
                        else:  # add number
                            parameter_index = random.randint(0, number_size - 1)
                            parameter_collection.append(number[parameter_index])
            operator_name = operator_name + '('
            for j in range(len(parameter_collection)):
                if j < len(parameter_collection) - 1:
                    operator_name = operator_name + str(parameter_collection[j]) + ','
                else:
                    operator_name = operator_name + str(parameter_collection[j]) + ')'
            expression.append(operator_name)

        # choose an expression randomly
        expression_index = random.randint(0, len(expression) - 1)
        ret = expression[expression_index]

        # inspect whether the number of operators contained in the expression is less than `operator_min`
        inspect_temp = ret.split('(')
        count = 0
        for string in inspect_temp:
            if string in operator:
                count += 1
        if count >= operator_min:
            break
    return ret







