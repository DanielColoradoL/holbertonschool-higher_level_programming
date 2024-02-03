#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division - Divides a / b avoiding 0 Div
    a: The dividend
    b: The divisor
    Return: the result, None if Div by 0
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
