#Write a Python script to check whether a number is a Perfect number or not.

def is_perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if(sum == n):
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")

n = int(input("Enter a number:"))
is_perfect(n)