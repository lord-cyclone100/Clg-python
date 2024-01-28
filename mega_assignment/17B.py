#Write a python program to convert a decimal number to a number of a given base b.

def dec_convert(num,base):
    new_str = ''
    while(num!=0):
        new_str=(str(num%base))+new_str
        num = num//base
    print(new_str)

n = int(input("Enter a decimal number:"))
b = int(input("Enter a base:"))
dec_convert(n,b)