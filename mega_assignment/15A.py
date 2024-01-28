#Write a Python script to check whether a number is an Armstrong number or not.

def count_digits(n):
    count = 0
    while n!=0:
        count+=1
        n=n//10
    return count

def check_armstrong(n):
    u = count_digits(n)
    num = n
    sum = 0
    while n!=0:
        sum+=((n%10)**u)
        n=n//10
    if(sum == num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

n = int(input("Enter a number:"))
check_armstrong(n)