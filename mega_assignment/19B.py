'''Write a Python script to find all roots of a quadratic equation ax^2 + bx + c for
all possible combinations of a, b and c'''

import math
def quadratic_roots(a,b,c):
    d = (b**2)-(4*a*c)
    if(d>0):
        root1 = (-b+math.sqrt(d))/(2*a)
        root2 = (-b-math.sqrt(d))/(2*a)
        print(f"Roots are real and distinct:\nRoot1={root1}\nRoot2={root2}")
    elif(d==0):
        root = -b/(2*a)
        print(f"Roots are real and equal:\nRoot1=Root2={root}")
    else:
        real = -b/(2*a)
        imag = math.sqrt(-d)/(2*a)
        print(f"Roots are imaginary:\nRoot1={real}+{imag}i\nRoot2={real}-{imag}i")

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
quadratic_roots(a,b,c)
