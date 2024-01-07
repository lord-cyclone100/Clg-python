import pandas as pd
import matplotlib.pyplot as plt
import random as r
r.randint(70,90)
marks = {
    "Sayan":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90)
    },
    "Sangneel":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90)
    },
    "Soham":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90)
    },
    "Sumrina":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90)
    },
    "Satish":{
        "DSA":r.randint(70,90),
        "A&D":r.randint(70,90),
        "COA":r.randint(70,90)
    }
}

df = pd.DataFrame(marks)
df.to_csv("pandas_and_matplotlib//question_2//marks.csv")

new_df = pd.read_csv("pandas_and_matplotlib//question_2//marks.csv",index_col=0)
print (new_df)


avg_list = []
name_list = []
for i in marks:
    x = (df[i].mean()).round(2)

    avg_list.append(x)
    name_list.append(i)


print(avg_list)
print(name_list)

average = {
    "Names":name_list,
    "Average":avg_list
}

avg_df = pd.DataFrame(average)
print(avg_df)

avg_df.plot(kind="bar",x="Names",y="Average")
plt.show()

plt.pie(avg_list,labels=name_list)
plt.show()