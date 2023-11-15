#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

#* Use a loop to print the name of each river included in the dictionary.

#* Use a loop to print the name of each country included in the dictionary.

Major_Rivers = {
    'Nile': 'Egypt',
    'Amazon River': 'Peru',
    'Niger': 'Guinea',
    'Rio Grande': 'Colorado',
    'Indus': 'Himalayas',
    }

for river, country in Major_Rivers.items(): # Uses a for-loop to print all the items in the dictionary.
    print("The " + river.title() + " flows through " + country.title() + ".") # Uses an f-string to format the keys and values in one string.

print("\nThese are the rivers that are included in this dictionary:")
for river in Major_Rivers.keys(): # Uses a for-loop to get only the keys in the dictionary.
    print("- " + river.title()) # Uses an f-string to format the keys and values in one string.

print("\nThese are the countries that are included in this dictionary:")
for country in Major_Rivers.values(): # Uses a for-loop to get only the values in the dictionary.
    print("- " + country.title()) # Uses an f-string to format the keys and values in one string.