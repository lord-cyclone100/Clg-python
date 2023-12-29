def add_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def subtract_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

matrix1 = [[1+2j, 2-1j], [3-4j, 5+6j]]
matrix2 = [[2+3j, 4-2j], [1-3j, 7+8j]]

result_addition = add_matrices(matrix1, matrix2)
print("Addition Result:")
for row in result_addition:
    print(row)

result_subtraction = subtract_matrices(matrix1, matrix2)
print("\nSubtraction Result:")
for row in result_subtraction:
    print(row)

result_multiplication = multiply_matrices(matrix1, matrix2)
print("\nMultiplication Result:")
for row in result_multiplication:
    print(row)
