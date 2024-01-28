'''Write a program that takes any two lists L and M of the same size and adds their
elements together to form a new list N whose elements are sums of the corresponding
elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should
equal [4,6,13].'''

def list_add(L,M):
    if(len(L)!=len(M)):
        print("Lists are not of same size")
        return
    N = []
    for i in range(len(L)):
        N.append(L[i]+M[i])
    print(f"List N = {N}")

L = eval(input("Enter 1st list of numbers:"))
M = eval(input("Enter 2nd list of numbers:"))
list_add(L,M)