# Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def description(city, country = 'Japan'): # Creates a function that has the default value of Japan.
    city = f"The city of {city.title()} is in the beautiful country {country.title()}!\n"
    print(city)

description('Tokyo') # Calls the function and changes its given values.
description('Sharjah', 'U.A.E.')
description('Kyoto')