#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            charCode = 32
        else:
            charCode = 0
        print("{:c}".format(ord(str[i]) - charCode), end="")
    print()
