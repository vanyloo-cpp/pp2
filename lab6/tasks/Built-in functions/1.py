#Write a Python program with builtin function to multiply all the numbers in a list
list = list(range(1,11))
r = 1
def mult(my_list, r):
    for i in my_list:
        r = r * i
    return r
print(mult(list, r))