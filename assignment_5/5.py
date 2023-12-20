def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

def check_prime(l):
    for element in l:
        c = is_prime(element)
        if(c == 0):
            print("False")
            return
    print("True")

l = eval(input("Enter the list:"))
check_prime(l)