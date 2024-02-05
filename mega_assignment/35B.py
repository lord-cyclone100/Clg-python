'''Store 5 students marks for 6 subjects(randomly) and return average marks of each subject
and topper student.'''

import random

def calc_avg(l):
    avg_list = []
    for i in l:
        avg_list.append(i/6)
    for i in range(5):
        print(f"Average marks of student-{i+1}: {avg_list[i]}")
    print(f"Topper of the class is student-{avg_list.index(max(avg_list))+1}")



student_marks = {
    "student-1": {
        "subject-1": random.randint(70, 90),
        "subject-2": random.randint(70, 90),
        "subject-3": random.randint(70, 90),
        "subject-4": random.randint(70, 90),
        "subject-5": random.randint(70, 90),
        "subject-6": random.randint(70, 90),
    },
    "student-2": {
        "subject-1": random.randint(70, 90),
        "subject-2": random.randint(70, 90),
        "subject-3": random.randint(70, 90),
        "subject-4": random.randint(70, 90),
        "subject-5": random.randint(70, 90),
        "subject-6": random.randint(70, 90),
    },
    "student-3": {
        "subject-1": random.randint(70, 90),
        "subject-2": random.randint(70, 90),
        "subject-3": random.randint(70, 90),
        "subject-4": random.randint(70, 90),
        "subject-5": random.randint(70, 90),
        "subject-6": random.randint(70, 90),
    },
    "student-4": {
        "subject-1": random.randint(70, 90),
        "subject-2": random.randint(70, 90),
        "subject-3": random.randint(70, 90),
        "subject-4": random.randint(70, 90),
        "subject-5": random.randint(70, 90),
        "subject-6": random.randint(70, 90),
    },
    "student-5": {
        "subject-1": random.randint(70, 90),
        "subject-2": random.randint(70, 90),
        "subject-3": random.randint(70, 90),
        "subject-4": random.randint(70, 90),
        "subject-5": random.randint(70, 90),
        "subject-6": random.randint(70, 90),
    },
}

total_list = []
for i in student_marks:
    sum = 0
    for j in range(1,7):
        sum+=student_marks[i][f"subject-{j}"]
    total_list.append(sum)

calc_avg(total_list)