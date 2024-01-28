#) Given a list of integers, write a program to find those which are palindromes

def check_palindrome(num):
    temp = num
    rev = 0
    while(num!=0):
        rev = rev*10 + num%10
        num = num//10
    if(temp==rev):
        return 1
    else:
        return 0
    
def palindrome_list(list):
    for num in list:
        if(check_palindrome(num)):
            print(num)

my_list = eval(input("Enter a list of numbers:"))