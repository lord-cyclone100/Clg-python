'''Write a Python function that accepts a string and calculate the number of
uppercase letters and lowercase letters. Sample String : ‘The quick Brown Fox’
Expected Output :
No. Of Uppercase characters : 3
No. Of Lower case Characters : 12'''

def lower_upper(str):
    l = len(str)
    upper_count = 0
    for letter in str:
        if(letter>='A' and letter<='Z'):
            upper_count+=1
    print(f"No of uppercase letters:{upper_count}")
    print((f"No of lowercase letters:{l-upper_count}"))

str = input("Enter a string:")
lower_upper(str)