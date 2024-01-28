#Write a Python script to create a Simple Calculator on user choice.

def calculator():
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice = int(input("Enter your choice:"))
    if choice==1:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Sum of {a} and {b} is {a+b}")
    elif choice==2:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Difference of {a} and {b} is {a-b}")
    elif choice==3:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        print(f"Product of {a} and {b} is {a*b}")
    elif choice==4:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        if b==0:
            print("Division by zero not possible")
        else:
            print(f"Quotient of {a} and {b} is {a/b}")
    else:
        print("Invalid choice")

calculator()