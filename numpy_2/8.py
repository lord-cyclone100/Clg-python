import numpy as np

my_array = np.array([1, 5, 10, 15, 20, 25, 30])

lower_bound = 10
upper_bound = 25

result_array = my_array[(my_array >= lower_bound) & (my_array <= upper_bound)]

print("Numbers within the range:", result_array)
