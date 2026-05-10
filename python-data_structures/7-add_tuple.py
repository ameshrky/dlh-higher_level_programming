#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    new_tuple_list = []
    for iterator in range(2):
        new_tuple_list.append(tuple_a[iterator] + tuple_b[iterator])
    return(new_tuple_list[0], new_tuple_list[1])
