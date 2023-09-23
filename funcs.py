#All of my key functions 

def pvp(player_x, player_y, round_counter):
    
    print(f"Round {round_counter + 1}: FIGHT!\n")

    #Launch atk sequence for the attacking player; launch def sequence for the defending player
    #Only call funcs once to trigger return of rand generated pwr property; will work with these values 
    #For duration of the single fight cycle
    print(f"{player_x.player_name} attacks with {player_x.player_launch_atk()} battle points!")
    print(f"{player_y.player_name} defends with {player_y.player_launch_def()} battle points!")
    #Post func call above, the atk and def should be set and persist for duration of fight cycle

    #Comparison of attacking power vs defending power has 3 outcomes: atk wins; def wins; tie
    if (player_x.player_atk_pwr > player_y.player_def_pwr):
        print(f"{player_x.player_name}'s attack has broken through {player_y.player_name}'s defenses!")
        resulting_atk_damage = player_x.player_atk_pwr - player_y.player_def_pwr
        print(f"{player_y.player_name} takes a devastating blow, losing -{resulting_atk_damage} hp!")
        player_y.player_hp = player_y.player_hp - resulting_atk_damage
    
        #Appears successful; I'm going to take the objects passed into this func and pass them to another func
        both_players_hp_status(player_x, player_y)
    elif (player_x.player_atk_pwr < player_y.player_def_pwr):
        print(f"{player_y.player_name} parries successfully and launches a counterattack on {player_x.player_name}!")
        resulting_def_damage = player_y.player_def_pwr - player_x.player_atk_pwr 
        print(f"{player_x.player_name} takes a devastating blow, losing -{resulting_def_damage} hp!")
        player_x.player_hp = player_x.player_hp - resulting_def_damage

        #Appears successful; I'm going to take the objects passed into this func and pass them to another func
        both_players_hp_status(player_x, player_y)
    else:
        print("It's a tie!")

def both_players_hp_status(player_a, player_b):

    print(f"\n{player_a.player_name} remaining hp: {player_a.player_hp_status()}")
    print(f"{player_b.player_name} remaining hp: {player_b.player_hp_status()}\n")
