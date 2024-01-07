def file(tabs,spaces,new_lines):
    with open("pandas_and_matplotlib//question_3//file.txt") as file:
        data = file.read()
        
        for i in data:
            if (i == " "):
                spaces += 1

            elif (i == "\t"):
                tabs += 1

            elif (i == "\n"):
                new_lines += 1

    n = [tabs, spaces, new_lines]
    return n

tabs = spaces = new_lines = 0
a = file(tabs, spaces, new_lines)
print("\n")
print(f"Number of tabs:{a[0]}")
print(f"Number of spaces:{a[1]}")
print(f"Number of newlines:{a[2]}")