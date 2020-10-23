'''
This is a simple program that generates a random number 
between 0 and 100 and asks the user to guess the number
'''

import random

# Function to generate the number
def numberGen():
    rnd_number = int(random.randrange(0, 100))
    return(rnd_number)

# Function to ask user to input number
def userGuess():
    # ask user for number and check that it's between 0-100
    while True:
        guess = int(input("Guess a number between 0 and 100: "))
        if 0 <= guess <= 100:
            break
        else:
            print("Try again")
    return(guess)

# Function to compare RNG to input number
def guessCheck(x, y):

    while x != y:
        if x < y:
            y = int(input("Too high, try again: "))
        elif y < x:
            y = int(input("Too low, try again: "))        
        else:
            break
    print("Great job!")

    return
  
# Use the fuctions to run the program
number = numberGen()
guess = userGuess()
guessCheck(number, guess)
