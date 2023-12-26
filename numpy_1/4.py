import numpy as np
import random

def product(matrix1,matrix2):
    product_matrix = np.dot(matrix1,matrix2)
    print(f"Product:\n{product_matrix}")

my_matrix1 = np.empty((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        my_matrix1[i, j] = random.randint(1, 9)
print(f"Matrix 1:\n{my_matrix1}")

my_matrix2 = np.empty((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        my_matrix2[i, j] = random.randint(1, 9)
print(f"Matrix 2:\n{my_matrix2}")

product(my_matrix1,my_matrix2)