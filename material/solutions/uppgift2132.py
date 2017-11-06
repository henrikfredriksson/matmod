#!/usr/bin/env python3

"""
Solution to exercise 2132

python3 -m pip install sympy
"""

from sympy import Symbol, solve

# solve(f) solves the equation f=0, hence we have to re-write so the
# RHS equals zero


def main():
    """
    This is the main method, I call it main by convention.
    """

    x = Symbol('x', real=True)

    uppg_a = 2**(5*x -2) - 2**x
    sol_a = solve(uppg_a)
    print(sol_a)

    uppg_b = 2**(5*x-2) - 4**x
    sol_b = solve(uppg_b)
    print(sol_b)

    uppg_c = 3**(2*x) -  1/27
    sol_c = solve(uppg_c)
    print(sol_c)

    uppg_d = 2**(3*x)*2**(-5) - 2**x
    sol_d = solve(uppg_d)
    print(sol_d)

if __name__ == "__main__":
    main()
