'''The set of input is given as ages. Then print the status according to the rules
using a python program.
Age    Status
<2     in born
2-10   child
11-17  young
18-49  adult
50-79  old
>80    very old'''

def age_status(age):
    if age>0:
        print("Ayein??")
    elif age<2:
        print("In born")
    elif age>=2 and age<=10:
        print("Child")
    elif age>=11 and age<=17:
        print("Young")
    elif age>=18 and age<=49:
        print("Adult")
    elif age>=50 and age<=79:
        print("Old")
    else:
        print("Very old")

ages = eval(input("Enter a list of ages:"))
for age in ages:
    age_status(age)


