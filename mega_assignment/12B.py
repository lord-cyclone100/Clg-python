# Write a Python script to find HCF (GCD) and LCM of two numbers.

def calc_HCF(a,b):
    while b:
        a, b = b, a % b
    return a

def calc_LCM(a,b):
    return ((a*b)//calc_HCF(a,b))


a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print(f"HCF = {calc_HCF(a,b)}")
print(f"LCM = {calc_LCM(a,b)}")