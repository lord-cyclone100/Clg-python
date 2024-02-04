'''Write a python program to reduce a string of lowercase characters in
range ascii ['a'..'z'] by doing a series of operations. In each operation, select a pair of
adjacent letters that match, and delete them. Delete as many characters as possible
using this method and return the resulting string. If the final string is empty,
return Empty String.
Input-aabbccdd, output-abd,
Input- abba output-empty string.'''

def reduce_str(str):
    test_str = ''
    for i in range(0,len(str),2):
        if str[i] == str[i+1]:
            test_str += str[i]
    if test_str == '':
        print("Empty String")
    else:
        print(test_str)


str = input("Enter a string:")
reduce_str(str)