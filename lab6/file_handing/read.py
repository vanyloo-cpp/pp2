f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile.txt", "r")
print(f.read(),"\n")

f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile.txt", "r")
print(f.read(5), '\n')

f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile.txt", "r")
print(f.readline(), "\n")

f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile.txt", "r")
print(f.readline())
print(f.readline(),"\n")

f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile.txt", "r")
for x in f:
  print(x)
print('\n')
f = open("C:/Users/Самир/Desktop/pp2/lab6/file_handing/demofile.txt", "r")
print(f.readline(),)
f.close()