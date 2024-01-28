'''Write a program to accept the age of n employees and count the number of
persons in the following age group: (i) 26 - 35 (ii) 36 - 45 (iii) 46 – 55'''


def count_age_group(age_list):
    age_group_1 = 0
    age_group_2 = 0
    age_group_3 = 0
    for i in age_list:
        if i >= 26 and i <= 35:
            age_group_1 += 1
        elif i >= 36 and i <= 45:
            age_group_2 += 1
        elif i >= 46 and i <= 55:
            age_group_3 += 1
    print(f"Age group 26-35:{age_group_1}")
    print(f"Age group 36-45:{age_group_2}")
    print(f"Age group 46-55:{age_group_3}")

n = int(input("Enter the number of employees:"))
age_list = []
for i in range(n):
    age = int(input(f"Enter the age of employee {i+1}:"))
    age_list.append(age)
count_age_group(age_list)
