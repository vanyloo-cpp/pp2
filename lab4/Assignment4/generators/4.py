#4.
#Implement a generator called `squares` to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.
a = int(input())
b = int(input())
def squarez(a, b):
    for i in range(a, b+1):
        yield i ** 2
for i in squarez(a, b):
    print(i)