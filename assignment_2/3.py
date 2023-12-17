def divisibility_check(n,m):
    for i in range(1,n+1):
        if (i % m == 0):
            print(f"{i} is divisible by {m}")
            if(i % 2 == 0):
                print(f"{i} is even")
            else:
                print(f"{i} is odd")

n = int(input("Enter the upper limit:"))
m = int(input("Enter the divisibility number:"))
divisibility_check(n,m)