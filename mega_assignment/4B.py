# Remove all duplicates characters from a given string in Python
# Examples:
# Input : abcabcde
# Output : abcde

def remove_duplicates(str):
    result = ''
    for i in str:
        if(i not in result):
            result += i
    print(result)

# Example usage:
str = input("Enter a string:")

print("String after removing duplicates:")
remove_duplicates(str)
