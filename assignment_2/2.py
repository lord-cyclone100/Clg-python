def num_to_word(n):
    if (n < 0 or n > 9):
        return -1
    num_list = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return num_list[n]

n = int(input("Enter a digit (0-9):"))
s = num_to_word(n)
if (s == -1):
    print("Invalid digit")
else:
    print(f"The number is:{s}")