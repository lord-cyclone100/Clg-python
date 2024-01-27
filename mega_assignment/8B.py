#Write a short program to find the average of some numbers entered throughthekeyboard.
#Output
#Enter numbers (Enter 'q' to see the average)
#2 5 7 15 12 q
#Average = 8.2

def calc_avg():
    on = 1
    avg_list = []
    while (on):
        n = input("Enter any number of q to find average:")
        if (n != 'q'):
            avg_list.append(int(n))
        elif(n == 'q'):
            if(len(avg_list)!=0):
                print(f"Average = {sum(avg_list)/len(avg_list)}")
            elif(len(avg_list)==0):
                print(f"Average = 0")
            on = 0

calc_avg()

