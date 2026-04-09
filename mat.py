import numpy as np

# Function to input matrix
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

# Matrix Addition
def addition(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

# Matrix Subtraction
def subtraction(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result

# Scalar Multiplication
def scalar_multiply(matrix, scalar):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][j] * scalar)
        result.append(row)
    return result

# Matrix Multiplication
def multiply(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            sum = 0
            for k in range(len(m2)):
                sum += m1[i][k] * m2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Transpose
def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

# Inverse (using numpy)
def inverse(matrix):
    np_matrix = np.array(matrix)
    inv = np.linalg.inv(np_matrix)
    return inv

# ---------------- MENU ----------------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix 1")
matrix1 = input_matrix(rows, cols)

print("\nEnter Matrix 2")
matrix2 = input_matrix(rows, cols)

while True:
    print("\nWhat Operation would you like to perform ?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Scalar Multiplication ")
    print("4. Matrix Multiplication")
    print("5. Transpose ")
    print("6. Inverse")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result:", addition(matrix1, matrix2))

    elif choice == 2:
        print("Result:", subtraction(matrix1, matrix2))

    elif choice == 3:
        scalar = int(input("Enter scalar value: "))
        print("Result:", scalar_multiply(matrix1, scalar))

    elif choice == 4:
        if cols != rows:
            print("Matrix multiplication requires proper dimensions.")
        else:
            print("Result:", multiply(matrix1, matrix2))

    elif choice == 5:
        print("Transpose:", transpose(matrix1))

    elif choice == 6:
        if rows == cols:
            print("Inverse:\n", inverse(matrix1))
        else:
            print("Inverse only possible for square matrix.")
