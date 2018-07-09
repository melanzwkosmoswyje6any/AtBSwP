#! python3
# bulletPointAdder.py program adding a Wikipedia bulletpoint to the start
# of each line of text on the clipboard.

import pyperclip
# Copy clipboard to variable text
text = pyperclip.paste()

# Separate lines
lines = text.split('\n')

# Each separate string in lines table gets a star at the beginning
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # Adding star at the beginning

# Creating single string from lines table
text = '\n'.join(lines)

# Copy text to clipboard
pyperclip.copy(text)