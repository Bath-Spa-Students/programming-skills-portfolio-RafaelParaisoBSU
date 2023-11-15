# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, design): #creates a function
    print (f"My shirt size is {size}.")
    print (f"The '{design}' will be printed on the shirt!\n")

make_shirt ('large', 'You Only Live Once') #calls the function and changing its given values
make_shirt (size = "medium", design = 'God is Good All the Time.') #calls the function and changing its given values

