'''Write a python program to reduce a string of lowercase characters in
range ascii ['a'..'z'] by doing a series of operations. In each operation, select a pair of
adjacent letters that match, and delete them. Delete as many characters as possible
using this method and return the resulting string. If the final string is empty,
return Empty String.
Input-aabbccdd, output-abd,
Input- abba output-empty string.'''

def reduce_string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)
    return result if result else "Empty String"

# Example usage:
input_str_1 = "aabbccdd"
output_1 = reduce_string(input_str_1)
print(f"Input: {input_str_1}, Output: {output_1}")

input_str_2 = "baab"
output_2 = reduce_string(input_str_2)
print(f"Input: {input_str_2}, Output: {output_2}")

