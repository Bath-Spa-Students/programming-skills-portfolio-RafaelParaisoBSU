guests = ['Wayeth', 'Joshua', 'Andrei', 'Isaac', 'Paul']

name = guests[0].title()
print (f'{name}, would you like to join us for dinner at 8PM sharp tonight?')

name = guests[1].title()
print (f'{name}, do you mind joining us for dinner at 8PM sharp tonight?')

name = guests[2].title()
print (f'{name}, how does dinner sound at 8PM, Monday?')

name = guests[3].title()
print (f"{name}, theres a party at Rafael's place tonight, you coming?")

name = guests[4].title()
print (f"Sorry, {name} is sick and cant go to the dinner party.")

# Paul couldn't make the dinner party, Let's go invite Marion to take his place.
del(guests[4])
guests.insert(4, 'Marion')

#Re-inviting the other Guests.

name = guests[0].title()
print (f'\n{name}, would you like to join us for dinner at 8PM sharp tonight?')

name = guests[1].title()
print (f'{name}, do you mind joining us for dinner at 8PM sharp tonight?')

name = guests[2].title()
print (f'{name}, how does dinner sound at 8PM, Monday?')

name = guests[3].title()
print (f"{name}, theres a party at Rafael's place tonight, you coming?")

name = guests[4].title()
print (f"{name}, Have you heard of the party happening at Rafael's place at 8PM? Should we join them?")