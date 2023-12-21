def new_tuple(my_tuple):
    t = ()
    for i in my_tuple:
        if i == 44 or i == 55:
            t+=(i,)
    print(f"Updated tuple:{t}")

my_tuple = (11, 22, 33, 44, 55, 66)
new_tuple(my_tuple)