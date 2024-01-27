#Write a python program to take an input list and removes the element at index 4 and add it to the 2nd position and also, at the end of the list.

def update_list(my_list):
    if(len(my_list)<=4):
        print("List is too short")
    else:
        element = my_list[4]
        my_list.remove(element)
        my_list.insert(2,element)
        my_list.append(element)
        print(my_list)

my_list = eval(input("Enter a list:"))
update_list(my_list)