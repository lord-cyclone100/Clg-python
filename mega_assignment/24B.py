'''Write programs as per following specifications: "Print the length of the longest
string in the list of strings str_list. Precondition : the list will contain at least one element."'''

def longest_str(str_list):
    if(len(str_list)==0):
        print("List is empty")
        return
    len_list = []
    for i in str_list:
        len_list.append(len(i))
        max_len = max(len_list)
    i = len_list.index(max_len)
    print(f"Largest string is {str_list[i]} with length {max_len}")

str_list = eval(input("Enter the list of strings:"))
longest_str(str_list)