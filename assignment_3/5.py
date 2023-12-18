def is_prime(x):
    c = 0
    for i in range(2,x):
        if(x%i == 0):
            c += 1
    return (c == 0)

def calc_GCD(n1,n2):
    if (n2 == 0):
        return n1
    else:
        return (calc_GCD(n2,n1%n2))
    
def calc_LCM(n1,n2):
    return ((n1*n2)//calc_GCD(n1,n2))

n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
print(f"GCD of {n1} and {n2} = {calc_GCD(n1,n2)}")
print(f"LCM of {n1} and {n2} = {calc_LCM(n1,n2)}")