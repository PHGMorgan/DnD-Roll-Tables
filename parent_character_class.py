import ast
import random
import csv
from DnD_classes import *
from race_class import *
from variables_page import max_char_level, char_level_odds, stat_mod_dict, shield_chance, race_weights


# To-do list:
# - IMPORTANT: Rework proficiencies, and make proficiencies a new character trait/feature.
# - ---DONE--- Move name list to outside Character class so it can be made once and then saved for duration of program running to save on system resources.
# - ---DONE--- Move armor, weapon, and shield lists outside of Character class to save on system resources when bulk rolling.
# - Comment all code and try to make it more efficient in lacking or old areas.
# - ---DONE--- Make Languages a separate pull and new character feature outside of the "character features" list.
# - ---DONE---Include a way to select character level the same way you can select class and race.
# - ---DONE---Include a way to type your own name for a character.
# - Maybe try to find a way to make a "settings" of sorts to allow users to change odds parameters after program has started.
# - ---DONE--- Make some weapons two-handed.
# - Maybe add skill proficiencies/points for the classes.
# - Should I include backgrounds!?

name_list = []
equipment_list = []

def create_name_list():
    global name_list
    if len(name_list) == 0:
        try: 
            with open("names.csv", mode="r") as csvfile:
                file_reader = csv.reader(csvfile)
                for row in file_reader:
                    name_list.append(row[0])
            return name_list
        except Exception as e:
            print(e)
    else:
        return name_list
    
def pull_from_equipment():
    global equipment_list
    if len(equipment_list) == 0:
        try:
            with open("equipment.csv", mode="r") as csvfile:
                file_reader = csv.reader(csvfile)
                next(file_reader)
                for row in file_reader:
                    equipment_list.append(row)
            return equipment_list
        except Exception as e:
            print(e)
    else:
        return equipment_list

            

