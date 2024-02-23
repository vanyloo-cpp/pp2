#5.
#Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
def decreas(n):
    for i in range(n, -1, -1):
        yield i
for i in decreas(n):
    print(i)