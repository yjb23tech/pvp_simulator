class Player():

    def __init__(self, player_name, player_location, player_age, player_special_atk):
        
        self.player_name = player_name
        self.player_location = player_location
        self.player_age = player_age
        self.player_special_atk = player_special_atk

        self.player_atk_pwr = 1
        self.player_def_pwr = 1 
        self.player_special_atk_pwr = 1
    
    def __str__(self):
        player_details = (f"\nName: {self.player_name}\nLocation: {self.player_location}\nSpecial Atk: {self.player_special_atk}\n")
        return player_details
    
    

