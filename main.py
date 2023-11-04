import function

range_low = 1
range_high = 1000

def start():
    choice = function.menu()
    if choice == 1:
        list_players = function.players()
        print (list_players)