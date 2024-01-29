'''Write a program that reads a file line by line. Each line read from the file1 is copied to
another file with line number specified at the beginning of the line.'''

with open("40B-givenfile.txt",mode="r") as file:
    data = file.readlines()
print(data)
with open("40B-generatedfile.txt",mode="w") as file:
    line_number = 1
    for line in data:
        file.write(f"{line_number}.) {line}")
        line_number += 1