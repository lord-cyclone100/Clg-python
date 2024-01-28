#Write a Python script to check whether a number is Prime number or not

def is_prime(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count == 0):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a not prime number")

n = int(input("Enter a number:"))
is_prime(n)