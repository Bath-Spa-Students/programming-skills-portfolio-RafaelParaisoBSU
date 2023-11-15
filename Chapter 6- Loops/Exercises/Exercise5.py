# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

Sandwich_Orders = ['Pastrami','Pastrami','Pastrami','Panini','Mortadella'] # Stores the sandwich toppings into a list.
Finished_Sandwiches = [] # Creates an empty list.

print ("Oh no! Our deli has ran out of Pastrami! Sorry but we won't be able to take Pastrami orders.\n")

while 'Pastrami' in Sandwich_Orders: # Creates a while loop.
    Sandwich_Orders.remove('Pastrami') # Removes Pastrami from the item list.

while Sandwich_Orders: # Creates a while loop.
    ordered = Sandwich_Orders.pop() # Stores the popped items into a variable.
    print (f"Hold on! Your {ordered} sandwich is currently being made.") #
    Finished_Sandwiches.append(ordered) # Prints the popped items.

print () # Breakline

for Sandwich in Finished_Sandwiches: # Uses a for loop for the finished items in the list.
    print (f"Your ordered {Sandwich} sandwich has been finished! Enjoy your meal.") # Uses an f-string to format the code in one string.