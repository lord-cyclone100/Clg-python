#A store charges Rs.120 per item if you buy less than 10 items. If you buy between10 and 99 items, the cost is Rs.100 per item. If you buy100 or moreitems, the cost is Rs.70 per item. Write a program that asks the user how many itemstheyare buying and prints the total cost.
def cal_cost(i):
    if(i < 10 and i > 0):
        print(f"Total cost= {i*120}")
        return
    if(i < 100 and i >= 10):
        print(f"Total cost= {i*100}")
        return
    if(i >= 100):
        print(f"Total cost= {i*70}")
        return
    print("Invalid entry")
    return

i = int(input("Enter the number of items:"))
cal_cost(i)