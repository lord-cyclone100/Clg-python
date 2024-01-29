def union(l1,l2):
    union_list = list(set(l1+l2))
    print(f"Union of {l1} and {l2}: {union_list}")

def intersection(l1,l2):
    intersection_list = []
    for i in l1:
        for j in l2:
            if i==j and i not in intersection_list:
                intersection_list.append(i)
    print(f"Intersection of {l1} and {l2}: {intersection_list}")


l1 = eval(input("Enter 1st list:"))
l2 = eval(input("Enter 2nd list:"))
union(l1,l2)
intersection(l1,l2)