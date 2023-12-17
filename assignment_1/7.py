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