#)Write a program to convert centigrade to Fahrenheit and reverse also.

def cel_to_far(temp):
    far_temp = ((9/5)*temp) + 32
    return far_temp

def far_to_cel(temp):
    cel_temp = (5/9)*(temp - 32)
    return cel_temp

temp = int(input("Enter celcius temperature:"))
print(f"Equivalent farenheit:{cel_to_far(temp)}")

temp = int(input("Enter farenheit temperature:"))
print(f"Equivalent celcius:{far_to_cel(temp)}")