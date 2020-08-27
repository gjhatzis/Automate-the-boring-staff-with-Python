# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:15:03 2020

@author: George Chatzis
"""

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
# # print('415-555-4242 is a phone number:')
# # print(isPhoneNumber('415-555-4242'))
# # print('Moshi moshi is a phone number:')
# # print(isPhoneNumber('Moshi moshi'))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#         print('Done')

# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())


# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the
# preceding group.
# {n,m}? or *? or +? performs a nongreedy match of the
# preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character,
# respectively.
# \D, \W, and \S match anything except a digit, word, or
# space character, respectively.
# [abc] matches any character between the brackets (such
# as a, b, or c).
# [^abc] matches any character that isn’t between the
# brackets.





