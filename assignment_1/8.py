def hour_check(hour,a):
    if (hour < 1 or hour > 12):
        return -1
    hour_list = [12,1,2,3,4,5,6,7,8,9,10,11]
    return hour_list[(hour+a)%12]

hour = int(input("Enter hour between 1-12:"))
a = int(input("How many hours ahead:"))
s = hour_check(hour,a)
if (s == -1):
    print("Invalid hour")
else:
    print(f"Time at that time would be:{s} O clock")