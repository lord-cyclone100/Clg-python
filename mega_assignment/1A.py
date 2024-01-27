# Use string slicing to perform the following:
# i. Take a string of length greater than 2, return a string except 1st and last characters.

def removechar(s):
    if (len(s) <= 2):
        print("Enter a larger string")
    else:
        print(s[1:-1])
s= input("Enter a string:")
removechar(s)

# ii. Take 2 strings, s1, and s2 return a new string made of the first, middle and last char of each input string.

def remchar(s):
    mid = len(s)//2
    print(s[1]+s[mid]+s[-1])
s1 = input("Enter 1st string:")
s2 = input("Enter 2nd string:")
print(f"Required strings:")
remchar(s1)
remchar(s2)

# iii. Write a python program to take 2 strings, s1 and s2, create a newstring by appending s2 in the middle of s1

def appendstr(s1,s2):
    print(s1[0:(len(s1)//2)]+s2+s1[(len(s1)//2):])
s1 = input("Enter 1st string:")
s2 = input("Enter 2nd string:")
appendstr(s1,s2)
