with open("pandas_and_matplotlib//question_4//main-file.txt") as file:
    f = file.readlines()
with open("pandas_and_matplotlib//question_4//copy-file.txt",'w') as file2:
    line_number = 1
    for line in f:
        file2.write(f"{line_number}:{line}")
        line_number += 1

with open("pandas_and_matplotlib//question_4//copy-file.txt") as file3:
    fl = file3.read()

print(fl)