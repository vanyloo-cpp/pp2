# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
s = input()
result = re.search("a.*b$", s)
print(result)