#!/usr/bin/python3
def square_matrix_simple(matix=[]):
    new_list = []
    for elem in matrix:
        y = list(map(lambda x: x ** 2, elem))
        new_list.append(y)
    return new_list
