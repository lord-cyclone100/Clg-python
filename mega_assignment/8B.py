#Write a short program to find the average of some numbers entered throughthekeyboard.
#Output
#Enter numbers (Enter 'q' to see the average)
#2 5 7 15 12 q
#Average = 8.2

def avg(my_list):
    if (len(my_list) == 0):
        print("Average is 0")
    else:
        print(f"Average is {sum(my_list) / len(my_list)}")


my_list = []
on = 1
while (on):
    n = input("Enter a number or press 'q' to stop:")
    if (n.lower() == 'q'):
        on = 0
    elif (n <= '0' or n >= '9'):
        print("Please enter a valid entry")
    else:
        my_list.append(int(n))

avg(my_list)

