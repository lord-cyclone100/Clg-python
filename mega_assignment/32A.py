'''Write a program to display the maximum and minimum values from the specified
range of indexes of list.'''

def max_min(l,start,end):
    if start<0 or end>len(l):
        return "Invalid index"
    max = l[start]
    min = l[start]
    for i in range(start,end+1):
        if l[i]>max:
            max = l[i]
        if l[i]<min:
            min = l[i]
    return max,min

l = eval(input("Enter a list:"))
start = int(input("Enter start index:"))
end = int(input("Enter end index:"))