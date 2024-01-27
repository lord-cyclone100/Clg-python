'''Write programs using nested loops to produce the following patterns:
A
A B
A B C
A B C D
A B C D E
A B C D E F'''

n = int(input("Enter the number of rows:"))
for i in range(n):
    k = 0
    for j in range(i+1):
        print(chr(65+k),end = " ")
        k+=1
    print("\n")