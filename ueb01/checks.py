import sympy as sp

# Classroom task 1.1
A = sp.Matrix([[0, 1, 0], [2, 0, 1], [1, 1, 0]])
det_A = A.det()
rank_A = A.rank()
assert det_A == 1, det_A
assert rank_A == 3, rank_A
assert A.inv() * A == sp.eye(3)

# Exercise 1.2: binary model data
values_12 = sp.Matrix([4, 8, 7, 16, 40])
times_12 = sp.Matrix([5, 9, 7, 15, 30])
assert list(values_12) == [4, 8, 7, 16, 40]
assert list(times_12) == [5, 9, 7, 15, 30]

# Feasibility examples for the cardinality/time constraints
x_example = sp.Matrix([1, 1, 1, 1, 0])
assert (times_12.T * x_example)[0] == 36  # this example violates the 30 minute limit
x_feasible = sp.Matrix([1, 1, 1, 0, 0])
assert (times_12.T * x_feasible)[0] == 21
assert sum(x_feasible) == 3

# If x_5 = 1, the time limit leaves no room for a second positive-time source.
for i in range(4):
    x = sp.zeros(5, 1)
    x[4] = 1
    x[i] = 1
    assert (times_12.T * x)[0] > 30

# Exercise 1.3: product LP coefficients
profit = sp.Matrix([3, 5, 4])
capacity = sp.Matrix([170, 150, 180])
resources = sp.Matrix([
    [1, 2, 1],  # Machine A
    [1, 1, 2],  # Machine B
    [0, 3, 1],  # Machine C
])
assert list(profit) == [3, 5, 4]
assert list(capacity) == [170, 150, 180]
assert resources == sp.Matrix([[1, 2, 1], [1, 1, 2], [0, 3, 1]])

# Sanity check: a sample production plan respects constraints if resources*x <= capacity.
x_sample = sp.Matrix([10, 20, 30])
used = resources * x_sample
assert used == sp.Matrix([80, 90, 90])
assert all(used[i] <= capacity[i] for i in range(3))

print("all checks passed")
