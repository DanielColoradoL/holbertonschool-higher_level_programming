#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    list_division - divides my_list_1 / my_list_2
    handles div/0 error, index error and type error

    args:
    my_list_1: The dividend list
    my_list_2: The divisor list

    Return:
    output_list: the resulting list of the division
    """
    output_list = list()
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        finally:
            output_list.append(div)
    return output_list
