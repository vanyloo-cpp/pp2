import os
os.remove("C:/Users/Самир/Desktop/pp2/lab6/file_handing/testfile.txt")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
#To delete an entire folder, use the os.rmdir() method:

os.rmdir("myfolder")