def max_max2(n):
    my_list = my_list2 = []
    for i in range(n):
        q = int(input("Enter number:"))
        my_list.append(q)
    print(max(my_list))
    my_list.remove(max(my_list))
    print(max(my_list))

n = int(input("How many integers would you like to insert:"))
max_max2(n)