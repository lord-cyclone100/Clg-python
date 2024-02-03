#Write a function in python to find the maximum and minimum element in a list within a given range of indices


def main():
    arr=[]
    n=int(input("Enter number of elements : "))
    for i in range(n):
        x=int(input("Enter element : "))
        arr.append(x)
    print("Enter range of indices : ")
    start=int(input("Enter start index : "))
    end=int(input("Enter ending index : "))
    max=arr[start]
    min=arr[start]
    for i in range(start,end+1):
        if arr[i]<min:
            min=arr[i]
        if arr[i]>max:
            max=arr[i] 
    print("Between indices ",start," and ",end," maximum value is : ",max," and minimum value is : ",min)

main()               