class Character:
    def __init__(self, char_id):
        # Set up all variable names
        self.__char_id__ = char_id
        self.__name__ = self.name_roll()
        self.__gender__ = self.random_gender()
        self.__alignment__ = self.alignment_compiler()
        self.__char_stats_dict__ = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.rolls_for_stats, self.armor_list, self.weapon_list, self.__features__, self.__languages__ = [], [], [], [], []
        self.__armor__, self.__weapon__, self.__shield__  = "None", "None", "None"
        # Run randomizers for each character variable
        self.race_roll()
        self.random_char_level()
        self.stats_roll()
        self.stats_compile()
        self.subclass_roll()
        self.proficiency_compiler()
        self.features_compiler()
        self.languages_compiler()
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
    
    def get_features(self):
        self.features_compiler()
        return self.__features__
    
    def get_alignment(self):
        return self.__alignment__

    def get_subclass(self):
        if self.subclass == "None":
            return self.subclass
        return self.subclass[0]

    def get_languages(self):
        return self.__languages__

    def remove_shield(self):
        self.__shield__ = "None"


    # Create the global names list variable from the data in the names.csv file.
    def name_roll(self):
        roll_list = create_name_list()
        return random.choice(roll_list)



    # Functions for rolling a character's alignment.
    def lawful_chaotic_roller(self):
        horizontal_axis_list = ["Lawful", "Neutral", "Chaotic"]
        return random.choices(horizontal_axis_list, weights=[3,2,1], k=1)[0]

    def good_evil_roller(self):
        vertical_axis_list = ["Good", "Neutral", "Evil"]
        return random.choices(vertical_axis_list, weights=[3,6,1])[0]
        
    def alignment_compiler(self):
        horiz = self.lawful_chaotic_roller()
        vert = self.good_evil_roller()
        if horiz == vert:
            return "True Neutral"
        else:
            return f"{horiz} {vert}"



    # Functions controlling character gender.
    def random_gender(self):
        char_sex = random.randint(1, 2)
        if char_sex == 1:
            return "Male"
        else:
            return "Female"

    def change_gender(self):
        if self.__gender__ == "Male":
            self.__gender__ = "Female"
        else:
            self.__gender__ = "Male"



    # This section is for all the functions used in rolling a character's race
    def race_roll(self):
        races_list = [
            Aarakocra, Aasimar, Bugbear, Centaur, Changeling, Dragonborn, Dwarf, Elf,
            Fairy, Firbolg, Genasi, Githyanki, Githzerai, Gnome, Goblin, Goliath,
            Grung, HalfElf, Halfling, HalfOrc, Harengon, Hobgoblin, Human, Kenku,
            Kobold, Lizardfolk, Minotaur, Orc, Owlin, Satyr, Shifter, Tabaxi,
            Tiefling, Tortle, Triton, Verdan, YuanTi
        ]
        race = random.choices(races_list, weights=race_weights, k=1)[0]
        self.race = race()

    def secondary_score(self):
        return [2, "CON"]
    
    def size_check(self):
        if self.race.get_race_name() == "Verdan" and self.__char_level__ >= 5:
            return "Size- Medium"
        else:
            return self.race.get_size()



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
        if self.get_asi() > 0:
            for i in range(self.get_asi()):
                self.apply_asi()

    def apply_asi(self):
        def apply_plus_one(stat):
            if self.__char_stats_dict__[stat] < 20:
                self.__char_stats_dict__[stat] += 1
                return True
            return False
        
        def apply_plus_two(stat):
            if self.__char_stats_dict__[stat] < 19:
                self.__char_stats_dict__[stat] += 2
                return True
            return False
        
        def random_stat():
            while True:
                random_stat = random.choice(stat_names_list)
                if random_stat != self.key_stat_index()[1] and random_stat != self.secondary_score()[1]:
                    return random_stat

        if random.choice([2, 1]) == 1:
            if apply_plus_one(self.key_stat_index()[1]):
                if not apply_plus_one(self.secondary_score()[1]):
                    while True:
                        if apply_plus_one(random_stat()):
                            break
            else:
                if not apply_plus_one(self.secondary_score()[1]):
                    while True:
                        random_stat_1 = random_stat()
                        if apply_plus_one(random_stat_1):
                            break
                    while True:
                        random_stat_2 = random_stat()
                        if random_stat_2 != random_stat_1:
                            if apply_plus_one(random_stat_2):
                                break
                else:
                    while True:
                        if apply_plus_one(random_stat()):
                            break
        else:
            if not apply_plus_two(self.key_stat_index()[1]):
                if not apply_plus_two(self.secondary_score()[1]):
                    while True:
                        if apply_plus_two(random_stat()):
                            break



    # Function for randomly rolling a character's level and some character features. Odds of each level appearing can be altered in the "variables_page" file. Variables used are max_char_level and char_level_odds.
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

    def proficiency_compiler(self):
        proficiency_list = []
        for item in self.race.get_proficiencies(): # Get list of racial proficiencies.
            proficiency_list.append(item) # Add it to the list if character level is greater than or equial to the level requirement.
        for item in self.get_class_proficiencies(): # Repeat the process for class proficiencies.
            proficiency_list.append(item)
        self.proficiencies = proficiency_list # Set self.proficiencies equal to the created list.

    def features_compiler(self):
        features_list = []
        for item in self.race.get_features():
            if self.__char_level__ >= item[0]:
                features_list.append(item[1])
        for item in self.get_class_features():
            if self.__char_level__ >= item[0]:
                features_list.append(item[1])
        if len(features_list) > 0:
            self.__features__ = features_list
        else:
            self.__features__ = ["None"]

    def get_class_language(self):
        return []

    def languages_compiler(self):
        languages = []
        languages.extend(self.race.get_languages())
        languages.extend(self.get_class_language())
        self.__languages__ = set(languages)


    # The following section is for functions used to calculate a character's HP.
    def subclass_tough_flag(self):
        return (False, 0)

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
        if self.subclass_tough_flag()[0] or self.race.tough_flag()[0]: # Check to see if character has a feature to grant extra hp that's signalled with the tough flag.
            hp =+ (self.__char_level__ * self.subclass_tough_flag()[1]) + (self.__char_level__ * self.race.tough_flag()[1])
        if hp <= 0:
            self.__hp__ = 1
        else:
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
            print(self.get_char_weapon().lower() in ["greatclub", "light crossbow", "shortbow", "glaive", "greataxe", "greatsword", "halberd", "lance", "maul", "pike", "heavy crossbow", "longbow"])
            if self.get_char_weapon().lower() in ["greatclub", "light crossbow", "shortbow", "glaive", "greataxe", "greatsword", "halberd", "lance", "maul", "pike", "heavy crossbow", "longbow"]:
                self.__shield__ = "None"
            else:
                self.__shield__ = self.shield_availability

    def make_equipment_list(self):
        self.shield_availability = "None"
        character_list = pull_from_equipment()
        for row in character_list:
            if row[0] == "Armor" and  any(item in row[1] for item in self.proficiencies):
                self.armor_list.append(row)
            if row[0] == "Weapon" and any(item in row[1] for item in self.proficiencies):
                self.weapon_list.append(row)
            if row[0] == "Shield" and any(item in row[1] for item in self.proficiencies):
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
            f"Character alignment: {self.get_alignment()} \n"
            f"Character gender: {self.get_char_gender()} \n"
            f"Character subrace: {self.race.get_subrace_name()} \n"
            f"Character class: {self.get_char_class()} \n"
            f"Character stats: {', '.join(f'{key}: {value}' for key, value in self.__char_stats_dict__.items())}"
        )