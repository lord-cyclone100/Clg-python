'''Write a Python script to find value of following series:
𝑦 = 1 + 1/2 + 1/3 + … + 1/n where 𝑛 is user input.'''

def series_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=(1/i)
    return sum

n = int(input("Enter the value of n:"))
print(f"Sum={series_sum(n)}")
