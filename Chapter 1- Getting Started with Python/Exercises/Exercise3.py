#Write a Python program to display the current date and time.

import datetime
today = datetime.datetime.today()
print (today.strftime("%d-%M-%Y %H:%M:%S"))