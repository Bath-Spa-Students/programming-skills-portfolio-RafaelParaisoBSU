# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.

Budget = 50 # Stores a value into a variable.
Price = 6
Total = (Budget // Price) # Stores a division formula into a variable.
Change = (Budget % Total) # Stores a modulus formula into a variable.

print (f"She can buy a total of {Total} USB sticks and still have {Change}$ as change.")
# Uses an f string to format the variables into one string and prints it in one statement.