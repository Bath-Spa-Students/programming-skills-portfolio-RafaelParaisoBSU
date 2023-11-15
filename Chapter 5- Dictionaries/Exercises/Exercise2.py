#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

Code_glossary = {
    'String': 'A "string" of characters.',
    'Variable': 'A container for storing data  values.',
    'Comments': 'A comment either to explain the code or make it readable.',
    'Dictionary': "Pairs of keys and values in a group or collection.",
    'Bug': 'An error or mistake that is in the code.',
    }

#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

for word, value in Code_glossary.items(): # Uses a for-loop to print all the items in the dictionary.
    print (f"{word}  -  {value}\n") # Uses an f-string to format the keys and values in one string.
