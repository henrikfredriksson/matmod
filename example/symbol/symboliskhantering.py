#!/usr/bin/env python3

"""
Examples on how to use sympy.

python3 -m pip install sympy
"""

from sympy import Symbol, simplify, sin, cos

def main():
    """
    This is the main method, I call it main by convention.
    """

    x = Symbol('x')

    exempel1 = x**2 - 4*x - 3*x + x**2
    exempel2 = simplify(sin(x)**2 + cos(x)**2)
    exempel3 = simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))

    print(exempel1)
    print(exempel2)
    print(exempel3)

if __name__ == "__main__":
    main()
