import math as m

def bin_to_dec(n):
    sum = 0
    p = 0
    for i in n[::-1]:
        sum = sum + (int(i) * m.pow(2,p))
        p += 1
    return sum


n = input("Enter a binary number:")
print(f"Equivalent decimal number: {bin_to_dec(n)}")






























