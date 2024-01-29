#Delete the second column from a given array and insert the new column in its place.

import numpy as np

def replace_2nd_column(arr):
    l = 9
    for i in arr:
        i[1] = l + 1
        l += 1
    return arr

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Original matrix:\n{arr}")
a = replace_2nd_column(arr)
print(f"Matrix after replacing second row:\n{a}")