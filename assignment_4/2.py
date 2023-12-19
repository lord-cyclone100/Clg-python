def even_length_words(s):
    l = s.split()
    for i in l:
        if(len(i) % 2 == 0):
            print(i,"\n")

s = input("Enter a string:")
even_length_words(s)