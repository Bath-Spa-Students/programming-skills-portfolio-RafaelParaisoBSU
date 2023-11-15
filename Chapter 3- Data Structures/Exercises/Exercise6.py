# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

guestlist = ['Wayeth', 'Isaac', 'Paul'] # Stores the strings into a list.

print("Oh no! My tablet wont arrive in time for dinner! We only have 2 spaces left.") # Prints a message that only 2 spaces are left for dinner.

popped_guests = guestlist.pop(2)
print (f"Unfortunately, I cant invite you for dinner {popped_guests}.")

for guests in guestlist: # Uses a for-loop to loop through all the items in the list.
    print (f"Don't worry {guests}! You're still invited to have dinner at 8PM.") # Uses an f-string to format the variable into the string.
