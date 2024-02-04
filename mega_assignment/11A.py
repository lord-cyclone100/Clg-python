#Write a python program to find out the palindromic prime numbers between a range.

def check_palindrome(n):
    num = n
    rev = 0
    while(n != 0):
        r = n%10
        rev = (rev*10)+r
        n = n // 10
    if(rev == num):
        return 1
    else:
        return 0

def check_prime(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count += 1
    if(count==0):
        p = check_palindrome(n)
        if(p==1):
            print(f"{n} is a palindromic prime number")

a = int(input("Enter lower bound:"))
b = int(input("Enter upper bound:"))

for i in range(a,b+1):
    check_prime(i)
