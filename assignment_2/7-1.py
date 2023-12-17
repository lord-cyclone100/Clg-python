def calc_factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

n = int(input("Enter a number:"))
g = calc_factorial(n)
print(f"Factorial of {n} = {g}")