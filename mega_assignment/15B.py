'''Write a Python function to check whether a string is a pangram or not. Pangramsare words or sentences containing every letter of the alphabet at least once.
For example : “The quick brown fox jumps over the lazy dog”'''

def check_pangram(n):
    low = n.lower()
    print(low)
    count = 0
    test_str = ''
    for letter in low:
        if letter not in test_str:
            test_str+=letter
    if(len(test_str)>=26):
        print("The string is a pangram")
    else:
        print("The string is not a pangram")

check_pangram("Pack my box with five dozen liquor jugs")