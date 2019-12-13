import time
import os
import random
import sys
import pyautogui
import numpy

print('---------------------------------------')
print('This is rock paper scissors the game.')
print('---------------------------------------')
time.sleep(2)
 
print('Choices include:')
time.sleep(1)
print('Rock - type "rock".')
time.sleep(1)
print('Paper - type "paper".')
time.sleep(1)
print('Scissors - type "scissors".')
time.sleep(1)

a = random.randint(-1, 1)

x = input('Please enter your choice:')  
if(x == 'rock', 'paper', 'scissors'):
  print('You selected:', x)
else:
  quit()

print('')
time.sleep(2)
print('Three...')
time.sleep(1)
print('Two...')
time.sleep(1)
print('One...')
time.sleep(2)

print('')

# -1 = rock
#  0 = paper
# +1 = scissors

if(a == -1):
    print('---------------------------')
    print('I randomly picked Rock!')
    print('---------------------------')
    #a1 = 'rock'
    time.sleep(2)
if(a == -1 and x == 'rock'):
    print('')
    print('--------')
    print('| Tie! |')
    print('--------')
      
if(a == 0):
    print('---------------------------')
    print('I randomly picked Paper!')
    print('---------------------------')
    #a2 = 'paper'
    time.sleep(2)
if(a == 0 and x == 'paper'):
    print('')
    print('--------')
    print('| Tie! |')
    print('--------')
      
if(a == 1):
    print('---------------------------')
    print('I randomly picked Scissors!')
    print('---------------------------')
    #a3 = 'scissors'
    time.sleep(2)
if(a == 1 and x == 'scissors'):
    print('')
    print('--------')
    print('| Tie! |')
    print('--------')
        
         

if(a == -1 and x == 'paper'):
    print('------------------------------')
    print('I won! Rock beats paper!')
    print('------------------------------')
    time.sleep(2)

if(a == 1 and x == 'paper'):
    print('------------------------------')
    print('I won! Scissors beats paper!')
    print('------------------------------')
    time.sleep(2)

if(a == -1 and x == 'scissors'):
    print('------------------------------')
    print('I won! Rock beats scissors!')
    print('------------------------------')
    time.sleep(2)

if(a == 0 and x == 'scissors'):
    print('------------------------------')
    print('You won. Scissors beats paper.')
    print('------------------------------')
    time.sleep(2)

if(a == 0 and x == 'rock'):
    print('------------------------------')
    print('I won! Paper beats rock.')
    print('------------------------------')
    time.sleep(2)

if(a == 1 and x == 'rock'):
    print('------------------------------')
    print('You won.  Rock beats scissors.')
    print('------------------------------')
    time.sleep(2)

print('')
print('')
print('----------------------------')
print('Would you like to try again?')
print('----------------------------')
z = input('')
time.sleep(1)
os.system('python RPS.py')

if(z == 'no', 'end', 'quit', 'stop'):
    quit()
