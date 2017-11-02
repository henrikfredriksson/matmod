# MA1477 Matmod

## Symbolisk hantering

För att kunna använda symboliska beräkningar i Python så behöver
använda biblioteketet [Sympy](http://www.sympy.org/en/index.html).

För att läsa in hela Sympy skiver man.

```python
from sympy import *
```

Vi kan nu deklarera en symbolisk variabel $x$ enligt

```python
x = Symbol('x')
```

Förenkling av symboliska uttryck görs med funktionen `simplify`.

```Python
simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
```

För att utveckla uttryck så kan man använda funktionen `expand`.

```Python
expand((x+1)**2)
```

Med `solve`så kan man lösa ekvationer. Notera att `solve(f)` löser
ekvationen $f(x) = 0$.


```Python
solve(x**2 - 2) #Solve the equation x^2 -2 = 0 
```




