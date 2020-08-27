# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:24:21 2020

@author: George Chatzis
"""

# spam=int(input('plase give a number'))
# if spam==1:
#     print('hello')
# elif spam==2:
#     print('Howdy')
# else:
#     print('greatings')

# for i in range(1,11):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1

# import random
# secret_number=random.randint(1, 20)
# print("i\'m thinking a number bewtween 1 and 20")
# for guesstaken in range(1,7):
#     guess=int(input('take a guess:'))
    
#     if guess<secret_number:
#         print('your guess is too low')
#     elif guess>secret_number:
#         print('your guess is too high')
#     else:
#         break
# if guess==secret_number:
#     print('good job!you guessed my number in' + str(guesstaken)+'guesses')
# else:
#     print('Nope,the number i was thinking was'+ str(secret_number))    

def collatz(number):
      if number%2==0:
            value=number/2
            return value
      elif number%2==1:
            value=3*number+1
            return value
      else:
            print('give a valid number')
      

        
try:
    number_given=int(input('Please give a number:>>'))
except ValueError:
    print('give a valid number')
while number_given!=1:
    number_given=collatz(number_given)   
    print(int(number_given))
    
         
        

   
    
    
    

