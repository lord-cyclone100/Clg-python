'''write a python program to find all occurrences of “India” in given string ignoring the case.'''

def India(str):
    s = str.lower()
    count = 0
    for i in range(len(s)):
        if s[i:i+5] == "india":
            count+=1
            print(f"India found at index {i}")
    print(f"India found {count} times in the given string")


str = "India, india with its rich cultural heritage and diverse landscapes, holds a special place in the hearts of many. From the majestic Himalayas in the north to the serene beaches in the south, India's geographical beauty is unparalleled. The vibrant cities, such as Delhi and Mumbai, showcase the fusion of tradition and modernity. India's history, spanning thousands of years, has left an indelible mark on the world. The cuisine, featuring a myriad of flavors and spices, reflects the country's culinary excellence. Whether you explore the historical sites like the Taj Mahal or embrace the spirituality of Varanasi, India offers a kaleidoscope of experiences. In every corner of India, from the bustling markets to the tranquil countryside, the essence of this incredible nation is deeply ingrained."
India(str)
