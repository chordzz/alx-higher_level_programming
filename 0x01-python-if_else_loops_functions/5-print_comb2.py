#!/usr/bin/python3
delimiter = ", "
for num in range(0, 100):
    if num < 10:
        print("0{}".format(num), end=delimiter)
    else:
        if num == 99:
            delimiter = "\n"
        print("{}".format(num), end=delimiter)
