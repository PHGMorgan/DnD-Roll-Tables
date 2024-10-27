import random
import csv
from DnD_classes import *
from variables_page import max_char_level, char_level_odds, stat_mod_dict

class Character:
    def __init__(self, char_id):
        #Set up all variable names
        self.__char_id__ = char_id
        self.__name__ = "None"
        self.__gender__ = "None"
        self.__char_race__ = "None"
        self.__char_stats_dict__ = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.rolls_for_stats = []
        #Run randomizers for each character variable
        self.name_roll()
        self.random_gender()
        self.race_roll()
        self.stats_roll()
        self.stats_compile()


    #Block of get functions
    def get_char_id(self):
        return self.__char_id__
    
    def get_name(self):
        return self.__name__
    
    def get_gender(self):
        return self.__gender__
    
    def get_race(self):
        return self.__char_race__[0]
    
    def get_class(self):
        return self.__char_class__

    def get_stats(self):
        return self.__char_stats_dict__
    
    def get_char_level(self):
        return self.__char_level__
    
    def get_char_hp(self):
        return self.__hp__
    
    
    #Create the global names list variable from the data in the names.csv file.
    def name_roll(self):
        names_list = []
        with open("names.csv", mode = "r", newline = "") as namefile:
            file_reader = csv.reader(namefile)
            for row in file_reader:
                names_list.append(row[0])
        self.__name__ = random.choice(names_list)
    
    def random_gender(self):
        char_sex = random.randint(1, 2)
        if char_sex == 1:
            self.__gender__ = "Male"
        else:
            self.__gender__ = "Female"

    def change_gender(self):
        if self.__gender__ == "Male":
            self.__gender__ = "Female"
        self.__gender__ = "Male"

    def race_roll(self):
        races_list = [
            ("Dragonborn", {"STR": 2, "CHA": 1}),
            ("Dwarf", {"STR": 2, "CON": 2}),
            ("Elf", {"DEX": 2, "INT": 1}),
            ("Gnome", {"CON": 1, "INT": 2}),
            ("Half-Elf", {"CHA": 2}),
            ("Half-Orc", {"STR": 2, "CON": 1}),
            ("Halfling", {"DEX": 2, "CHA": 1}),
            ("Human", {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}),
            ("Tiefling", {"INT": 1, "CHA": 2})
        ]
        self.__char_race__ = random.choice(races_list)

    def stats_roll(self):
        self.rolls_for_stats = [0, 0, 0, 0, 0, 0]
        while self.rolls_for_stats[self.key_stat_index()] == 0 or self.rolls_for_stats[self.key_stat_index()] < max(self.rolls_for_stats):
            numbers_rolled = []
            for i in range(6):
                stat_roll = self.four_six_drop_low()
                numbers_rolled.append(stat_roll)
            self.rolls_for_stats = numbers_rolled

    def four_six_drop_low(self):
        rolls_list = []
        for i in range(4):
            rolls_list.append(random.randint(1, 6))
        rolls_list.remove(min(rolls_list))
        return rolls_list[0] + rolls_list[1] + rolls_list[2]

    def stats_compile(self):
        self.__char_stats_dict__["STR"] = self.rolls_for_stats[0]
        self.__char_stats_dict__["DEX"] = self.rolls_for_stats[1]
        self.__char_stats_dict__["CON"] = self.rolls_for_stats[2]
        self.__char_stats_dict__["INT"] = self.rolls_for_stats[3]
        self.__char_stats_dict__["WIS"] = self.rolls_for_stats[4]
        self.__char_stats_dict__["CHA"] = self.rolls_for_stats[5]
        race_bonus_dict = self.__char_race__[1]
        for race_bonus in race_bonus_dict:
            if race_bonus in self.__char_stats_dict__:
                self.__char_stats_dict__[race_bonus] += race_bonus_dict[race_bonus]

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

    # Rolls HP stat. Starts by setting hp to 0 for a fresh start, then creates a list of numbers for each number in hp_stat_index (to represent dice faces).
    # HP is added for free (for level 1), then the list is iterated over a number of times equal to character_level - 1 (for levels 2 and up).
    # Lastly, CON mod is added in by multiplying it by the character_levels. self.__hp__ is then set to this value.
    def roll_hp(self):
        dice_faces_list = []
        hp = 0
        for i in range(self.hp_stat_index()):
            i += 1
            dice_faces_list.append(i)
        hp += self.hp_stat_index()
        for i in range(self.__char_level__ - 1):
            hp += random.choice(dice_faces_list)
        hp += (stat_mod_dict[self.__char_stats_dict__["CON"]] * self.__char_level__)
        self.__hp__ = hp

    def __str__(self):
        return (
            f"Character name: {self.__name__} \n"
            f"Character gender: {self.__gender__} \n"
            f"Character race: {self.__char_race__[0]} \n"
            f"Character class: {self.__char_class__} \n"
            f"Character stats: {self.__char_stats_dict__} \n"
            f"Character level: {self.__char_level__} \n"
            f"Character HP: {self.__hp__}"
        )