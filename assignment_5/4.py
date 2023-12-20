def equal_check(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return 1
    return 0

list1 = eval(input("Enter 1st list:"))
list2 = eval(input("Enter 2nd list:"))
s = equal_check(list1,list2)
if s == 1:
    print("True")
else:
    print("False")