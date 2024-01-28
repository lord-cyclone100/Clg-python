'''Write a Python script for the following…
An electric distribution companies arranges its domestic consumer as follows:
Consumption in Units                Rate of charge
0 – 200                             Rs. 0.50 per unit
201 – 400                           Rs. 100 plus Rs. 0.65 per unit excess to 200
400 – 600                           Rs. 250 plus Rs. 0.80 per unit excess to 400
Above 600                           Rs. 425 plus Rs. 1.25 per unit excess to 600
Print the amount to be paid by the consumer.'''

def bill(units):
    if units<0:
        return "Invalid units"
    if units>=0 and units<=200:
        return units*0.5
    elif units<=400:
        return 100+(units-200)*0.65
    elif units<=600:
        return 250+(units-400)*0.8
    else:
        return 425+(units-600)*1.25

units = int(input("Enter the units consumed:"))
print(f"Amount to be paid: Rs{bill(units)}")