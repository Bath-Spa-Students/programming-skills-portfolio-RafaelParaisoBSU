# Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

#•	 If the alien is green, print a message that the player earned 5 points.

#•	 If the alien is yellow, print a message that the player earned 10 points.

#•	 If the alien is red, print a message that the player earned 15 points.

#•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.

Alien_Color = 'Dark_Green' # Stores a string in a variable.

if Alien_Color == 'Dark_Green': # If statement that prints if the variable is "Dark Green"
        print ("Wow! You shot the Dark Green Alien! You won 5 points!")
else: # Will print a different string if the input is different from the if statement.
        print ("Congrats! You just won 10 points!")


Alien_Color = 'Bright_Pink' # Re-assigns the string to the the variable.

if Alien_Color == 'Dark_Green':
        print ("Wow! You shot the Dark Green Alien! You won 5 points!")
else: # Will print a different string if the input is different from the if statement.
        print ("You just shot the Bright Pink Alien, you just won 10 points!")


if Alien_Color == 'Dark_Green':
        print ("Wow! You shot the Dark Green Alien! You won 5 points!")        
elif Alien_Color == 'Orange': # Will print a different string if the input is different from the if statement. 
        print ("You just shot the Bright Pink Alien, you just won 10 points!")
else: # Will print a different string if the input is different from the elif or if statement.
        print ("You just shot the Orange Alien! Congrats on 15 points!")