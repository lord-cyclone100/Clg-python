def update_tuple(my_tuple):
    my_tuple[1][0] = 222
    print(my_tuple)

my_tuple = (11, [22, 33], 44, 55)
update_tuple(my_tuple)