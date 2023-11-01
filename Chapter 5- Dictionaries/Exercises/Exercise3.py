# Now that you know how to loop through a dictionary, clean up the code from Exercise 5-2 by replacing your series of print()calls with a loop that runs through the dictionary’s keys and values. 

Code_glossary = {
    'String': 'A "string" of characters.',
    'Variable': 'A container for storing data values.',
    'Comments': 'A comment either to explain the code or make it readable.',
    'Dictionary': "Pairs of keys and values in a group or collection.",
    'Bug': 'An error or mistake that is in the code.',
    'Integer': 'A value that can be stored in a variable.',
    'Float': 'A data type that is composed of a positive or negative number.',
    'Operators': 'A symbol that is used to perform operations like addition, subtraction, etc.',
    'Lists': "A list that can be ordered, changed, or collected.",
    'Tuple': 'An list that can ordered or collected but not changed.',
    }

for word, definition in Code_glossary.items():
    print("\n" + word.title() + ": " + definition) 