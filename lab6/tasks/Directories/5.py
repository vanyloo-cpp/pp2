#Write a Python program to write a list to a file.
import os

color = ["colum", "word", "number"]
with open('C:/Users/Самир/Desktop/pp2/lab6/tasks/Directories/s.txt', "w") as fr:
        for i in color:
                fr.write("%s\n" % i)
content = open('s.txt')
print(content.read())