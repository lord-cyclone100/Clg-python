#Display the marks of two students for 5 subjects using suitable graphical tools.

import matplotlib.pyplot as plt
import random as r
import numpy as np

marks_dict = {
    "Student-1":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90),
        "ECO":r.randint(70,90),
        "MATHS":r.randint(70,90)
    },
    "Student-2":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90),
        "ECO":r.randint(70,90),
        "MATHS":r.randint(70,90)
    }
}
label_list = ["DSA","A&D","COA","ECO","MATHS"]
marks_stud1 = []
for i in marks_dict["Student-1"]:
    marks_stud1.append(marks_dict["Student-1"][i])
marks_stud2 = []
for i in marks_dict["Student-2"]:
    marks_stud2.append(marks_dict["Student-2"][i])

x_list = np.arange(5)
y_list = [i+0.3 for i in x_list]

plt.bar(x_list,marks_stud1,width=0.3,label="Student-1")
plt.bar(y_list,marks_stud2,width=0.3,label="Student-2")
plt.legend()
plt.xticks((x_list+0.15),label_list)
plt.show()