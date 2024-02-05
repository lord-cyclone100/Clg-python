'''Program to check a number is ugly or not. Ugly numbers are positive numbers whose only
prime factors are 2, 3 or 5.'''

def uglyNum(n):
    if n==1:
        return True
    if not n%2 or not n%3 or not n%5:
        return True
    return False

a = int(input("Enter a number: "))
if(uglyNum(a)):
    print("The Number is Ugly")
else:
    print("The Number is not Ugly")