'''Read a text file which contain monthly electricity bills of different customers.
print the electricity consumption for July and November month.'''

with open("28B.txt","r") as file:
    data = file.readlines()
    print(f"{data[6]}\n{data[10]}")