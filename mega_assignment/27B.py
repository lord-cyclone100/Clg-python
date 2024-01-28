'''Read two matrices and add them. Store the matrices and result in a file.'''

import numpy as np

def mat_add(mat1,mat2):
    return mat1+mat2

def file_add(mat1,mat2,sum):
    with open("27B.txt","w") as f:
        f.write(f"Matrix 1:\n{mat1}\nMatrix 2:\n{mat2}\nSum:\n{sum}")

mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
sum = mat_add(mat1,mat2)
print(f"Sum = \n{sum}")
file_add(mat1,mat2,sum)