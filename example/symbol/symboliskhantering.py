#!/usr/bin/env python3
"""Examples on how to use sympy"""

from sympy import Symbol, simplify, sin, cos

x = Symbol('x')

A = x**2 - 4*x - 3*x + x**2
B = simplify(sin(x)**2 + cos(x)**2)
C = simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))


print(A)
print(B)
print(C)
