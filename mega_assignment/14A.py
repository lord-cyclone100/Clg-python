'''Write a Python program that accepts a hyphen-separated sequence of words asinput and prints the words in a hyphen-separated sequence after sorting themalphabetically.
Sample Input : green-red-yellow-black-white
Output : black-green-red-white-yellow'''

def hyphen(str):
    p = str.split("-")
    p.sort()
    print('-'.join(p))

str = input("Enter a hyphen separated string:")
hyphen(str)