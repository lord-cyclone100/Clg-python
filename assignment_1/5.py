import math as m

def cal_cube(a,b):
    return (m.pow(a,3) + 3*m.pow(a,2)*b + 3*a*m.pow(b,2) + m.pow(b,3))

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print(f"Result = {cal_cube(a,b)}")