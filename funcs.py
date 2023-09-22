#All of my key functions 

def pvp(player_x, player_y, round_counter):
    
    print(f"Round {round_counter}: FIGHT!")

    if (player_x.player_atk_pwr > player_y.player_def_pwr):
        print(f"{player_x.player_name} wins through attacking power!")
    elif (player_x.player_atk_pwr < player_y.player_def_pwr):
        print(f"{player_y.player_name} wins through defensive power!")
    else:
        print("It's a tie!")

