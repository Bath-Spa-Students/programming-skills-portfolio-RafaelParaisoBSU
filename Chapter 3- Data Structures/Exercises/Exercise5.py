# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

guestlist = ['Wayeth', 'Joshua', 'Andrei', 'Isaac', 'Paul'] # Stores the strings into a list.

print("Paul wont make it to the dinner! Let's invite someone else.")
guestlist[4] = ("Marion")

for guests in guestlist: # Uses a for-loop to loop through all the items in the list.
    print (f"Hello {guests}, would you like to have dinner at 8PM?") # Uses an f-string to format the variable into the string.
