'''Print the following pattern using Python program
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1'''

import math
n = int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(i+1,0,-1):
        print((2**(j-1)),end=" ")
    print("\n")
