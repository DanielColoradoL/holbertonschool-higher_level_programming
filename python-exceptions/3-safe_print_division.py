#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division - Divides a / b avoiding 0 Div
    
    args:
    a: The dividend
    b: The divisor

    Return:
    result: the result of the division, None if Div by 0
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
