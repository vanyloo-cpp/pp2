#2. Write a program using generator 
# to print the even numbers between 0 and `n` in comma separated form where `n` is input from console.
n = int(input())
def evenNumb(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i 
for i in evenNumb(n):
    print(i)
