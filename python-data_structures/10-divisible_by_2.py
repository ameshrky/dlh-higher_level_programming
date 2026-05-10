#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for item in my_list:
        list_result.append(item % 2 == 0)
    return list_result
