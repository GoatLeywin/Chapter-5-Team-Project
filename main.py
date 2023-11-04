import function

range_low = 1
range_high = 1000
win = 0
turns = 0

def start():
    range_low = 1
    range_high = 1000
    win = 0
    turns = 0
    
    choice = function.menu()
    if choice == 1:
        player_list = function.players()
        print (player_list)
        random_number = function.get_random_number(range_low, range_high)
        print (random_number)
        
        while win == 0:
            for number in range(len(player_list)):
                print (player_list[number], ' what is your guess? ', sep = '', end = '')
                guessed_number = input('')
                win = function.check_win(random_number, guessed_number, turns)