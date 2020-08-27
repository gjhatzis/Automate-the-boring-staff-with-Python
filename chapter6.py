# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:58:08 2020

@author: George Chatzis
"""


# MANIPULATING STRINGS

    # Escape characters
    
        # \' Single quote
        # \" Double quote
        # \t Tab
        # \n Newline (line break)
        # \\ Backslash
    
    # Raw strings
        
        # r : completly ignores all escape characters
        
    # Triple quotes
    
        #     While you can use the \n escape character to put a newline
        # into a string, it is often easier to use multiline strings. A
        # multiline string in Python begins and ends with either three
        # single quotes or three double quotes.
        
    # Multiple comments
        # """dsdlal"""
        
        # METHODS
            # upper() converts in capital letters
            # lower() converts in lower case
                
            # isupper() returns True if has one upper case letter
            # islower() returns True if has one lower case letter
            
            # isalpha() returns True if the string consists only of letters and is not blank.
            # isalnum() returns True if the string consists only of letters and numbers and is not blank.
            # isdecimal() returns True if the string consists only of numeric characters and is not blank.
            # isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
            # istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
                        
                        # FOR VALIDATING USER INPUT
                
            #startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively)
            #with the string passed to the method; otherwise, they return False.
            
            # join() method is useful when you have a list of strings that need to be joined together into a single string value.
            # 
            # rjust() and ljust() string methods return a padded
                # version of the string they are called on, with spaces inserted to
                # justify the text. The first argument to both methods is an integer
                # length for the justified string.
                
            # center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right.
            
            # strip() string method will return a new string without any whitespace characters at the beginning or end.
            # lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively.
            # pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard
            
            
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups':4, 'cookies': 8000}

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    
    
# # printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# import pyperclip
# pyperclip.copy('Hello world')
# pyperclip.paste()

# def PrintTable(my_list):
    

tabledata = [['apples', 'oranges', 'cherries','banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

colwidths = [0] * len(tabledata)

for i in tabledata[:1]:
    maxnumber=











