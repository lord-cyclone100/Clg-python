'''A positive integer d is said to be a factor of another positive integer N if when N is
divided by d, the remainder obtained is zero. For example, for number 12, there are 6 factors 1,
2, 3, 4, 6, 12. Every positive integer k has at least two factors, 1 and the number k itself. Given
two positive integers N and k, write a program to print the kth largest factor of N.'''

def kth_largest_factor(n, k):
    factor_list = []
    for i in range(1,n+1):
        if n%i==0:
            factor_list.append(i)
    if k>len(factor_list):
        print(f"{n} doesn't have {k} factors")
    else:
        print(f"{k}th largest factor of {n} is {factor_list[-k]}")


n = int(input("Enter a positive number N:"))
k = int(input("Enter a positive number k:"))
kth_largest_factor(n,k)