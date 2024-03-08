#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
if os.path.exists("C:/Users/Самир/Desktop/pp2/lab6/tasks/Directories/delete.py"):
  os.remove("C:/Users/Самир/Desktop/pp2/lab6/tasks/Directories/delete.py")
else:
  print("The file does not exist")