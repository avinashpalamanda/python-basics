# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

secret_number = 0
guesses = 0
count = 0
choice = 0 

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global choice
    global count
    if (choice == 1):
        count = 7
        secret_number = random.randrange(0, 100)
        print
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is ",count
    elif (choice == 2):
        count = 10
        secret_number = random.randrange(0, 1000)
        print
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is ",count
    else:
        count = 7
        secret_number = random.randrange(0, 100)
        print
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is ",count
 

#define event handlers for control panel
#For range 0 to 100
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global choice
    choice = 1
    new_game()      

#For range 0 to 1000    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global choice
    choice = 2
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses
    global count
    global choice
    global secret_number
    count = count - 1
    guesses = int(guess)
    print
    print "Guess was ",guesses
    
    if (count > 0):
        if (guesses < secret_number):
            print "Number of remaining guesses is ",count
            print "Higher!"
        elif (guesses > secret_number):
            print "Number of remaining guesses is ",count
            print "Lower!"
        elif (guesses == secret_number):
            print "Number of remaining guesses is ",count
            print "Bingo!!!!Correct!!!!"
            print "--------------------------------------------"
            print
            choice = 0
            new_game()
    else:
        print "Number of remaining guesses is ",count
        print "Bad Luck....Try Again..."
        print "--------------------------------------------"
        choice = 0
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the Number",300,300)
frame.add_button("Range is [0,100)",range100, 100)
frame.add_button("Range is [0,1000)",range1000, 100)
frame.add_input("Guess", input_guess, 100)

# register event handlers for control elements and start frame
# call new_game 
new_game()
