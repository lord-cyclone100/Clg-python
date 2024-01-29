'''A student’s grade is calculated in a subject according to the following rules:
Number Obtained         Grade
>=90 and <=100          O
>=80 and <90            E
>=70 and <80            A
>=60 and <70            B
>=50 and <60            C
>=40 and <50            D
<40 and >=0             F(FAILED)
Others No.              INVALID
Write a Python script which accepts a student’s marks as an input and then determine
the grade of the students in that subject.'''

def grade(marks):
    if marks >= 90 and marks <= 100:
        print ("Grade: O")
    elif marks >= 80 and marks < 90:
        print ("Grade: E")
    elif marks >= 70 and marks < 80:
        print ("Grade: A")
    elif marks >= 60 and marks < 70:
        print ("Grade: B")
    elif marks >= 50 and marks < 60:
        print ("Grade: C")
    elif marks >= 40 and marks < 50:
        print ("Grade: D")
    elif marks >= 0 and marks < 40:
        print ("Grade: F(FAILED)")
    else:
        print ("INVALID")

marks = int(input("Enter the marks:"))
grade(marks)