#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None
    int_list = list()
    output = 0
    flag = 0
    for letter in roman_string:
        if letter == 'I':
            int_list.append(1)
        if letter == 'V':
            int_list.append(5)
        if letter == 'X':
            int_list.append(10)
        if letter == 'L':
            int_list.append(50)
        if letter == 'C':
            int_list.append(100)
        if letter == 'D':
            int_list.append(500)

    for index in range(len(int_list)):
        if index + 1 == len(int_list):
            if flag == 1:
                flag = 0
                continue
            output = output + int_list[index]
        elif int_list[index] >= int_list[index + 1]:
            output = output + int_list[index]
        else:
            output = output + (int_list[index + 1] - int_list[index])
            index = index + 1
            flag = 1
    return (output)
