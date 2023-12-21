import itertools
l = eval(input("Enter a list:"))
print(f"Permutations of the list are:{list(itertools.permutations(l))}")
r = int(input("How many items would you like to choose:"))
print(f"Combinations of the list are:{list(itertools.combinations(l,r))}")