'''Say a box of cookies can hold 24 cookies, and a container can hold 75 boxes of
cookies. Write a program that prompts the user to enter the total number of cookies,
then outputs the number of boxes and the number of containers to ship the cookies.
Note that each box must contain the specified number of cookies, and each container
must contain the specified number of boxes. If the last box of cookies contains
less than the number of specified cookies, you can discard it and output the number of
leftover cookies. Similarly, if the last container contains less than the number of
specified boxes, you can discard it and output the number of leftover boxes.
Take the capacity of the box and container from the keyboard.'''

def cookies(c):
    boxes = c//24
    leftover_boxes = c%24
    containers = boxes//75
    leftover_containers = boxes%75
    print(f"The number of boxes required to pack {c} cookies: {boxes}")
    print(f"Leftover cookies: {leftover_boxes}")
    print(f"The number of containers required to pack {boxes} boxes: {containers}")
    print(f"Leftover boxes: {leftover_containers}")

c = int(input("Enter total no of cookies:"))
cookies(c)