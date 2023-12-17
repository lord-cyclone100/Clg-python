def close(n1,n2):
    return (abs(n1-n2)<= 0.001)

n1 = float(input("Enter 1st number:"))
n2 = float(input("Enter 12nd number:"))

if(close(n1,n2)):
    print("Close")
else:
    print("Not close")