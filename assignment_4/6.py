def remove_duplicate(s):
    rev = ""
    for i in s:
        if((i not in rev) and (i.upper() not in rev)):
        # if(i not in rev):
            rev = rev + i
    return rev

s = input("Enter a string:")
r = remove_duplicate(s)
print(r)