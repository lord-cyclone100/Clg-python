import numpy as np

array_of_tuples = np.array([(1, 2, 3),(4, 5, 6),(7, 8, 9)])

column_index = 1

extracted_column = np.array([row[column_index] for row in array_of_tuples])

print("Original array of tuples:")
print(array_of_tuples)

print("\nExtracted column:")
print(extracted_column)
