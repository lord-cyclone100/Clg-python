#Generate 30 random 2-d points and draw it using a scatter plot.

import matplotlib.pyplot as plt
import random

x_list = []
y_list = []

for i in range(30):
    x_list.append(random.randint(1,100))
    y_list.append(random.randint(1,100))

plt.scatter(x_list,y_list)
plt.show()
