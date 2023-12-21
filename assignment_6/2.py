#Method 1
def reverse_tuple(my_tuple):
    r_tuple = my_tuple[::-1]
    print(f"Reversed tuple = {r_tuple}")

#Method 2
def reverse_tuple(my_tuple):
    new_tuple = ()
    for i in range(len(my_tuple)-1,-1,-1):
        new_tuple += (my_tuple[i],)
    print(f"Reversed tuple = {new_tuple}")

my_tuple = eval(input("Enter a tuple:"))
reverse_tuple(my_tuple)