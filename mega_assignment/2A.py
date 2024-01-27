#Write a program to take a year as input and check If it is a leap year or not.

def check_leap(year):
    if(year%400 == 0):
        print(f"{year} is a leap year")
    elif(year%100 == 0):
        print(f"{year} is not a leap year")
    elif(year%4 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter a year:"))
check_leap(year)