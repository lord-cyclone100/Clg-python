def calculate_si(p,r,t):
    return ((p*r*t)/100)

p = int(input("Enter the principal amount:"))
r = int(input("Enter the rate of interest:"))
t = int(input("Enter the time in years:"))

print(f"Simple Interest = {calculate_si(p,r,t)}")