#Write a Python program to display the current date and time.

import datetime # Fetches the current date and time of your system.
today = datetime.datetime.today()
print (today.strftime("%d-%M-%Y %H:%M:%S")) # Prints a formatted current time and date. 