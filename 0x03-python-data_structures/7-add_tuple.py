#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    arg_a1, arg_a2, arg_b1, arg_b2 = 0, 0, 0, 0
    if len_a < 2:
        arg_a1 = tuple_a[0]
        arg_a2 = 0
    else:
        arg_a1 = tuple_a[0]
        arg_a2 = tuple_a[1]

    if len_b < 2:
        arg_b1 = tuple_b[0]
        arg_b2 = 0
    else:
        arg_b1 = tuple_b[0]
        arg_b2 = tuple_b[1]
    return ((arg_a1 + arg_b1), (arg_a2 + arg_b2))
