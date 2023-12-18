def age_group(employee_list):
    a = b = c = 0
    for i in employee_list:
        if(i>=26 and i<=35):
            a +=1
        if(i>=36 and i<=45):
            b +=1
        if(i>=46 and i<=55):
            c +=1
    print(f"Employees in age group 26 - 35:{a}")
    print(f"Employees in age group 36 - 45:{b}")
    print(f"Employees in age group 46 - 55:{c}")


n = int(input("Enter the number of employees:"))
employee_list = []
for i in range(n):
    a = int(input("Enter employee age:"))
    employee_list.append(a)

age_group(employee_list)