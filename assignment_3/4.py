import math as m

def fact(n):
    f = 1
    while(n > 0):
        if(n == 1):
            return 1
        else:
            return (n*fact(n-1)) 

def calc(x):
    return (x - m.pow(x,2)/fact(2) + m.pow(x,3)/fact(3) - m.pow(x,4)/fact(4) + m.pow(x,5)/fact(5) - m.pow(x,6)/fact(6))

x = int(input("Enter the value of x:"))
print(f"Sum:{calc(x)}")