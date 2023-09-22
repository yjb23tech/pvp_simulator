#All of my key functions 

def pvp(player_x, player_y, round_counter):
    
    print(f"Round {round_counter + 1}: FIGHT!")

    #Launch atk sequence for the attacking player; launch def sequence for the defending player
    #Only call funcs once to trigger return of rand generated pwr property; will work with these values 
    #For duration of the single fight cycle
    print(f"{player_x.player_name} launches an attack with {player_x.player_launch_atk()} battle points!")
    print(f"{player_y.player_name} launches a defensive block with {player_y.player_launch_def()} battle points!")
    #Post func call above, the atk and def should be set and persist for duration of fight cycle

    if (player_x.player_atk_pwr > player_y.player_def_pwr):
        print(f"{player_x.player_name}'s attack has broken through {player_y.player_name}'s defenses!")
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

