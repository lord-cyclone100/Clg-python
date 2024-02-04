max = 5
queue = []

def enqueue(value):
    if(len(queue)>=max):
        print("Queue overflow")
        return
    queue.append(value)
    return

def dequeue():
    if(len(queue)==0):
        print("Queue underflow")
        return
    queue.pop(0)
    return

def display():
    if(len(queue)==0):
        print("Stack is empty")
        return
    print(queue)
    return

def peek():
    if (len(queue) == 0):
        print("Queue is empty")
        return
    return queue[-1]

def isempty():
    if(len(queue)==0):
        print("Queue is empty")
        return
    else:
        print("Queue is not empty")
        return

def isfull():
    if(len(queue)==max):
        print("Queue is full")
        return
    else:
        print("Queue is not full")
        return


on = 1
while(on):
    print("\nMenu")
    print("1.)Enqueue")
    print("2.)Dequeue")
    print("3.)Display")
    print("4.)Peek")
    print("5.)Is empty")
    print("6.)Is full")
    print("0.)Exit")

    choice = int(input("Enter your choice:"))
    if(choice == 1):
        value = int(input("Enter the value to enqueue:"))
        enqueue(value)

    if (choice == 2):
        dequeue()

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