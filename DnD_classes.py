import random
from parent_character_class import Character
from variables_page import stat_mod_dict
import ast



# Child classes of the main Character class. Each child (except Commoner) is used to store data specific to that class.
class Artificer(Character):
    def __init__(self, char_id):
        self.__char_class__= "Artificer"
        super().__init__(char_id)
        
    def key_stat_index(self):
        return 3
    
    def hp_stat_index(self):
        return 8


class Barbarian(Character):
    def __init__(self, char_id):
        self.__char_class__= "Barbarian"
        super().__init__(char_id)
        print(self.armor_list)

    def key_stat_index(self):
        return 0
    
    def hp_stat_index(self):
        return 12
    
    def calculate_ac(self):
        if self.__shield__ == "None":
            self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]] + stat_mod_dict[self.__char_stats_dict__["CON"]]
        else:
            self.__ac__ = 12 + stat_mod_dict[self.__char_stats_dict__["DEX"]] + stat_mod_dict[self.__char_stats_dict__["CON"]]


class Bard(Character):
    def __init__(self, char_id):
        self.__char_class__= "Bard"
        super().__init__(char_id)

    def key_stat_index(self):
        return 5
    
    def hp_stat_index(self):
        return 8


class Cleric(Character):
    def __init__(self, char_id):
        self.__char_class__= "Cleric"
        super().__init__(char_id)

    def key_stat_index(self):
        return 4
    
    def hp_stat_index(self):
        return 8


# Commoner is the only different child class and sets the character level to 0, uses its own stat roll function (which limits its range), and roll hp function ().
class Commoner(Character):
    def __init__(self, char_id):
        self.__char_class__= "Commoner"
        super().__init__(char_id)

    def key_stat_index(self):
        return 2
    
    def random_char_level(self):
        self.__char_level__ = 0
    
    def stats_roll(self):
        self.rolls_for_stats = [0, 0, 0, 0, 0, 0]
        while self.rolls_for_stats[self.key_stat_index()] == 0 or self.rolls_for_stats[self.key_stat_index()] < max(self.rolls_for_stats):
            numbers_rolled = []
            for i in range(6):
                stat_roll = random.choices([6, 7, 8, 9, 10, 11, 12, 13, 14], weights = [1, 2, 3, 4, 5, 4, 3, 2, 1], k=1)[0]
                numbers_rolled.append(stat_roll)
            self.rolls_for_stats = numbers_rolled

    def roll_hp(self):
        self.__hp__ = 4 + stat_mod_dict[self.__char_stats_dict__["CON"]]

    def calculate_ac(self):
        self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]]


class Druid(Character):
    def __init__(self, char_id):
        self.__char_class__= "Druid"
        super().__init__(char_id)

    def key_stat_index(self):
        return 4
    
    def hp_stat_index(self):
        return 8


class Fighter(Character):
    def __init__(self, char_id):
        self.__char_class__= "Fighter"
        super().__init__(char_id)

    def key_stat_index(self):
        return random.randint(0, 1)
    
    def hp_stat_index(self):
        return 10
    
    def roll_weapon(self):
        while True:
            self.__weapon__ = random.choice(self.weapon_list)
            if self.__char_stats_dict__["DEX"] > self.__char_stats_dict__["STR"] and ast.literal_eval(self.__weapon__[4]):
                break
            elif self.__char_stats_dict__["DEX"] <= self.__char_stats_dict__["STR"]:
                break


class Monk(Character):
    def __init__(self, char_id):
        self.__char_class__= "Monk"
        super().__init__(char_id)

    def key_stat_index(self):
        return random.choice([1, 4])
    
    def hp_stat_index(self):
        return 8
    
    def roll_weapon(self):
        while True:
            self.__weapon__ = random.choice(self.weapon_list)
            if "Finesse" in ast.literal_eval(self.__weapon__[4]):
                break

    def calculate_ac(self):
        self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]] + stat_mod_dict[self.__char_stats_dict__["WIS"]]


class Paladin(Character):
    def __init__(self, char_id):
        self.__char_class__= "Paladin"
        super().__init__(char_id)

    def key_stat_index(self):
        return 5
    
    def hp_stat_index(self):
        return 10


class Ranger(Character):
    def __init__(self, char_id):
        self.__char_class__= "Ranger"
        super().__init__(char_id)

    def key_stat_index(self):
        return 1
    
    def hp_stat_index(self):
        return 10


class Rogue(Character):
    def __init__(self, char_id):
        self.__char_class__= "Rogue"
        super().__init__(char_id)

    def key_stat_index(self):
        return 1
    
    def hp_stat_index(self):
        return 8
    
    def roll_weapon(self):
        while True:
            self.__weapon__ = random.choice(self.weapon_list)
            if "Finesse" in ast.literal_eval(self.__weapon__[4]):
                break


class Sorcerer(Character):
    def __init__(self, char_id):
        self.__char_class__= "Sorcerer"
        super().__init__(char_id)        

    def key_stat_index(self):
        return 5
    
    def hp_stat_index(self):
        return 6


class Warlock(Character):
    def __init__(self, char_id):
        self.__char_class__= "Warlock"
        super().__init__(char_id)

    def key_stat_index(self):
        return 5
    
    def hp_stat_index(self):
        return 8


class Wizard(Character):
    def __init__(self, char_id):
        self.__char_class__= "Wizard"
        super().__init__(char_id)

    def key_stat_index(self):
        return 3
    
    def hp_stat_index(self):
        return 6