import function

range_low = 1
range_high = 1000
win = 0
turns = 0

def start():
    global range_low
    global range_high
    global turns
    win = 0
    
    choice = function.menu()
    
    is_integer_choice = function.check_integer(choice)
    while is_integer_choice == 0:
        print ('invalid input must be integer')
        choice = function.menu()
        is_integer_choice = function.check_integer(choice)
    choice = int(choice)
    
    if choice == 1:
        player_list = function.players()
        change_range = input('Do you wish to change the range of numbers? (default 1-1000 answer "y" to change or "n" to not) ')
        
        if change_range == 'y':
            range_list = function.choose_range()
            range_low = range_list[0]
            range_high = range_list[1]
            
        if change_range == 'n':
            range_low = range_low
            range_high = range_high
        
        if change_range != 'n' and change_range != 'y':
            print ('invalid choice please redo')
            start()
            
        random_number = int(function.get_random_number(range_low, range_high))
        
        while win == 0:
            turns = function.amount_of_turns(turns)
            for number in range(len(player_list)):
                print (player_list[number], ' what is your guess? ', sep = '', end = '')
                guessed_number = input('')
                
                is_integer_guess = function.check_integer(guessed_number)
                while is_integer_guess == 0:
                    print ('invalid input must be integer')
                    print (player_list[number], ' what is your guess? ', sep = '', end = '')
                    guessed_number = input('')
                    is_integer_guess = function.check_integer(guessed_number)
                guessed_number = int(guessed_number)
                
                if guessed_number < range_low:
                    print ('that guess is out of range guess again')
                    print (player_list[number], ' what is your guess? ', sep = '', end = '')
                    guessed_number = int(input(''))
                    
                if guessed_number > range_high:
                    print ('that guess is out of range guess again')
                    print (player_list[number], ' what is your guess? ', sep = '', end = '')
                    guessed_number = int(input(''))
                    
                win = function.check_win(random_number, guessed_number, turns)
                function.get_feedback(random_number, guessed_number)
                if win == 1:
                    start()
                    break
        
    if choice == 2:
        range_list = function.choose_range()
        range_low = range_list[0]
        range_high = range_list[1]
        start()
    
    if choice == 3:
        print ('Thanks for playing our number guessing game')
        
    if choice > 3 or choice < 1:
        print ('invalid choice please redo')
        start()
        
start()