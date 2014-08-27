
#==========To run, click the link below================#

########################################################
#http://www.codeskulptor.org/#user29_gahmhlJRV57Hnja.py#
########################################################


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
num_range=100
guess_num=-1
s_number=-1
attempts_left=-1
range_=1

# helper function to start and restart the game
def new_game():
    # remove this when you add your code 
    global s_number
    s_number= random.randrange(0,num_range)
    # define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    global attempts_left,range_
    range_=1
    num_range=100
    attempts_left=7 
    new_game()
    print "New Game. Range is [0,100) "
    print "Number of remaining guesses is ",attempts_left
    print    
    # remove this when you add your code    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range,attempts_left,range_
    num_range=1000
    range_=2
    attempts_left=10
    new_game()
    print "New Game. Range is [0,1000) "
    print "Number of remaining guesses is ",attempts_left
    print       
    # remove this when you add your code    
       
def input_guess(guess):
    # main game logic goes here	
    global attempts_left,s_number
    global range_
    guess_num= int(guess)
    attempts_left=attempts_left-1
    print "Guess was ", guess
    
    if((attempts_left==0)and(not(guess_num==s_number))):
        print 'Computer Wins!'
        print 'Secret Number was',s_number
        print
        if(range_==1):
            range100()
        else: range1000()
        
        
    print "Number of remaining guesses ", attempts_left
    if(guess_num>s_number):
        print "Higher!"
        print
    elif(guess_num<s_number):
        print "Lower!"
        print
    else :
        print "Correct!"
        print
        if(range_==1):
            range100()
        else: range1000()     
    # remove this when you add your code
    
# create frame
frame= simplegui.create_frame("Guess The Number",200,200)

# register event handlers for control elements
frame.add_button("Range is [0,100) ",range100,200)
frame.add_button("Range is [0,1000) ",range1000,200)
frame.add_input("Enter the guess ",input_guess,200)

# call new_game and start frame
range100()
frame.start()
# always remember to check your completed program against the grading rubric
