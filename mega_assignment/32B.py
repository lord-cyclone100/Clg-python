'''Program to check a number is ugly or not. Ugly numbers are positive numbers whose only
prime factors are 2, 3 or 5.'''

n=int(input("Enter a number : "))

def isPrime(x): 
    f=0
    for i in range(2,x//2):
        if x%i==0:
            f+=1
    if f==0:
        return True
    else:
        return False
    
def checkugly():
    f=0
    for i in range(1,n+1):
        if(n%i==0 and isPrime(i)):
            if(i==2 or i==3 or i==5):
                f=0
            else: 
                f+=1
    return f

def main():
    x=checkugly()   
    if x==0 or n==1:
        print(n,"is ugly") 
    else:
        print(n,"is not ugly")  

main()                               