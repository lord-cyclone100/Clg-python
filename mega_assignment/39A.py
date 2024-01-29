'''Python program to accept the strings which contains all vowels
Examples :
Input : ABeeIghiObhkUul
Output : Accepted'''

def vowel_container(str):
    s = str.lower()
    if 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s:
        print("Accepted")
    else:
        print("Not Accepted")

str = input("Enter a string:")
vowel_container(str)