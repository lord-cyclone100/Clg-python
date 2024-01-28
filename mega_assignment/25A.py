'''Write programs to find the sum of the following series:
x - x^2 /2! + x^3 /3! - x^4 /4! + x^5 /5! - x^6 /6! (Input x)'''

def factorial(n):
    product = 1
    while(n!=0):
        product*=n
        n-=1
    return product

def series_sum(x):
    sum = 0
    for i in range(6):
        f = factorial(i+1)
        sum+=(((x**(i+1))/f)*(-1**i))
    print(f"Sum={sum}")

x = int(input("Enter the value of x:"))
series_sum(x)
