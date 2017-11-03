#!/usr/bin/local/python3

"""
Solution to exercise 2111

python3 -m pip install sympy
"""

from sympy import Symbol, simplify, expand


def main():
    """
    This is the main method, I call it main by convention.
    """

    x = Symbol('x')
    a = Symbol('a')
    b = Symbol('b')

    exercisea = 5*x**2 - 4*(2*x-3)*(x-5)
    print(simplify(exercisea))


    exerciseb = 3*(a-b)**2 - 2*(a-b)**2
    print(expand(exerciseb))

    exercisec = (x-2)**3
    print(expand(exercisec))

    exercised = (x-1)*x + (x**2 -2*x -4)*(x+1)
    print(expand(exercised))

if __name__ == "__main__":
    main()
