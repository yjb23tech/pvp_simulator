import player
import funcs

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

while (fight_counter < 5):

    if (bool_player_1_starts == True):
        funcs.pvp(player_1, player_2, fight_counter)
    else:
        funcs.pvp(player_2, player_1, fight_counter)

    #print(f"Attack Power via func call: {player_1.player_launch_atk()}")
    #print(f"Defense Power via func call: {player_1.player_launch_def()}")
    #print(f"HP Status: {player_1.player_hp}")

    #print(f"Attack Power via GETish: {player_1.player_atk_pwr}")
    #print(f"Defense Power via GETish: {player_1.player_def_pwr}")

    print(" ")

    if (bool_player_1_starts == True):
        print("Player 2 Starts!")
        bool_player_1_starts = False
    else:
        print("Player 1 Starts!")
        bool_player_1_starts = True 
    
    fight_counter += 1


