'''Input two 3X3 Matrices. Now perform
a. the addition of two 3X3 Matrices.
b. perform the elements-wise multiplication of two 3X3 Matrices.
c. perform the Matrix Multiplication of two 3X3 Matrices.'''

import numpy as np

def mat_add(mat1,mat2):
    return mat1+mat2
def mat_mul(mat1,mat2):
    return mat1*mat2

def multiply(mat1,mat2):
    return np.dot(mat1,mat2)

mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Sum = {mat_add(mat1,mat2)}")
print(f"Element wise product = {mat_mul(mat1,mat2)}")
print(f"Sum = {multiply(mat1,mat2)}")