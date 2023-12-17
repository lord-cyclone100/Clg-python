def cm_to_inch(l):
    if (l<0):
        return -1
    return 1

l = float(input("Enter length in cm:"))
s = cm_to_inch(l)

if(s == -1):
    print("Negative length not allowed")

else:
    print(f"{l} cm = {l / 2.54} inch")
