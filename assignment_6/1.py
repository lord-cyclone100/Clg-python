def find_repeat(my_tuple):
    t = []
    repeated_tuple = []
    for i in my_tuple:
        if i not in t:
            t.append(i)
        else:
            if i not in repeated_tuple:
                repeated_tuple.append(i)
    repeated_tuple = tuple(repeated_tuple)
    print(f"Repeated elements are:{repeated_tuple}")

my_tuple = eval(input("Enter the tuple:"))
find_repeat(my_tuple)