# Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

age = 72

if age < 2: # If the person is less than 2 years old, print a message that the person is a baby.
    print ("You're a baby!")
elif age < 3: # If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
    print ("You're a toddler!")
elif age < 4: # If the person is at least 4 years old but less than 13, print a message that the person is a kid.
    print ("You're a kid!")
elif age < 13: # If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
    print ("You're an teenager!")
elif age < 65: # If the person is at least 20 years old but less than 65, print a message that the person is an adult.
    print ("You're an adult!")
else: # If the person is age 65 or older, print a message that the person is an elder.
    print ("Wow! Hope you continue to have a long life!")