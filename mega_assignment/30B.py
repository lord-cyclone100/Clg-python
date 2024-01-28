'''i. Write a program to compare two equal sized lists and print the first index
where they differ.'''

def compare(l1,l2):
    if len(l1)!=len(l2):
        return "Lists are not of equal size"
    for i in range(len(l1)):
        if(l1[i]!=l2[i]):
            return i

l1 = eval(input("Enter first list:"))
l2 = eval(input("Enter second list:"))
print(f"list 1: {l1}")
print(f"list 2: {l2}")
print(f"First index where they differ: {compare(l1,l2)}")

'''ii. Write a program to reverse a list without using another list or in-built function.'''

my_list = eval(input("Enter a list:"))
print(f"Original list: {my_list}")
print(f"Reversed list:{my_list[::-1]}")