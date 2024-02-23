import datetime

#1
#Write a Python program to subtract five days from current date.


dt = datetime.date.today() - datetime.timedelta(5)

print('Current Date :',datetime.date.today())
print('5 days before Current Date :',dt)