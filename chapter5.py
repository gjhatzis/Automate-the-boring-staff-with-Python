# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:08:03 2020

@author: George Chatzis
"""

# Dictionaries

# Statements:
    # in , not in check if the key or value is in the dic, retursn True or False
# Methods:
    
    # keys() it returns the keys of a dictionary
    # values() it returns the values of a dic
    # items() it returns both keys and values of a dic
    # get()  it takes two arguments: a key and a value: if the key exists returns
        # its value, if not returns the second argument as value
    # setdefault() it takes two arguments , the first one is the key to check for
        # and if it doesnt exists it passes the second argument as value ..nice
        # to check if a key exists
    # pprint module: pprint(), pformat() they pretty print a dic
    
# spam = {'color': 'red', 'age': 42}
# for k,v in spam.items():
#     print('key:'+k+", value:"+str(v))
# 'color' in spam.keys()

# import pprint
# message = 'It was a bright cold day in April, and the \
# clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(pprint.pformat(count))

# theBoard = {
# 'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
# 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
# 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
#     print('-+-+-')
#     print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
#     print('-+-+-')
#     print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#             turn = 'X'
    
# printBoard(theBoard)

# allGuests = {'Alice': {'apples': 5, 'pretzels':12},
# 'Bob': {'ham sandwiches': 3, 'apples':2},
# 'Carol': {'cups': 3, 'apple pies': 1}}
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))

# Practice Projects

# inventory= {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','ruby','ruby']   

# def addToInventory(myinventory, addedItems):
    
#     for char in addedItems:
#         if char in myinventory.keys():
#             myinventory[char]=myinventory[char]+1
#         else:
#             myinventory.setdefault(char,1)
#     return myinventory

  
# def DisplayInventory(myinventory):
#     print('Inventory:')
#     total=0
#     for k,v in myinventory.items():
#         print(str(v)+' '+k)
#         total=total + v
#     print('Total number of items is:'+ str(total))
    
    
# inv=addToInventory(inventory,dragonLoot)   
# DisplayInventory(inv)  





         