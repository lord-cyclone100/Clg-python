import numpy as np
import random

def sum(my_matrix):
    sum1 = 0
    sum2 = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if i == j:
                sum1 += my_matrix[i, j]
            if i+j == 2:
                sum2 += my_matrix[i, j]

    print(f"Sum of leading diagonal elements: {sum1}")
    print(f"Sum of trailing diagonal elements: {sum2}")

my_matrix = np.empty((3, 3), dtype=int)

for i in range(3):
    for j in range(3):
        my_matrix[i, j] = random.randint(1, 9)

print(my_matrix)

sum(my_matrix)