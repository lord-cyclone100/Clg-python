def avg_calc():
    on = 1
    num_list = []
    while(on):
        n = input(f"Enter a number or press q to find average:")
        if (n != 'q'):
            num_list.append(int(n))
        if (n == 'q'):
            on = 0
    if(len(num_list) != 0):
        print(f"Average:{sum(num_list)/len(num_list)}")
    else:
        print("Average:0.0")

avg_calc()