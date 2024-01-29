'''Generate marks of two students for 6 unit tests randomly then compare the result using
suitable graph.'''

import random
import matplotlib.pyplot as plt
import numpy as np

label_list = ["Unit test 1","Unit test 2","Unit test 3","Unit test 4","Unit test 5","Unit test 6"]
x_list1 = np.arange(6)
x_list2 = [i+0.3 for i in x_list1]
y_list1 = []
for i in range(6):
    y_list1.append(random.randint(70,90))

y_list2 = []
for i in range(6):
    y_list2.append(random.randint(70,90))

plt.bar(x_list1,y_list1,label="Student-1",width=0.3)
plt.bar(x_list2,y_list2,label="Student-2",width=0.3)
plt.legend()
plt.xticks((x_list1+0.15),label_list)
plt.title("Unit test marks")
plt.show()