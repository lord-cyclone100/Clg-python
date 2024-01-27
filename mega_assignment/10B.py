'''Election results of India for the year 2000 is published.
Out of 400 seats, 'ABC’ got
180, ‘XYZ’ got 200 and ‘MNP’ got the rest. Display the result using suitable graphical
tools.'''

import matplotlib.pyplot as plt
x_list = ['ABC','XYZ','MNP']
y_list = [180,200,20]

plt.bar(x_list,y_list,width=0.5)
plt.title("Election results of India, 2000")
plt.show()
