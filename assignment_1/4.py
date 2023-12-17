def rev_num(n):
    rev = 0
    while(n != 0):
        r = n % 10
        n = n // 10
        rev = (rev * 10) + r
    return rev

n = int(input("Enter a number:"))
print(f"Reversed number:{rev_num(n)}")