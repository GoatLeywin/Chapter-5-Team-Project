import random
from random import randint

def menu():
    #display menu accepts no arguments
    #it outputs the menu choices and takes input from the user
    # for the menu item and returns the choice
    print('\t\tMENU')
    print('1) Start new game')
    print('2) Choose range')
    print('3) Exit game')
    
    choice = int(input('Enter a selection: '))
    return choice

def get_range(range_low, range_high):
    #accepts range for the bottom and top number when the user decides the range
    #will generate random number within range and return that number
    random_number = randint(range_low, range_high)
    
    return random_number

def get_feedback(random_number, guessed_number):
    if random_number > guessed_number:
      print ("try guessing a bigger number")
    if random_number < guessed_number:
      print ("try guessing a smaller number")
  
def players():
    #accepts no arguments
    #prompts user for players first name and last name
    #returns all variables
    
    #starting variable
    player1f = input("Enter your first name: ")
    player1l = input("Enter your last name: ")
    player2f = input("Enter your first name: ")
    player2l = input("Enter your last name: ")
    
    player1_name = player1f, player1l
    
    player2_name = player2f, player2l
    
    return player1_name, player2_name

def check_win(random_number, guessed_number, turns):
    if random_number == guessed_number:
        print ("CONGRATULATIONS! You won the game the number you were looking for was", random_number)
        print ("it took", turns, "to win")