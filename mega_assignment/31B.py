'''Create the following lists using a for loop:
The list ['a','bb','ccc','dddd',...], that ends with 26 copies of the letter z.'''

def letter_printer():
    letter_list = []
    for i in range(26):
        letter_list.append(chr(97+i)*(i+1))
    print(letter_list)

letter_printer()