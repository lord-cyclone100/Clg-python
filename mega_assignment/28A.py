'''Write a Python script to enter the length and breadth of a rectangle and radius of
a circle. Find perimeter and area of rectangle and circumference and area of
circle.'''

import math
def primeter_area(l,b,r):
    print(f"Perimeter of rectangle: {2*(l+b)} units")
    print(f"Area of rectangle: {l*b} sq. units")
    print(f"Circumference of circle: {2*math.pi*r} units")
    print(f"Area of circle: {math.pi*r*r} sq. units")

l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))
r = int(input("Enter the radius of circle:"))
primeter_area(l,b,r)