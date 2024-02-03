#Generate the average marks(CGPA) of 10 section then plot it using suitable graph.

import numpy as np
import matplotlib.pyplot as pp
import random

studentgrades=[]
studentname=[]
mks=[]

def getgrade(x):
    if x>40:
        if x>50:
            if x>60:
                if x>70:
                    if x>80:
                        if x>90:
                            return 'O'
                        return 'A'
                    return 'B'
                return 'C'
            return 'D'
        return 'F'

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