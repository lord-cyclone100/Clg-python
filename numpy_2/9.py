import numpy as np

array_2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print("Original array:")
print(array_2d)
column1_index = 0
column2_index = 2

array_2d[:, [column1_index, column2_index]] = array_2d[:, [column2_index, column1_index]]

print("Updated array:")
print(array_2d)
