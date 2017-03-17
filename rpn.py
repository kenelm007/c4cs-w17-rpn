#!/usr/bin/env python3

import operator
import readline
from colored import fg, attr, fore, style

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

COLOR = {
    "+": fore.YELLOW,
    "-": fore.BLUE,
    "*": fore.MAGENTA,
    "/": fore.CYAN,
    "^": fore.DARK_GRAY,
}

def calculate(arg):
    stack = []
    try:
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
    except:
        print ("An error occured")
        return None

def main():
    while True:
        equation = input("rpn calc> ")
        rst = calculate(equation)
        coloredEq = ""
        for i in equation.split():
            try:
                num = float(i)
                if num < 0:
                    color = fore.RED
                else:
                    color = fore.WHITE
                coloredEq += color + i + ' '
            except:
                coloredEq += COLOR[i] + i + ' '
                
        print (style.BOLD + coloredEq + fore.LIGHT_YELLOW + "= " + style.RESET + str(rst))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()

