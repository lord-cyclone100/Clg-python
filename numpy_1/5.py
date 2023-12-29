import numpy as np
import random

def row_max(my_matrix):
    max_array = []
    for i in range(len(my_matrix)):
        max_array.append(max(my_matrix[i]))
    print(f"Row maximum element:{max(max_array)}")

def col_min(my_matrix):
    min_array = []
    for i in range(len(my_matrix)):
        min_array.append(min(row[i] for row in my_matrix))
    print(f"Column minimum element:{min(min_array)}")


my_matrix = np.empty((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        my_matrix[i, j] = random.randint(1, 20)
print(f"Matrix 1:\n{my_matrix}")

row_max(my_matrix)
col_min(my_matrix)
