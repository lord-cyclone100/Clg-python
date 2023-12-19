def capitalize(s):
    l = s.split()
    for i in l:
        length = len(i)
        print(i.title()[:length-1]+i[-1].upper()+" ")

s = input("Enter a string:")
capitalize(s)