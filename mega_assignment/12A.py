''' Write a python program to find the Twins primes between a range
( Twin primes are pairs of prime numbers that have just one number between them: 5 and 7, 11 and13,and 29 and 31)'''
def is_prime(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count == 0):
        return 1
    else:
        return 0

def twin_prime(prime_list):
    for i in range(len(prime_list)-1):
        if(prime_list[i+1]-prime_list[i]==2):
            print(f"{prime_list[i]} and {prime_list[i+1]}")

a = int(input("Enter lower bound:"))
b = int(input("Enter upper bound:"))
prime_list = []
for i in range(a,b+1):
    s = is_prime(i)
    if(s):
        prime_list.append(i)
print("Twin primes are:")
twin_prime(prime_list)