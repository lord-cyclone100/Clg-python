#Generate the average marks(CGPA) of 10 section then plot it using suitable graph.

import numpy as np
import matplotlib.pyplot as pp
import random

studentgrades=[]
studentname=[]
mks=[]

def getgrade(x):
    if x<40:return 'F'
    if x>=40 and x<50: return 'D'
    if x>=50 and x<60: return 'C'
    if x>=60 and x<70: return 'B'
    if x>=70 and x<80: return 'A'
    if x>=80 and x<90: return 'E'
    if x>=90 and x<100: return 'O'

def getmarks():
    for i in range(1,11):
        marks=random.randint(41,99)
        mks.append(marks)
        studentgrades.append(getgrade(marks))
        studentname.append("Student "+str(i)+": "+str(getgrade(marks)))

def plott():
    xp=np.array(studentname)
    yp=np.array(mks)
    pp.bar(xp,yp,width=0.5)
    pp.show()

def main():
    getmarks()
    plott()

main()               