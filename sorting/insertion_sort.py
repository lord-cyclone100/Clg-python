def insertion_sort(l):
    for i in range(1,len(l)):
        s = l[i]
        j = i - 1
        while((l[j] > s) and j >= 0):
            l[j+1] = l[j]
            j-=1
        l[j+1] = s
    print(f"Sorted list: {l}")
    
l = eval(input("Enter a list:"))
print(f"Unsorted list: {l}")
insertion_sort(l)