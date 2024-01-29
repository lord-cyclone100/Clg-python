'''
      1
     1 2
    1 2 3
   1 2 3 4
  1 2 3 4 5
 1 2 3 4 5 6
1 2 3 4 5 6 7
 1 2 3 4 5 6
  1 2 3 4 5
   1 2 3 4
    1 2 3
     1 2
      1
'''


def pattern():
    for i in range(1,8):
        print(" "*(7-i),end="")
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    for i in range(1,7):
        print(" "*i,end="")
        for j in range(1,8-i):
            print(j,end=" ")
        print()

pattern()