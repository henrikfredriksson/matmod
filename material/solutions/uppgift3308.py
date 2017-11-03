#!/usr/bin/env python3

"""
Solution to exercise 3308 

python3 -m pip install sympy
"""

from sympy import Symbol, diff

def main():

    x = Symbol('x')

    f = x**3 - 2*x

    f_p = diff(f)

    print("f'(x) = ", str(diff(f, x)))
    print("f'(1) = ", f_p.subs(x, 1))
    print("f'(0) = ", f_p.subs(x, 0))

if __name__ == "__main__":
    main()
