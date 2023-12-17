def triangle_check(a,b,c):
    if((a + b) > c and (a + c) > b and (c + b) > a):
        if(a == b == c):
            print("The triangle is equilateral")
            return
        if(a == b or b == c or c == a):
            print("The triangle is isoceles")
            return
        else:
            print("The triangle is scalene")
            return
    else:
        print("Triangle is not possible with the given sides")

a = float(input("Enter 1st side of the triangle:"))
b = float(input("Enter 2nd side of the triangle:"))
c = float(input("Enter 3rd side of the triangle:"))

triangle_check(a, b, c)