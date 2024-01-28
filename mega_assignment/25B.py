#Write a program to move all duplicate values in a list to the end of the list.

def duplicate(my_list):
    unique_list = []
    dup_values = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            dup_values.append(i)
    return unique_list+dup_values


my_list = eval(input("Enter the list:"))
print(duplicate(my_list))