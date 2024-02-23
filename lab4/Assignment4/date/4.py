import datetime

#4
#Write a Python program to calculate two date difference in seconds.


def date_diff_in_Seconds(date2, date1):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
y = input()#2015-01-01 01:00:00
date1 = datetime.datetime.strptime(y, '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.datetime.now().replace(microsecond= 0)
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()

print(date1)
print(date2)