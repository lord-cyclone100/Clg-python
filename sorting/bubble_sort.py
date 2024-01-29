def bubble_sort(l):
    for i in range(len(l)):
        flag = 0
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                flag = 1
        if flag == 0:
            break
    print(f"Sorted list: {l}")

l = eval(input("Enter a list: "))
print(f"Unsorted list: {l}")
bubble_sort(l)