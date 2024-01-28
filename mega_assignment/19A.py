#Write a Python Program to print the Prime Factors of an Integer.

def is_prime(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count==0):
        return 1
    else:
        return 0

def prime_factors(n):
    factors = []
    for i in range(2,n):
        if(n%i==0):
            if(is_prime(i)):
                factors.append(i)
    return factors

n = int(input("Enter a number:"))
print(f"Prime factors of {n} are:{prime_factors(n)}")