#Write a Python script to print Fibonacci series up to n terms.

def fibonacci(n):
    a,b = 0,1
    fibo_series = []
    for i in range(n):
        fibo_series.append(a)
        a,b=b,a+b
    print(f"Fibonacci series upto {n} terms:{fibo_series}")

n = int(input("Enter the range:"))
fibonacci(n)