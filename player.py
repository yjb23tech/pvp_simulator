import random

class Player():

    def __init__(self, player_name, player_location, player_age, player_special_atk):
        
        self.player_name = player_name
        self.player_location = player_location
        self.player_age = player_age
        self.player_special_atk = player_special_atk

        self.player_hp = 100
        self.player_atk_pwr = 1
        self.player_def_pwr = 1 
        self.player_special_atk_pwr = 1
    
    def __str__(self):
        player_details = (f"\nName: {self.player_name}\nLocation: {self.player_location}\nSpecial Atk: {self.player_special_atk}\n")
        return player_details
    
    def player_hp_status(self):
        player_hp = self.player_hp
        return player_hp 
    
    def player_launch_atk(self):
        self.player_atk_pwr = random.randint(1,20)
        return self.player_atk_pwr

    def player_launch_def(self):
        self.player_def_pwr = random.randint(1,20)
        return self.player_def_pwr
    
def set_player_name():
    ui_player_name = input(f"\nWhat is your name Warrior?\n")
    return ui_player_name

def set_player_location():
    ui_player_location = input(f"\nWhere are you from Warrior?\n")
    return ui_player_location 

def set_player_age():
    ui_player_age = int(input(f"\nHow old are you Warrior?\n"))
    return ui_player_age

def set_player_special_atk():
    ui_player_special_atk = input("\nWhat is the name of your special attack Warrior?\n")
    return ui_player_special_atk





    

