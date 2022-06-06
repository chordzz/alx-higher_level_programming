#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for el in matrix:
        for i in range(len(el)):
            if i != (len(el) - 1):
                print("{:d}".format(el[i]), end=" ")
            else:
                print("{:d}".format(el[i]))
