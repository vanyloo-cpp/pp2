#Write a Python program to count the number of lines in a text file.
name = "C:/Users/Самир/Desktop/pp2/lab6/tasks/Directories/text.txt"
def file(name):
    with open(name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", file("C:/Users/Самир/Desktop/pp2/lab6/tasks/Directories/text.txt"))
