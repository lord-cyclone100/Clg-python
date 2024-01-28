'''Python program to check if a string has at least one letter and one number
Examples:
Input: welcome2ourcountry34
Output: True
Input: stringwithoutnum
Output: False'''

def check_string(str):
    letter_flag = False
    number_flag = False
    for char in str:
        if char.isalpha():
            letter_flag = True
        if char.isdigit():
            number_flag = True
    return letter_flag and number_flag

print(check_string("welcome2ourcountry34"))
print(check_string("stringwithoutnum"))
