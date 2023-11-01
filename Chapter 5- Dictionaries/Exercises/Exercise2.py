#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

Code_glossary = {
    'String': 'A "string" of characters.',
    'Variable': 'A container for storing data  values.',
    'Comments': 'A comment either to explain the code or make it readable.',
    'Dictionary': "Pairs of keys and values in a group or collection.",
    'Bug': 'An error or mistake that is in the code.',
    }

#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

word = 'String'
print("\n" + word.title() + ": " + Code_glossary[word])

word = 'Variable'
print("\n" + word.title() + ": " + Code_glossary[word])

word = 'Comments'
print("\n" + word.title() + ": " + Code_glossary[word])

word = 'Dictionary'
print("\n" + word.title() + ": " + Code_glossary[word])

word = 'Bug'
print("\n" + word.title() + ": " + Code_glossary[word])