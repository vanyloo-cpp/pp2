#3.
#Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and `n`.
n = int(input())
def div_3_4(n):
    for i in range(n+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i
for i in div_3_4(n):
    print(i)