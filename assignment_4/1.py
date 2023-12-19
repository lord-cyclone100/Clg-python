def is_palindrome(s):
    p = s[::-1]
    if p == s:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

def is_symmetric(s):
    n = len(s)
    if(n % 2 != 0):
        print("The entered string is not symmetric")
    else:
        p = s[:n//2]
        q = s[n//2:]
        if p == q:
            print("The entered string is symmetric")
        else:
            print("The entered string is not symmetric")


s = input("Enter a string:")
(is_palindrome(s))
(is_symmetric(s))