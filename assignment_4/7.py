def binary(s):
    count = 0
    for i in s:
        if(i != '0' and i != '1'):
            count+=1
    return count

s = input("Enter a string:")
c = binary(s)
if(c == 0):
    print("Yes")
else:
    print('No')