def selection_sort(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[j] < l[i]:
                l[j],l[i] = l[i],l[j]
    print(f"Sorted list: {l}")
    
l = eval(input("Enter a list:"))
print(f"Unsorted list: {l}")
selection_sort(l)