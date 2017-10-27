#!/usr/bin python3

from sympy import *
import numpy as np

x = Symbol('x')

a = x**2 - 4*x - 3*x + x**2
b = simplify(sin(x)**2 + cos(x)**2)
c = simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))

print(a)
print(b)
print(c)
