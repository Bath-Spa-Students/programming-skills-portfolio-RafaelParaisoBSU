# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = 'large', design = 'I love Python!'): # Creates a function.
    print (f"My shirt size is {size}.") # Prints a statement using an f-string to insert a variable in the string.
    print (f"The '{design}' will be printed on the shirt!\n")

make_shirt () # Calls for the function and changes its original values.
make_shirt ('medium', 'You Only Live Once') # Calls for the function and changes its corresponding values.
make_shirt (size = "small", design = 'God is Good All the Time.') # Calls the function and changes its  values.