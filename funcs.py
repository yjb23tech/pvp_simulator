#All of my key functions 

def pvp(player_x, player_y, round_counter):
    
    print(f"Round {round_counter}: FIGHT!")

    if (player_x.player_atk_pwr > player_y.player_def_pwr):
        print(f"{player_x.player_name} has broken through {player_y.player_name}'s defenses!")
        resulting_atk_damage = player_x.player_atk_pwr - player_y.player_def_pwr
        player_y.player_hp = player_y.player_hp - resulting_atk_damage
    
        print(f"{player_x.player_name} now has {player_x.player_hp_status()} health points left")
        print(f"{player_y.player_name} now has {player_y.player_hp_status()} health points left")
    elif (player_x.player_atk_pwr < player_y.player_def_pwr):
        print(f"{player_y.player_name} parries successfully and launches a counterattack on {player_x.player_name}!")
        resulting_def_damage = player_y.player_def_pwr - player_x.player_atk_pwr 
        player_x.player_hp = player_x.player_hp - resulting_def_damage

        print(f"{player_x.player_name} now has {player_x.player_hp_status()} health points left")
        print(f"{player_y.player_name} now has {player_y.player_hp_status()} health points left")
    else:
        print("It's a tie!")

