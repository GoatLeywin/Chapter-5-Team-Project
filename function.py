import random
from random import randint
from multiprocessing.sharedctypes import Value

def check_integer(prompt):
    integer = 2
    flag = True
    
    try:
        # try converting to integer
        int(prompt)
    except ValueError:
        flag = False
    # flag check
    if flag:
        integer = 1
    else:
        integer = 0
    
    return integer

def menu():
    #display menu accepts no arguments
    #it outputs the menu choices and takes input from the user
    # for the menu item and returns the choice
    print('MENU')
    print('1) Start new game')
    print('2) Choose range')
    print('3) Exit game')
    
    choice = input('Enter a selection: ')
    return choice

def get_random_number(range_low, range_high):
    #accepts range for the bottom and top number when the user decides the range
    #will generate random number within range and return that number
    random_number = randint(range_low, range_high)
    
    return random_number

def get_feedback(random_number, guessed_number):
    if random_number > guessed_number:
      print ("Try guessing a bigger number")
    if random_number < guessed_number:
      print ("Try guessing a smaller number")
      
  
def players():
    #accepts no arguments
    #prompts user for number of players
    #prompts user for players names
    #returns all variables
    
    #makes player list
    player_list = []
    
    amount_of_players = input("How many players are there? ")
    
    is_integer_choice = check_integer(amount_of_players)
    while is_integer_choice == 0:
        print ('invalid input must be integer')
        amount_of_players = input("How many players are there? ")
        is_integer_choice = check_integer(amount_of_players)
    amount_of_players = int(amount_of_players)
    
    for number in range(1, amount_of_players + 1):
        print ("What is player ", number, "'s name? ", sep = '', end = '')
        player = input('')
        player_list.append(player)
    
    return player_list

def check_win(random_number, guessed_number, turns):
    #makes a variable to see if anyone has won or not 0 = no win and 1 = win
    
    if random_number == guessed_number:
        print ("CONGRATULATIONS! You won the game the number you were looking for was", random_number)
        print ("it took", turns, "turn(s) to win")
        print('')
        win = 1
        
    else:
        win = 0
        
    return win

def choose_range():
    
    range_list = []
    
    range_low = input('Choose the lowest number the random number can be: ')
    
    is_integer_choice = check_integer(range_low)
    while is_integer_choice == 0:
        print ('invalid input must be integer')
        range_low = input('Choose the lowest number the random number can be: ')
        is_integer_choice = check_integer(range_low)
    range_low = int(range_low)
        
    range_high = input('Choose the highest number the random number can be: ')
    
    is_integer_choice = check_integer(range_high)
    while is_integer_choice == 0:
        print ('invalid input must be integer')
        range_high = input('Choose the highest number the random number can be: ')
        is_integer_choice = check_integer(range_high)
    range_high = int(range_high)
        
    range_list.append(range_low)
    range_list.append(range_high)
    
    return range_list

def amount_of_turns(turns):
        
    turns = turns + 1
    return turns
