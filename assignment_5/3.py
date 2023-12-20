def intersection(list1,list2):
    i_list = []
    for i in list1:
        for j in list2:
            if ((i not in i_list) and i == j):
                i_list.append(i)
    print(f"Intersection of {list2} and {list2}: {i_list}")

def union(list1, list2):
    u_list = []
    for i in list1:
        if i not in u_list:
            u_list.append(i)
    for i in list2:
        if i not in u_list:
            u_list.append(i)
    print(f"Union of {list1} and {list2}: {u_list}")

list1 = eval(input("Enter 1st list:"))
list2 = eval(input("Enter 2nd list:"))
union(list1, list2)
intersection(list1, list2)