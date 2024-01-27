#Write a Python script to print all Prime numbers between 1 to n.

def is_prime(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count == 0):
        return 1
    else:
        return 0

def print_prime(n):
    prime_list = []
    for i in range(2,n+1):
        s = is_prime(i)
        if(s == 1):
            prime_list.append(i)
    return prime_list

n = int(input("Enter the value of n:"))
print(f"prime numbers in the range:{print_prime(n)}")
