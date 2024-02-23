#1. Create a generator that generates the squares of numbers up to some number `N`.
n = int(input())
def gensquares(n):
    for i in range(n+1): 
        if (i**2 > n):
            break
        yield i**2
#gensquares(n)
for i in gensquares(n):
    print(i)