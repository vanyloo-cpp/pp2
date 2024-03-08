#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string
import os

parent_folder = "C:/Users/Самир/Desktop/pp2/lab6/tasks/Directories/" 


letters_folder = os.path.join(parent_folder, "letters")

if not os.path.exists(letters_folder):
    os.makedirs(letters_folder)

for letter in string.ascii_uppercase:
    file_path = os.path.join(letters_folder, letter + ".txt")
    
    with open(file_path, "w") as file:
        file.writelines(letter)
