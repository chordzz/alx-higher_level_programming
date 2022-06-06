#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    prog, op1, operator, op2 = args.split()
    match operator:
        case "+":
            print("{} {} {} = {}".format(op1, operator, op2, add(int(op1), int(op2)))
                    case "-":
                    print("{} {} {} = {}".format(op1, operator, op2, sub(int(op1), int(op2))))
                    case "*":
                    print("{} {} {} = {}".format(op1, operator, op2, mul(int(op1), int(op2))))
                    case "/":
                    print("{} {} {} = {}".format(op1, operator, op2, div(int(op1), int(op2))))
                    case _:
                print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
