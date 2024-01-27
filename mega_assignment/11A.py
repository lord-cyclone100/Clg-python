#Write a python program to find out the palindromic prime numbers between a range.

def check_palindrome(n):
    num = n
    rev = 0
    while(n != 0):
        r = n%10
        rev = (rev*10)+r
        n = n // 10
    if(rev == num):
        print(num,end=" ")

a = int(input("Enter lower bound:"))
b = int(input("Enter upper bound:"))

for i in range(a,b+1):
    check_palindrome(i)
