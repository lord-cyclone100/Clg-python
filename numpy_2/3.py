import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Shape of array:{arr.shape}")
newarr = arr.reshape(4, 3)
print(f"Shape of array:{newarr.shape}")