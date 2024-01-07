import numpy as np

data = np.array([(1, 'apple'), (2, 'banana'), (3, 'cherry')], dtype=object)

two_d_array = data.reshape((-1, 2))

print(two_d_array)
