# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet


Pets = []
pet = {
    'Species': 'Persian Cat',
    'Name': 'Lilac',
    'Owner': 'Rafael',
    'Country': 'U.A.E.',
    'Diet': 'Cat Food',
}
Pets.append(pet)

pet = {
    'Species': 'British Longhair Cat',
    'Name': 'Maverick',
    'Owner': 'Wayeth',
    'Country': 'U.A.E.',
    'Diet': 'Organic Food',
}
Pets.append(pet)

pet = {
    'Species': 'Dog',
    'Name': 'Marc',
    'Owner': 'Wayeth',
    'Country': 'Africa',
    'Diet': 'Dog Food',
}
Pets.append(pet)

for pet in Pets:
    print("\nHere's what I know about " + pet['Name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))