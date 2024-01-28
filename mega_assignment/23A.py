'''Write a Python program to sum the sequence: 1 + 1/1! + 1/2! + 1/3! + + 1/n!
(Input n through keyboard)'''

def factorial(n):
    product = 1
    while(n!=0):
        product*=n
        n-=1
    return product

def series_sum(n):
    sum = 0
    for i in range(n+1):
        f = factorial(i)
        sum+=(1/f)
    return sum

n = int(input("Enter the value of n:"))
s = series_sum(n)
print(f"Sum={s}")