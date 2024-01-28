'''Write a python program to create an 3X3 Matrix randomly and calculate sum of
the diagonal elements.'''

import numpy as np
import random

def sum_diagonal(n):
    sum1 = 0
    sum2 = 0
    for i in range(3):
        for j in range(3):
            if i==j:
                sum1 += n[i,j]
            if i+j==2:
                sum2 += n[i,j]
    print(f"Sum of leading diagonal elements is {sum1}")
    print(f"Sum of non-leading diagonal elements is {sum2}")

n = np.empty(shape=(3,3),dtype=int)
for i in range(3):
    for j in range(3):
        n[i,j] = random.randint(1,10)
print(f"The matrix is:\n{n}")
sum_diagonal(n)