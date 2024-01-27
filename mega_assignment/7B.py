#Write a Python function that takes a list and returns a new list with unique elementsof the first list.
#Sample List : [1,2,3,3,3,4,3,5]
#Unique List : [1, 2, 3, 4, 5]

def unique(sample_list):
    unique_list = []
    for i in sample_list:
        if i not in unique_list:
            unique_list.append(i)
    return (unique_list)

sample_list = []

n = int(input("How many elements would you enter:"))
for i in range(n):
    element = int(input("Enter element:"))
    sample_list.append(element)
print(sample_list,"\n",unique(sample_list))