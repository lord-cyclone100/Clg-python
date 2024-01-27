#Display electricity consumption of a customer for 12 months using suitable graphical tools.

import matplotlib.pyplot as plt
import random

x_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
y_list = []
for i in range(12):
    y_list.append(random.randint(300,600))
plt.bar(x_list,y_list)
plt.show()
