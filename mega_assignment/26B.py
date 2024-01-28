'''Take the five marks of a student for a particular subject.
Display the data graphically using suitable graphs.'''

import matplotlib.pyplot as plt
import numpy as np
import random

def bar_graph(x,y):
    plt.bar(x,y)
    plt.show()

def pie_chart(x,y):
    plt.pie(y,labels=x)
    plt.show()

x_list = np.array(["Maths","Digital","CO","DSA","Economics"])
y_list = []
for i in range(5):
    y_list.append(random.randint(70,90))
bar_graph(x_list,y_list)
pie_chart(x_list,y_list)