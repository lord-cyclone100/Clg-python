def palindrome(num):
    k = num
    rev = 0
    while(num != 0):
        r = num % 10
        num = num // 10
        rev = (rev*10) + r

    if (rev == k):
        return 1
    else:
        return -1

def pal_calc():
    on = 1
    num_list = []
    while(on):
        n = input(f"Enter a number or press q to stop:")
        if (n != 'q'):
            num_list.append(int(n))
        if (n == 'q'):
            on = 0
    for i in num_list:
        h = palindrome(i)
        if (h == 1):
            print(f"{i} is a palindrome\n")

pal_calc()