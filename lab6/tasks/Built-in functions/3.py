#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
def palindrome_string(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]
print(palindrome_string(s))