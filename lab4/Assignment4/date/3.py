import datetime

#3
#Write a Python program to drop microseconds from datetime.

x = datetime.datetime.today().replace(microsecond = 0)
print(x)
