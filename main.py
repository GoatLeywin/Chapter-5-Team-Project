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
    if choice == 1:
        player_list = function.players()
        random_number = int(function.get_random_number(range_low, range_high))
        
        while win == 0:
            turns = function.amount_of_turns(turns)
            for number in range(len(player_list)):
                print (player_list[number], ' what is your guess? ', sep = '', end = '')
                guessed_number = int(input(''))
                win = function.check_win(random_number, guessed_number, turns)
                if win == 1:
                    break
        
    if choice == 2:
        range_list = function.choose_range()
        range_low = range_list[0]
        range_high = range_list[1]
        start()
    
    if choice == 3:
        print ('Thanks for playing our number guessing game')