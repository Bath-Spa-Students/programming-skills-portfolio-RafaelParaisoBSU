# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

Sandwich_Orders = ['Italian','Meatball','Grilled Cheese','Panini','Mortadella'] # Stores the sandwich toppings into a list.
Finished_Sandwiches = [] # Creates an empty list.

while Sandwich_Orders: # Creates a while loop.
    ordered = Sandwich_Orders.pop() # Stores the popped items into a variable.
    print (f"Hold on! Your {ordered} sandwich is currently being made.") #
    Finished_Sandwiches.append(ordered) # Prints the popped items.

print () # Breakline

for Sandwich in Finished_Sandwiches: # Uses a for loop for the finished items in the list.
    print (f"Your ordered {Sandwich} sandwich has been finished! Enjoy your meal.") # Uses an f-string to format the code in one string.
 