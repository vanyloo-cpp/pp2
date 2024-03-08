#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
 
print("Test a path exists or not:")
path = 'C:/Users/Самир/Desktop/pp2/lab6/file_handing'
print(os.path.exists(path))
path = 'C:/Users/Самир/Desktop/pp2/lab6/file_handing'
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))