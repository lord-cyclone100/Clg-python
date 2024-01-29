'''A) Write a program to input N numbers and then print the largest and
second largest number.'''

def largest_secondlargest(l):
    l.sort()
    print(f"Largest element:{l[-1]}")
    print(f"Second largest element:{l[-2]}")

l = eval(input("Enter a list:"))
largest_secondlargest(l)