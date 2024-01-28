'''Write a program to take N (N > 20) as an input from the user. Print numbers from11 to N. When the number N is a multiple of 3, print "Tipsy", when it is a multipleof 7,
print "Topsy". When it is a multiple of both, print "TipsyTopsy'''

def tipsytopsy(n):
    for i in range(11,n+1):
        if(i%21==0):
            print(f"{i} Tipsy Topsy")
        elif(i%7==0):
            print(f"{i} Topsy")
        elif(i%3==0):
            print(f"{i} Tipsy")
        else:
            print(i)

n = int(input("Enter the value of N:"))
if(n<=20):
    print("Enter a bigger number")
else:
    tipsytopsy(n)