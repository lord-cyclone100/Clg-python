max = 5
stack = []

def push(value):
    if(len(stack)>=max):
        print("Stack overflow")
        return
    stack.append(value)
    return

def pop():
    if(len(stack)==0):
        print("Stack underflow")
        return;
    stack.pop(-1)
    return

def display():
    if(len(stack)==0):
        print("Stack is empty")
        return
    print(stack[::-1])
    return

def peek():
    if (len(stack) == 0):
        print("Stack is empty")
        return
    return stack[-1]

def isempty():
    if(len(stack)==0):
        print("Stack is empty")
        return
    else:
        print("Stack is not empty")
        return

def isfull():
    if(len(stack)==max):
        print("Stack is full")
        return
    else:
        print("Stack is not full")
        return


on = 1
while(on):
    print("\nMenu")
    print("1.)Push")
    print("2.)Pop")
    print("3.)Display")
    print("4.)Peek")
    print("5.)Is empty")
    print("6.)Is full")
    print("0.)Exit")

    choice = int(input("Enter your choice:"))
    if(choice == 1):
        value = int(input("Enter the value to push:"))
        push(value)

    if (choice == 2):
        pop()

    if (choice == 3):
        display()

    if (choice == 4):
        p = peek()
        print("Top element is:",p)

    if (choice == 5):
        isempty()

    if (choice == 6):
        isfull()

    if (choice == 0):
        print("Exiting...")
        on = 0