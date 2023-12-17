def sec_calculate(seconds):
    print(f"{seconds} seconds = {seconds//60} minutes and {seconds%60} seconds")

seconds = int(input("Enter the number of seconds:"))
sec_calculate(seconds)