'''write a program to input a list of numbers and test if a number is equal to the sum
of the cubes of its digits. Print that new list and find the smallest and greatest element
of that list.'''

def max_min(my_list):
    print(f"Max element = {max(my_list)}")
    print(f"Min element = {min(my_list)}")
def digit_cube_sum(my_list):
    for num in my_list:
        cube_list = []
        n = num
        sum = 0
        while n!=0:
            r = n%10
            sum+=(r**3)
            n = n//10
        if(sum==num):
            cube_list.append(num)
    return cube_list

my_list = eval(input("Enter a list of numbers:"))
l = digit_cube_sum(my_list)
print(l)
max_min(l)
