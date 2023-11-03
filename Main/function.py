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