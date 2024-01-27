#Write a Python program to print every integer between 1 and n divisible by m. Also report whether the number that is divisible by m is even or odd.

def odd_even(n):
    if(n%2==0):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

def divisibility(n,m):
    for i in range(1,n+1):
        if(i%m==0):
            print(f"{i} is divisible by {m}")
            odd_even(i)

n = int(input("Enter the value of n:"))
m = int(input("Enter the value of m:"))
divisibility(n,m)