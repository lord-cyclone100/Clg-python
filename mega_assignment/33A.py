'''A year is a leap year if it is divisible by 4, except that years divisible by 100
are not leap years unless they are also divisible by 400. Write a program that asks the
user for a year and prints out whether it is a leap year or not.'''


def leap_year(year):
    if year%400==0:
        print(f"{year} is a leap year")
    elif year%100==0:
        print(f"{year} is not a leap year")
    elif year%4==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter a year:"))
leap_year(year)