def checkNumAndAlpha(s):
    alpha = num = False
    for i in s:
        if i.isdigit():
            num = True
        elif i.isalpha():
            alpha = True
    return (num and alpha)  

s = input("Enter a string:")
print(checkNumAndAlpha(s))