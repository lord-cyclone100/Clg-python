#Write a python program to find the last position of a substring “Emma” in a givenstring.
def last_pos(str):
    s = str.rfind("Emma")
    print(f"Last position of Emma is:{s}")

str = "Emma is a great student. Emma likes programming. Emma is diligent."
last_pos(str)
