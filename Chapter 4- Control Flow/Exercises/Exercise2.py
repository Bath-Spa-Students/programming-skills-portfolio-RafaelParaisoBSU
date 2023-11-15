# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

#•Write one version of this program that runs the if block and another that runs the else block.

Alien_Color = 'Dark_Green' # Stores a string in a variable.

if Alien_Color == 'Dark_Green': # If statement that prints if the variable is "Dark Green"
        print ("Wow! You just won 5 points!")
else: # Will print a different string if the input is different from the if statement.
        print ("Congrats! You just won 10 points!")

Alien_Color = 'Bright_Pink' # Re-assigns the string to the the variable.

if Alien_Color == 'Dark_Green':
        print ("Wow! You just won 5 points!")
else:
        print ("You just shot the Bright Pink Alien, you just won 10 points!")
