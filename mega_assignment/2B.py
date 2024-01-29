#Plot the curve O(n) and O(n^2).

import numpy as np
import matplotlib.pyplot as plt

x_list = np.arange(0,10,0.5)
y_list1 = [i+1 for i in x_list]
y_list2 = [i**2 for i in x_list]

plt.plot(x_list,y_list1,label="O(n)")
plt.plot(x_list,y_list2,label="O(n^2)")
plt.legend()
plt.show()