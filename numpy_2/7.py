import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5, 6, 7])

result_array = np.setdiff1d(array1, array2)

print("Result array:", result_array)
