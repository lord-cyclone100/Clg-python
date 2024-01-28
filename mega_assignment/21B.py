#Write Python programs to sum the given sequences up to n terms: 2/9 - 5/13 + 8/17…

def series_sum(n):
    sum = 0
    a,b = 2,9
    for i in range(n):
        sum+=(a/b)*((-1)**i)
        a+=3
        b+=4
    return sum

n = int(input("Enter the value of n:"))
s = series_sum(n)
print(f"Sum={s}")