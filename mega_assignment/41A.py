'''Create a matrix randomly then sort it with respect to 2 nd row.'''

import numpy as np

def sort_2nd_row(arr):
    l = arr[1]
    l.sort()
    arr[1] = l
    return arr

arr = np.array([[2,3,1],[5,6,4],[8,9,7]])
print(f"Original matrix:\n{arr}")
a = sort_2nd_row(arr)
print(f"Matrix after sorting second row:\n{a}")