import player

player_1 = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age(), player.set_player_special_atk())
print(player_1)

player_2 = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age(), player.set_player_special_atk())
print(player_2)

fight_counter = 0 

bool_player_1_starts = True

while (fight_counter < 5):

    if (bool_player_1_starts == True):
        print(f"{player_1.player_name} is attacking!")
        print(f"{player_2.player_name} is on the defensive\n")
    else:
        print(f"{player_2.player_name} is attacking")
        print(f"{player_1.player_name} is on the defensive!\n")

    print(f"Attack Power via func call: {player_1.player_launch_atk()}")
    print(f"Defense Power via func call: {player_1.player_launch_def()}")
    print(f"HP Status: {player_1.player_hp}")

    print(f"Attack Power via GETish: {player_1.player_atk_pwr}")
    print(f"Defense Power via GETish: {player_1.player_def_pwr}")

    print(" ")

    if (bool_player_1_starts == True):
        print("Player 2 Starts!")
        bool_player_1_starts = False
    else:
        print("Player 1 Starts!")
        bool_player_1_starts = True 
    
    fight_counter += 1


