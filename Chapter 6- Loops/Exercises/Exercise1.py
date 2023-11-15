# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

while True: # Creates a while loop.
    print ("Please type '0' to quit!") # Prints a string telling the user to input a value to quit.
    pizza_topping = input("What toppings would you like for your pizza?: ") # Allows the user to input a string inside a variable.
    if pizza_topping != '0': # If the input is not "0", the code continues the loop.
        print (f"Your desired pizza topping is {pizza_topping}.\n")
    else:  # Prints a string before;
        print ("\nThank you for ordering our pizza!")
        break # Ending the loop.