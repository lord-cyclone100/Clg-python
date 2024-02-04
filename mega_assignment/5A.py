'''write a python program to find all occurrences of “India” in given string ignoring the case.'''

def India(str):
    s = str.lower()
    print(s.find("india"))


str = input("Enter a string:")
India(str)
