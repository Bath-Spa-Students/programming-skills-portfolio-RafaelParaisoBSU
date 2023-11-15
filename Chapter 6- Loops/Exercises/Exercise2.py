# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their  age, and then tell them the cost of their movie ticket

age = int(input("What is your age?:"))

if age < 3:
        print ("The tickets for children that are 3 and below are free :)")
elif age < 13:
        print ("The tickets for those between 3 and 12 are priced 10$ :)")
else:
        print ("The ticket prices for ages 13 and above is 15$")

