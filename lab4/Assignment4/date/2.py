import datetime
#2
#Write a Python program to print yesterday, today, tomorrow.


yestr = datetime.date.today() - datetime.timedelta(1)
tmmrw = datetime.date.today() + datetime.timedelta(1)
print('Yesterday : ', yestr)
print('Today :', datetime.date.today())
print('Tomorrow :', tmmrw)
