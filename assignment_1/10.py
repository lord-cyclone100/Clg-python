def leap_year(year):
    if(year % 400 == 0):
        return 1
    if(year % 100 == 0):
        return -1
    if(year % 4 == 0):
        return 1
    else:
        return -1

year = int(input("Enter year:"))
n = leap_year(year)

if(n == 1):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")