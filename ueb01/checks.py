#!/usr/bin/env python3
from itertools import product

# Classroom task 1.1
A = [[0, 1, 0], [2, 0, 1], [1, 1, 0]]
detA = (
    A[0][0] * A[1][1] * A[2][2]
    + A[0][1] * A[1][2] * A[2][0]
    + A[0][2] * A[1][0] * A[2][1]
    - A[0][2] * A[1][1] * A[2][0]
    - A[0][1] * A[1][0] * A[2][2]
    - A[0][0] * A[1][2] * A[2][1]
)
assert detA == 1, detA

# Exercise 1.2: data in the model
values_12 = [4, 8, 7, 16, 40]
times_12 = [5, 9, 7, 15, 30]
assert values_12 == [4, 8, 7, 16, 40]
assert times_12 == [5, 9, 7, 15, 30]
feasible_12 = []
for x in product([0, 1], repeat=5):
    time = sum(t * xi for t, xi in zip(times_12, x))
    used = sum(x)
    value = sum(v * xi for v, xi in zip(values_12, x))
    if time <= 30 and used >= 2:
        feasible_12.append((value, time, x))
assert feasible_12, "the binary model has feasible choices"
best_12 = max(feasible_12)
assert best_12 == (28, 29, (1, 1, 0, 1, 0)), best_12

# Exercise 1.3: data in the model
profit_13 = [3, 5, 4]
machine_A = [1, 2, 1]
machine_B = [1, 1, 2]
machine_C = [0, 3, 1]
capacity = [170, 150, 180]
assert profit_13 == [3, 5, 4]
assert machine_A == [1, 2, 1]
assert machine_B == [1, 1, 2]
assert machine_C == [0, 3, 1]
assert capacity == [170, 150, 180]

# Verify that the displayed constraints evaluate correctly on a sample point.
x = [10, 20, 30]
assert sum(a * b for a, b in zip(machine_A, x)) == 80
assert sum(a * b for a, b in zip(machine_B, x)) == 90
assert sum(a * b for a, b in zip(machine_C, x)) == 90
assert sum(a * b for a, b in zip(profit_13, x)) == 250

print("checks passed")
