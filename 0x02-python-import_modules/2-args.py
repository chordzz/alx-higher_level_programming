#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    arg_n = len(args) - 1
    print("{}".format(arg_n), end=(" "))
    print("{}".format("argument" if arg_n == 1 else "arguments"), end="")
    print("{}".format("." if arg_n == 0 else ":"))
    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
