"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""
f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile2.txt", "r")
print(f.read(), "\n")

f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile3.txt", "r")
print(f.read())