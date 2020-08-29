# Exchange parts of two expressions randomly
import random


def exchange_expression(x, y):
    """
    Exchange parts of two expressions randomly.

    Parameters
    ----------
    x: string (an expression)
    y: string (an expression)

    Returns
    -------
    two new expressions after partly exchanging

    Notes
    -----
    * An error might occur if not brackets are contained in the expression.

    """
    assert isinstance(x, str)
    assert isinstance(y, str)

    x_left = [index for index, charactor in enumerate(x) if charactor == '(']  # get the index of '(' in x

    y_left = [index for index, charactor in enumerate(y) if charactor == '(']  # get the index of '(' in y

    x_index = random.randint(0, len(x_left)-1)
    y_index = random.randint(0, len(y_left)-1)

    def search_index(var, index, left):
        """
        Search for left index and right index for later use

        Parameters
        ----------
        var: target variable
        index: initial index
        left: collection of positions of `(`

        Returns
        -------

        """
        left_index = left[index]
        expression_judge = random.randint(0, 1)
        if expression_judge == 1:
            # search for right index
            right_index = left_index
            stack = ['(']  # like a stack
            while True:
                right_index += 1
                if var[right_index] == '(':
                    stack.append('(')
                if var[right_index] == ')':
                    stack.pop()
                    if len(stack) == 0:
                        break
            # search for left index
            while True:
                left_index -= 1
                if left_index == 0 or var[left_index - 1] in ['(', ',']:
                    break
        else:
            # search for right index
            right_index = left_index
            stack = []  # like a stack
            while True:
                right_index += 1
                if var[right_index] == '(':
                    stack.append('(')
                if var[right_index] in [',', ')'] and len(stack) == 0:
                    right_index -= 1
                    break
                if var[right_index] == ')':
                    stack.pop()
                    if len(stack) == 0:
                        break
            # search for left index
            left_index = left_index + 1

        return left_index, right_index

    x_left_index, x_right_index = search_index(x, x_index, x_left)
    y_left_index, y_right_index = search_index(y, y_index, y_left)

    # exchange
    x_new = x[:x_left_index] + y[y_left_index:y_right_index+1] + x[x_right_index+1:]
    y_new = y[:y_left_index] + x[x_left_index:x_right_index+1] + y[y_right_index+1:]

    return x_new, y_new

