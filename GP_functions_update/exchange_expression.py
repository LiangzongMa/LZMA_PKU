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

    x_left_index = x_left[x_index]
    expression_judge = random.randint(0, 1)
    if expression_judge == 1:
        # search for right index
        x_right_index = x_left_index
        stack = ['(']  # like a stack
        while True:
            x_right_index += 1
            if x[x_right_index] == '(':
                stack.append('(')
            if x[x_right_index] == ')':
                stack.pop()
                if len(stack) == 0:
                    break
        # search for left index
        while True:
            x_left_index -= 1
            if x_left_index == 0 or x[x_left_index-1] in ['(', ',']:
                break
    else:
        # search for right index
        x_right_index = x_left_index
        stack = []  # like a stack
        while True:
            x_right_index += 1
            if x[x_right_index] == '(':
                stack.append('(')
            if x[x_right_index] in [',', ')'] and len(stack) == 0:
                x_right_index -= 1
                break
            if x[x_right_index] == ')':
                stack.pop()
                if len(stack) == 0:
                    break
        # search for left index
        x_left_index = x_left_index + 1

    y_left_index = y_left[y_index]
    expression_judge = random.randint(0, 1)
    if expression_judge == 1:
        # search for right index
        y_right_index = y_left_index
        stack = ['(']  # like a stack
        while True:
            y_right_index += 1
            if y[y_right_index] == '(':
                stack.append('(')
            if y[y_right_index] == ')':
                stack.pop()
                if len(stack) == 0:
                    break
        # search for left index
        while True:
            y_left_index -= 1
            if y_left_index == 0 or y[y_left_index - 1] in ['(', ',']:
                break
    else:
        # search for right index
        y_right_index = y_left_index
        stack = []  # like a stack
        while True:
            y_right_index += 1
            if y[y_right_index] == '(':
                stack.append('(')
            if y[y_right_index] in [',', ')'] and len(stack) == 0:
                y_right_index -= 1
                break
            if y[y_right_index] == ')':
                stack.pop()
                if len(stack) == 0:
                    break
        # search for left index
        y_left_index = y_left_index + 1

    # exchange
    x_new = x[:x_left_index] + y[y_left_index:y_right_index+1] + x[x_right_index+1:]
    y_new = y[:y_left_index] + x[x_left_index:x_right_index+1] + y[y_right_index+1:]

    return x_new, y_new

