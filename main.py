import player

test_player = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age(), player.set_player_special_atk())
print(test_player)

fight_counter = 0 

while (fight_counter < 5):

    print(f"Attack Power via func call: {test_player.player_launch_atk()}")
    print(f"Defense Power via func call: {test_player.player_launch_def()}")
    print(f"HP Status: {test_player.player_hp}")

    print(f"Attack Power via GETish: {test_player.player_atk_pwr}")
    print(f"Defense Power via GETish: {test_player.player_def_pwr}")

    print(" ")
    fight_counter += 1


