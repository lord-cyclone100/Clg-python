def make_dict(keys,values):
    my_dict = {}
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]
    print(my_dict)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
make_dict(keys,values)