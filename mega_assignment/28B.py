'''Read a text file which contain monthly electricity bills of different customers.
print the electricity consumption for July and November month.'''

with open("28B.txt","r") as file:
    title = file.readline()
    data1 = file.readline().split(",")
    data2 = file.readline().split(",")
    data3 = file.readline().split(",")
    print(data1,data2,data3)

print("Customer1-> July:",data1[7],"November:",data1[11])
print("Customer2-> July:",data2[7],"November:",data2[11])
print("Customer3-> July:",data3[7],"November:",data3[11])