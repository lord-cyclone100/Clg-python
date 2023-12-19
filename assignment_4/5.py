def vowel(s):
    if (("A" in s or "a" in s) and ("E" in s or "e" in s) and ("I" in s or "i" in s )and ("O" in s or "o" in s) and ("U" in s or "u" in s)):
        print("Accepted")
    else:
        print("Not Accepted")

s = input("Enter a string:")
vowel(s)