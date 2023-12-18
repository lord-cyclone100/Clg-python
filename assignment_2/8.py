n = int(input("Enter number of rows:"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if (j>=i):
            print("  ",end=" ")
    for k in range(2*n-1):
        if(k< ((2*i) - 1)):
            print("+ ",end=" ")
    print("\n")