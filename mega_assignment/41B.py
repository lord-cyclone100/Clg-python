'''Election results of West Bengal between party X,Y,Z using suitable graph.Take the
input total seat and number of seat the party X,Y,Z got.'''

import matplotlib.pyplot as plt

def graph_plot(x,y,z):
    if(x+y+z)>n:
        print("Invalid input")
    else:
        x_list = ["X","Y","Z"]
        y_list = [x,y,z]
        plt.bar(x_list,y_list,width=0.5)
        plt.title("Election results")
        plt.show()

n = int(input("Enter the total no of seats:"))
x = int(input("Enter the no of seats won by party X:"))
y = int(input("Enter the no of seats won by party Y:"))
z = int(input("Enter the no of seats won by party Z:"))
graph_plot(x,y,z)