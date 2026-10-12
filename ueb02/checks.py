#!/usr/bin/env python3
import sympy as sp

x1, x2, x3, t = sp.symbols('x1 x2 x3 t')

# Classroom task 2.1
A = sp.Matrix([[1, 1], [0, 3]])
b = sp.Matrix([2, 3])
orig = A.LUsolve(b)
assert orig == sp.Matrix([1, 1])
At = sp.Matrix([[1, 1, 0], [0, 3, 1]])
assert At * sp.Matrix([1 + t/3, 1 - t/3, t]) == b

# Exercise 2.1 in lecture standard form: max c^T x, Ax=b, x>=0
Astd = sp.Matrix([[2, -1, 1, 0], [1, 0, 0, 1]])
bstd = sp.Matrix([12, 8])
cstd = sp.Matrix([2, 1, 0, 0])
assert Astd * sp.Matrix([0, 0, 12, 8]) == bstd
for M in [0, 1, 10, 100]:
    x = sp.Matrix([0, M, 12 + M, 8])
    assert Astd * x == bstd
    assert all(v >= 0 for v in x)
    assert (cstd.T * x)[0] == M

# Exercise 2.2, one LP matching Figure 1
# min 2*x1+x2 subject to x1>=3, 2*x1+3*x2>=12, -x1+2*x2>=-1.
# Boundary intersections used in the graphical solution.
assert 2*3 + 3*2 == 12
assert 3 >= 3
assert -3 + 2*2 == 1 and 1 >= -1
inter = sp.solve([sp.Eq(2*x1 + 3*x2, 12), sp.Eq(-x1 + 2*x2, -1)], [x1, x2])
assert inter[x1] == sp.Rational(27, 7)
assert inter[x2] == sp.Rational(10, 7)
assert 2*3 + 2 == 8
assert 2*inter[x1] + inter[x2] == sp.Rational(64, 7)
assert sp.Rational(64, 7) > 8

# Exercise 2.3 vertices and objective values
vertices = [(0, 0), (sp.Rational(16, 3), 0), (4, 4), (0, 4)]
values = []
for a, b2 in vertices:
    assert a + 2*b2 <= 12
    assert 3*a + b2 <= 16
    assert 0 <= b2 <= 4
    assert a >= 0
    values.append(3*a + 5*b2)
assert values == [0, 16, 32, 20]
assert max(values) == 32
assert vertices[values.index(32)] == (4, 4)

print('all checks passed')
