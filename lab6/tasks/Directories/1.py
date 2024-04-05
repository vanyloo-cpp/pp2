#Напишите программу на Python, которая будет отображать только каталоги, файлы и все каталоги и файлы по указанному пути.

import os
path = 'C:/Users/Самир/Desktop/pp2/lab6/file_handing'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
