import numpy as np

A = np.array([[2, 3], [5, 4]])
B = np.array([8, 13])

X = np.linalg.solve(A, B)

print(f"Solution: x = {X[0]}, y = {X[1]}")

import numpy as np

n = int(input("Enter number of rows: ").strip())

A = []
B = []

print("Enter coefficients row wise:")

for i in range(n):
    row = list(map(float, input(f"Row[{i + 1}]: ").split()))
    if len(row) != n:
        print("Error: Number of coefficients must be equal to number of rows.")
        exit()
    A.append(row)

print("Enter constants vector:")

for i in range(n):
    val = float(input(f"B[{i + 1}]: "))
    B.append(val)

A = np.array(A)
B = np.array(B)

if np.isclose(np.linalg.det(A), 0):
    print("No unique solution exists.")
else:
    X = np.linalg.solve(A, B)
    print("Solution:")
    for i in range(n):
        print(f"x{i + 1} = {X[i]}")
