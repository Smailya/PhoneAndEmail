# This code will help you find phone numbers and email addresses on the clipboard.

import pyperclip  # Import the pyperclip module for clipboard operations
import re  # Import the re module for regular expressions

# Phone regex pattern you should adjust this regex based on your country
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?         # Group 1: Area code (optional), can be 3 digits or (3 digits)
    (\s|-|\.)?                 # Group 2: Separator (optional), can be space, hyphen, or dot
    (\d{3})                    # Group 3: First 3 digits of the phone number
    (\s|-|\.)                  # Group 4: Separator (required), can be space, hyphen, or dot
    (\d{4})                    # Group 5: Last 4 digits of the phone number
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # Group 6: Extension (optional), can be prefixed by ext, x, or ext. followed by 2 to 5 digits
)''', re.VERBOSE)  # Use re.VERBOSE for better readability

# Creating email regex pattern
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+         # Group 1: Username, must contain at least one character from the set
    @                          # Literal '@' character
    [a-zA-Z0-9._]+            # Group 2: Domain name, can contain letters, digits, dots, and underscores
    (\.[a-zA-Z]{2,4})         # Group 3: Top-level domain (TLD), must start with a dot followed by 2 to 4 letters
)''', re.VERBOSE)  # Use re.VERBOSE for better readability

# Finding matches based on clipboard text
text = str(pyperclip.paste())  # Get the text from the clipboard and convert it to a string
matches = []  # Initialize an empty list to store matches

# Find all phone number matches
for groups in phoneRegex.findall(text):
    # Construct the phone number from the matched groups
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # Join area code, first 3 digits, and last 4 digits with '-'
    
    # Check if there is an extension and append it if present
    if groups[6] != '':  # Check Group 6 for the extension
        phoneNum += ' x' + groups[6]  # Append ' x' followed by the extension number
    matches.append(phoneNum)  # Add the constructed phone number to the matches list

# Find all email matches
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # Add the full email address (Group 1) to the matches list

# Copying results to the clipboard
if len(matches) > 0:  # Check if there are any matches found
    pyperclip.copy('\n'.join(matches))  # Copy the matched phone numbers and emails to the clipboard
    print('Copied to clipboard:')  # Print a message indicating the results were copied
    print('\n'.join(matches))  # Print the matched phone numbers and emails
else:
    print('No phone numbers or email addresses found.')  # Print a message if no matches were found