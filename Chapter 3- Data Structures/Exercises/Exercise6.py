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
print (f"\nSorry, {name} is sick and cant go to the dinner party.")


# Paul couldn't make the dinner party, Let's go invite Marion to take his place.
print ("\n Paul couldn't make the dinner party, Let's go invite Marion to take his place.")
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


#Your brand new dinner table is bigger than expected, let's go invite more people for dinner.

print ("\nYour brand new dinner table is bigger than expected, let's go invite more people for dinner.")

guests.insert(5, 'Gabriel')
guests.insert(6, 'Yyan')
guests.append('Raphael')

name = guests[0].title()
print (f'\n{name}, would you like to join us for dinner at 8PM sharp tonight?')

name = guests[1].title()
print (f'{name}, do you mind joining us for dinner at 8PM sharp tonight?')

name = guests[2].title()
print (f'{name}, how does dinner sound at 8PM, Monday?')

name = guests[3].title()
print (f"{name}, theres a party at Rafael's place tonight, you coming?")

name = guests[4].title()
print (f"{name}, join us at Rafael's place for dinner at 8PM, Monday!")

name = guests[5].title()
print (f'{name}, are you available on 8PM, Monday? I want to invite you for dinner.')

name = guests[6].title()
print (f"{name}, did you know that there's a dinner party on Rafael's place on Monday, 8M? Let's go!")

name = guests[7].title()
print (f"{name}, are you hungry? Theres a dinner party nearby at Raf's place at 8PM if you want to eat.")


# Dang, the table won't arrive on time. There's only space for 4 people.
print ("\nDang, the table won't arrive on time. There's only space for 4 people.")

name = guests.pop()
print (f"\nSorry {name.title()}, there's no more room to fit you at the table.")

name = guests.pop()
print (f"My bad {name.title()}, apparently there's no more room at the table.")

name = guests.pop()
print (f"Im sorry to say this but, {name.title()}, we're overbooked at the table, we dont have space for  you anymore.")

name = guests.pop()
print (f"My apologies, {name.title()}, the table didn't arrive sooner as expected, we have no more space for your company anymore.")

name = guests.pop()
print (f"Oh no! {name.title()}, the table's not big enough for your company. Sorry.")

name = guests.pop()
print (f"Aw shucks, {name.title()}, you might go home hungry today, there's no more seats available.")


#There should be 2 more people remaining on the list, let's make sure to invite them.

name = guests[0].title()
print (f'\n{name}, would you like to join us for dinner at 8PM sharp tonight?')

name = guests[1].title()
print (f'{name}, do you mind joining us for dinner at 8PM sharp tonight?')

del(guests[0])
del(guests[0])


print(guests)