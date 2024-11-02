import ast
import random
import csv
from DnD_classes import *
from race_class import *
from variables_page import max_char_level, char_level_odds, stat_mod_dict, shield_chance



class Character:
    def __init__(self, char_id):
        #Set up all variable names
        self.__char_id__ = char_id
        self.__name__ = None
        self.__gender__ = None
        self.__char_stats_dict__ = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.rolls_for_stats, self.armor_list, self.weapon_list, self.__features__ = [], [], [], []
        #Run randomizers for each character variable
        self.name_roll()
        self.random_gender()
        self.race_roll()
        self.stats_roll()
        self.stats_compile()
        self.random_char_level()
        self.roll_hp()
        self.make_equipment_list()
        self.roll_armor()
        self.roll_weapon()
        self.roll_shield()
        self.calculate_ac()



    # Block of get functions
    def get_char_id(self):
        return self.__char_id__
    
    def get_char_name(self):
        return self.__name__
    
    def get_char_gender(self):
        return self.__gender__
    
    def get_char_race(self):
        return self.race.get_name()
    
    def get_char_class(self):
        return self.__char_class__

    def get_char_stats(self):
        return self.__char_stats_dict__
    
    def get_char_level(self):
        return self.__char_level__
    
    def get_char_hp(self):
        return self.__hp__
    
    def get_char_ac(self):
        return self.__ac__
    
    def get_char_armor(self):
        if self.__armor__ == "None":
            return "None"
        return self.__armor__[2]
    
    def get_char_weapon(self):
        if self.__weapon__ == "None":
            return "None"
        return self.__weapon__[2]
    
    def get_char_shield(self):
        if self.__shield__ == "None":
            return "None"
        return self.__shield__[2]



    # Create the global names list variable from the data in the names.csv file.
    def name_roll(self):
        names_list = []
        try:
            with open("names.csv", mode = "r", newline = "") as namefile:
                file_reader = csv.reader(namefile)
                for row in file_reader:
                    names_list.append(row[0])
            self.__name__ = random.choice(names_list)
        except:
            Exception



    # Functions controlling character gender.
    def random_gender(self):
        char_sex = random.randint(1, 2)
        if char_sex == 1:
            self.__gender__ = "Male"
        else:
            self.__gender__ = "Female"

    def change_gender(self):
        if self.__gender__ == "Male":
            self.__gender__ = "Female"
        else:
            self.__gender__ = "Male"



    # This section is for all the functions used in rolling a character's race
    def race_roll(self):
        races_list = [
            Aarakocra,
            Aasimar,
            Bugbear,
            Centaur,
            Changeling,
            Dragonborn,
            #Dwarf, (Duergar too)
            #Elf, (Eladrin,	Sea Elf, Shadar-Kai too)
            #Fairy,
            #Firbolg,
            #Genasi,
            #Githyanki,
            #Githzerai,
            #Gnome, (Deep Gnome too)
            #Goblin,
            #Goliath,
            #Grung,
            #Half-Elf,
            #Halfling,
            #Half-Orc,
            #Harengon,
            #Hobgoblin,
            #Human,
            #Kenku,
            #Kobold,
            #Lizardfolk,
            #Minotaur,
            #Orc,
            #Owlin,
            #Satyr,
            #Shifter,
            #Tabaxi,
            #Tiefling,
            #Tortle,
            #Triton,
            #Verdan,
            #Yuan-Ti
        ]
        race = random.choice(races_list)
        self.race = race()

    def secondary_score(self):
        return [2, "CON"]

    # The following are functions related to rolling a character's stats and adding all stat bonuses together.
    def stats_roll(self):
        self.rolls_for_stats = [0, 0, 0, 0, 0, 0]
        while self.rolls_for_stats[self.key_stat_index()[0]] == 0 or self.rolls_for_stats[self.key_stat_index()[0]] < max(self.rolls_for_stats):
            for i in range(6):
                self.rolls_for_stats[i] = self.four_six_drop_low()

    def four_six_drop_low(self):
        rolls_list = []
        for i in range(4):
            rolls_list.append(random.randint(1, 6))
        rolls_list.remove(min(rolls_list))
        return rolls_list[0] + rolls_list[1] + rolls_list[2]

    def stats_compile(self):
        self.__char_stats_dict__.update({
            "STR": self.rolls_for_stats[0],
            "DEX": self.rolls_for_stats[1],
            "CON": self.rolls_for_stats[2],
            "INT": self.rolls_for_stats[3],
            "WIS": self.rolls_for_stats[4],
            "CHA": self.rolls_for_stats[5]
        })
        race_bonus = self.race.get_race_stats(self.key_stat_index()[1], self.secondary_score()[1])
        for bonus in race_bonus:
            self.__char_stats_dict__[bonus] += race_bonus[bonus]



    # Function for randomly rolling a character's level. Odds of each level appearing can be altered in the "variables_page" file. Variables used are max_char_level and char_level_odds.
    def random_char_level(self):
        level_num = max_char_level
        levels_list = []
        weights_list = []
        odds_value = 10
        while True:
            levels_list.append(level_num)
            level_num -= 1
            if level_num == 0:
                break
        for i in range(max_char_level):
            weights_list.append(odds_value)
            odds_value = int(round(char_level_odds * odds_value))
        self.__char_level__ = random.choices(levels_list, weights=weights_list, k=1)[0]

    def roll_hp(self):
        dice_faces_list = [] # Create an empty list for the hit dice
        hp = 0 # Create hp variable and set it equal to 0
        for i in range(self.hp_stat_index()): # Call hp_stat_index to get size of hit die. Function returns a number (either 6, 8, 10, or 12).
            i += 1
            dice_faces_list.append(i) # Add a number to the list a number of times equal to the hit die. This list is our d6, d8, d10, or d12.
        hp += self.hp_stat_index() # Increase health by max roll to represent level 1 hp.
        for i in range(self.__char_level__ - 1): # Roll a number of times equal to 1 - character level to represent rolling for health for each level after the 1st.
            hp += random.choice(dice_faces_list) # Increase health by a random number from the die_face_list to represent rolling the die.
        hp += (stat_mod_dict[self.__char_stats_dict__["CON"]] * self.__char_level__) # Add an amount of hp = CON modifier * level.
        self.__hp__ = hp # Set self.__hp__ to our hp variable.



    # The following section is for the functions related to rolling a character's equipment and calculating a character's AC.
    def roll_armor(self):
        if len(self.armor_list) > 0:
            self.__armor__ = random.choice(self.armor_list)

    def roll_weapon(self):
        if len(self.weapon_list) > 0:
            self.__weapon__ = random.choice(self.weapon_list)

    def roll_shield(self):
        if random.randint(1, shield_chance) <= 10:
            self.__shield__ = self.shield_availability

    def make_equipment_list(self):
        print(f"Using character class: {self.__char_class__}")
        self.__shield__ = "None"
        self.__armor__ = "None"
        self.__weapon__ = "None"
        self.shield_availability = "None"
        with open("equipment.csv", mode = "r", newline = "") as csvfile:
            file_reader = csv.reader(csvfile)
            for row in file_reader:
                if row[0] == "Armor" and self.__char_class__ in row[1]:
                    self.armor_list.append(row)
                if row[0] == "Weapon" and self.__char_class__ in row[1]:
                    self.weapon_list.append(row)
                if row[0] == "Shield" and self.__char_class__ in row[1]:
                    self.shield_availability = row
    
    def calculate_ac(self):
        if self.__armor__ == "None":
            if self.__shield__ == "None":
                self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]]
            else:
                self.__ac__ = 12 + stat_mod_dict[self.__char_stats_dict__["DEX"]]
        elif self.__shield__ == "None":
            if self.__char_stats_dict__["DEX"] > int(ast.literal_eval(self.__armor__[3])[0]):
                self.__ac__ = int(ast.literal_eval(self.__armor__[3])[1]) + int(ast.literal_eval(self.__armor__[3])[0])
            else:
                self.__ac__ = int(ast.literal_eval(self.__armor__[3])[1]) + stat_mod_dict[self.__char_stats_dict__["DEX"]]
        else:
            if self.__char_stats_dict__["DEX"] > int(ast.literal_eval(self.__armor__[3])[0]):
                self.__ac__ = int(ast.literal_eval(self.__armor__[3])[1]) + int(ast.literal_eval(self.__armor__[3])[0]) + 2
            else:
                self.__ac__ = int(ast.literal_eval(self.__armor__[3])[1]) + stat_mod_dict[self.__char_stats_dict__["DEX"]] + 2

    def __str__(self):
        return (
            f"Character name: {self.get_char_name()} \n"
            f"Character gender: {self.get_char_gender()} \n"
            f"Character race: {self.race.get_name()} \n"
            f"Character class: {self.get_char_class()} \n"
            f"Character stats: {', '.join(f'{key}: {value}' for key, value in self.__char_stats_dict__.items())} \n"
            f"Character level: {self.__char_level__} \n"
            f"Character HP: {self.__hp__} \n"
            f"Character AC: {self.__ac__} \n"
            f"Character weapon: {self.get_char_weapon()} \n"
            f"Character armor: {self.get_char_armor()} \n"
            f"Character shield: {self.get_char_shield()}"
        )
    