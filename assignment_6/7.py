def square_dict(n):
    my_dict = {}
    for i in range(0,n+1):
        my_dict[i+1] = (i+1)**2
    print(my_dict)

n = int(input("Enter the value of n:"))
square_dict(n)