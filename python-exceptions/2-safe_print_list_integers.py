#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Safe print a list.
    This function safe print a list given any sort of datatypes.
    Parameters:
    - my_list (list): The list to be proccesed.
    - x (int): The lenght to be analized

    Returns:
    - (int): The number of integers that were printed.
    """
    count = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count = count + 1
        except IndexError:
            print(end="")
        except (TypeError, ValueError):
            print(end="")
    print()
    return count
