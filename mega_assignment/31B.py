def letter_printer():
    letter_list = []
    for i in range(26):
        letter_list.append(chr(97+i)*(i+1))
    print(letter_list)

letter_printer()