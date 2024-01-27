#Write a python program to find the mean and median of a set of elements.

def mean(sequence):
    print(sequence)
    print(f"Mean is:{sum(sequence)/len(sequence)}")

def median(sequence):
    l = len(sequence)
    if(l%2 == 1):
        print(f"Median is:{sequence[l//2]}")
    else:
        print(f"Median is:{(sequence[l//2]+sequence[(l//2)-1])/2}")
sequence = [15, 7, 2, 20, 11, 8]
sequence.sort()
mean(sequence)
median(sequence)