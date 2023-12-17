def calc_fact(n):
    if (n == 0):
        return 1
    else:
        return n* calc_fact(n-1)


n = int(input("Enter a number:"))
f = calc_fact(n)
print(f"Factorial of {n} = {f}")
