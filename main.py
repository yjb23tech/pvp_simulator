import player
import funcs

def play():

    #Create Player 1
    player_1 = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age(), player.set_player_special_atk())
    print(player_1)

    #Create Player 2 
    player_2 = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age(), player.set_player_special_atk())
    print(player_2)

    #Tracks the number of rounds played 
    fight_counter = 0 

    #Determines who is on attack, who is on defence 
    bool_player_1_starts = True

    while ((player_1.player_hp_status() > 0) and (player_2.player_hp_status() > 0)):

        #The Player fed into funcs.pvp 1st is on attack; the Player fed in 2nd is on defence
        if (bool_player_1_starts == True):
            #When the bool is True, Player 1 is fed in 1st and Player 2 in 2nd
            funcs.pvp(player_1, player_2, fight_counter)
        else:
            #When the bool is False, Player 2 is passed in 1st and Player 1 in 2nd
            funcs.pvp(player_2, player_1, fight_counter)

        #Once the pvp func is run, the order of the Players needs to swap to allow a new Player on atk and def
        #Functions as a switch; swaps the order of Players so each Player has the chance to go first 
        if (bool_player_1_starts == True):
            #Player 1 started; order is swapped by changing boolean value; now Player 2 will start
            bool_player_1_starts = False
        else:
            #Player 2 started; order is swapped by changing boolean value; now Player 1 will start 
            bool_player_1_starts = True 
    
        fight_counter += 1

play()

