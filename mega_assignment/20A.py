'''Python program to check if a given string is binary string or not
Examples:
Input: str = "01010101010"
Output: Yes'''

def check_binary(str):
    for char in str:
        if char!='0' and char!='1':
            return 0
    return 1

str = input("Enter a string:")
if(check_binary(str)):
    print("The string is binary")
else:
    print("The string is not binary")