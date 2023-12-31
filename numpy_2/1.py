import numpy as np

a = np.array([[1,2],[3,4]])
print(a)

new_array = a.view()
new_array[1,0] = 5

print(new_array)
print(a)