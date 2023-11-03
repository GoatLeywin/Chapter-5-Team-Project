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

