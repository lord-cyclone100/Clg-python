#Write a menu driven program to find out the area of circle, square, rectangle and triangle.

import math

def area_circle(r):
    print(f"Area of the circle = {round(math.pi * (r**2),2)} sq units")

def area_square(s):
    print(f"Area of the square = {s**2} sq units")

def area_rectangle(l,b):
    print(f"Area of the rectangle = {l*b} sq units")

def area_triangle(b,h):
    print(f"Area of the triangle = {round((0.5*b*h),2)} sq units")

on = 1
while(on):
    print('Menu')
    print('1.)Area of circle')
    print('2.)Area of square')
    print('3.)Area of rectangle')
    print('4.)Area of triangle')
    print('0.)Exit')
    n = int(input('Enter your choice:'))
    if(n == 1):
        radius = int(input('Enter the radius of the circle:'))
        area_circle(radius)
    elif(n == 2):
        side = int(input('Enter the side of the square:'))
        area_square(side)
    elif(n == 3):
        length = int(input('Enter the length of the rectangle:'))
        breadth = int(input('Enter the breadth of the rectangle:'))
        area_rectangle(length,breadth)
    elif(n == 4):
        base = int(input('Enter the base of the triangle:'))
        height = int(input('Enter the height of the triangle:'))
        area_triangle(base,height)
    elif(n == 0):
        print('Exiting program....')
        on = 0
    else:
        print('Please enter correct option')