#!/usr/bin/env python3

import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

def calculate(arg):
    stack = []
    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_fn = OPERATIONS[operand]
            result = operator_fn(arg1, arg2)

            stack.append(result)
    return stack.pop()

def main():
    while True:
        rst = calculate(input("rpn calc> "))
        print (rst)

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()

