#Program to calculate interest via SI and CI methods

p=int(input("Enter value of principle in Rs.: "))
r=float(input("Enter rate of interest in %: "))
t=int(input("Enter time in years : "))

def si():
    i=(p*r*t)/100
    return i+p

def ci():
    y=1+(r/100)
    amt=p*pow(y,t)
    return amt

def main():
    sim=round(si(),2)
    com=round(ci(),2)
    print("Amount payable in Simple Interest is Rs.",sim)
    print("Amount payable in Compound Interest is Rs.",com)

main()