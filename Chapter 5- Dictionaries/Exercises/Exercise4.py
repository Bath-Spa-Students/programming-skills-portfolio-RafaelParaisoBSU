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

for river, country in Major_Rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in Major_Rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in Major_Rivers.values():
    print("- " + country.title())