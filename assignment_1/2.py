import math as m

def cal_result(x,y,z):
    return ((4*x*4) + (3*y*3) + (9*z) + (6*m.pi))

x = float(input("Enter the value of x:"))
y = float(input("Enter the value of y:"))
z = float(input("Enter the value of z:"))

print(f"Result = {cal_result(x,y,z)}")