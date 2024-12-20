import csv
import os
import random
from DnD_classes import *
from parent_character_class import Character
from variables_page import class_odds_list

# These two functions are for loop 2 of the main function and make it so a class object is only created after character class has been decided.
class_mapping = {
        "Artificer": Artificer,
        "Barbarian": Barbarian,
        "Bard": Bard,
        "Cleric": Cleric,
        "Commoner": Commoner,
        "Druid": Druid,
        "Fighter": Fighter,
        "Monk": Monk,
        "Paladin": Paladin,
        "Ranger": Ranger,
        "Rogue": Rogue,
        "Sorcerer": Sorcerer,
        "Warlock": Warlock,
        "Wizard": Wizard
    }

def class_roll():
    global class_mapping
    return random.choices(list(class_mapping.keys()), weights = class_odds_list, k=1)[0]



#CSV Functions
def check_or_create_csv():
    try:
        if os.path.exists("saved_characters.csv"):
            print("Saved characters directory csv file exists!")
        else:
            with open("saved_characters.csv", mode="w") as csvfile:
                file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
                file_writer.writerow(["Character ID", "Name", "Alignment", "Gender", "Race", "Subrace", "Class", "Subclass", "Languages", "Speed", "Size", "Saving Throws", "Stats", "Level", "HP", "AC", "Weapon", "Armor", "Shield", "Proficiencies", "Character Features"])
                print("Saved characters directory csv file created!")
    except Exception as e:
        print(e)



# This section is dedicated to the help function and the functions that it mentions
def help_loop_one():
    print("Type \"exit\" or \"quit\" to end the program.")
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to select a number of characters to roll and save without prompts.")
    print("Press Enter to begin rolling a character!")

def help_loop_two():
    print("Type \"exit\" or \"quit\" to end the program.")
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to select a number of characters to roll and save without prompts.")
    print("Type \"r\" to reroll your character's class!")
    print("Type \"class info\" for a list of all available classes!")
    print("Type the name of the class you want to use that character class.")
    print("Press Enter to accept your character's class and roll out the character!")

def help_loop_three():
    print("Type \"exit\" or \"quit\" to end the program.")
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to select a number of characters to roll and save without prompts.")
    print("Type \"name\" to reroll character's name.")
    print("Type \"enter name\" to manually enter a name for the character.")
    print("Type \"gender\" to switch character's gender.")
    print("Type \"race\" to reroll character's race.")
    print("Type the name of a race to use that specific race.")
    print("Type \"race info\" for a list of all available races!")
    print("Type \"subclass\" to reroll your subclass!")
    print("Type \"stat\" or \"stats\" to reroll character's stats.")
    print("Type \"level\" to reroll character's level.")
    print("Type \"select level\" to manually select character's level.")
    print("Type \"weapon\" to reroll character's weapon.")
    print("Type \"armor\" to reroll character's armor.")
    print("Type \"shield\" to reroll if a character has a shield.")
    print("Type \"character\" or \"info\" to see shortened character information.")
    print("Type \"details\" or \"full\" to see all character information.")
    print("Type \"save\" to save the character")    

def help_exit():
    print("---Exiting Program---")
    return True

def help_name(char_id):
    char_id.name_roll()
    print(f"This character's name is now {char_id.get_char_name()}.")

def help_enter_name(char_id, name):
    char_id.__name__ = name
    print(f"This character's name is now {char_id.get_char_name()}.")

def help_alignment(char_id):
    char_id.alignment_compiler()
    print(f"This character's alignment is now {char_id.get_alignment()}")

def help_gender(char_id):
    char_id.change_gender()
    print(f"This character's gender is now {char_id.get_char_gender()}.")

def help_race(char_id):
    char_id.race_roll()
    char_id.proficiency_compiler()
    char_id.features_compiler()
    char_id.make_equipment_list()
    char_id.stats_compile()
    char_id.roll_hp()
    print(f"This character's race is now {char_id.race.get_subrace_name()}.")

def help_race_select(char_id, input_string):
    char_id.race = globals()[input_string.title()]()
    char_id.proficiency_compiler()
    char_id.features_compiler()
    char_id.make_equipment_list()
    char_id.stats_compile()
    char_id.roll_hp()
    print(f"This character's race is now: {char_id.race.get_subrace_name()}.")

def help_subclass(char_id):
    char_id.subclass_roll()
    char_id.proficiency_compiler()
    char_id.features_compiler()
    char_id.languages_compiler()
    char_id.make_equipment_list()
    print(f"This character's subclass is now: {char_id.get_subclass()}")

def help_stat(char_id):
    char_id.stats_roll()
    char_id.stats_compile()
    char_id.roll_hp()
    print(f"This character's stats are now {char_id.get_char_stats()}.")

def help_level(char_id):
    pre_level_asi = char_id.get_asi()
    char_id.random_char_level()
    new_asi = char_id.get_asi()
    if pre_level_asi != new_asi:
        char_id.stats_roll()
        char_id.stats_compile()
    else:
        char_id.stats_compile()
    char_id.subclass_roll()
    char_id.size_check()
    char_id.proficiency_compiler()
    char_id.features_compiler()
    char_id.languages_compiler()
    char_id.roll_hp()
    print(f"This character's level is now {char_id.get_char_level()}.")

def help_select_level(char_id, value):
    pre_level_asi = char_id.get_asi()
    char_id.__char_level__ = value
    new_asi = char_id.get_asi()
    if pre_level_asi != new_asi:
        char_id.stats_roll()
        char_id.stats_compile()
    else:
        char_id.stats_compile()
    char_id.subclass_roll()
    char_id.size_check()
    char_id.proficiency_compiler()
    char_id.features_compiler()
    char_id.languages_compiler()
    char_id.roll_hp()
    print(f"This character's level is now {char_id.get_char_level()}.")

def help_weapon(char_id):
    char_id.roll_weapon()
    if char_id.get_char_weapon().lower() in ["greatclub", "light crossbow", "shortbow", "glaive", "greataxe", "greatsword", "halberd", "lance", "maul", "pike", "heavy crossbow", "longbow"]:
        char_id.remove_shield()
        char_id.calculate_ac()
        print(f"This character is now wielding a {char_id.get_char_weapon()}. New weapon is two-handed.")
        return
    print(f"This character is now wielding a {char_id.get_char_weapon()}.")

def help_armor(char_id):
    char_id.roll_armor()
    char_id.calculate_ac()
    print(f"This character is now wearing {char_id.get_char_armor()}.")

def help_shield(char_id):
    char_id.roll_shield()
    char_id.calculate_ac()
    print(f"This character character's shield is now {char_id.get_char_shield()}.")

def help_save(char_id):
    char_id.race.get_subrace_name()
    try:
        with open("saved_characters.csv", mode = "a", newline = "") as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
            file_writer.writerow(
                [char_id.get_char_id(),
                char_id.get_char_name(),
                char_id.get_char_alignment(),
                char_id.get_char_gender(),
                char_id.get_char_race(),
                char_id.get_char_subrace(),
                char_id.get_char_class(),
                char_id.get_char_subclass()[0],
                ', '.join(char_id.get_char_languages()),
                char_id.get_char_speed(),
                char_id.get_char_size(),
                ', '.join(f"{key}: {value}" for key, value in char_id.get_char_stats().items()),
                ', '.join(f"{key}: {'+' if value > 0 else ''}{value}" for key, value in char_id.get_char_saving_throws().items()),
                char_id.get_char_level(),
                char_id.get_char_hp(),
                char_id.get_char_ac(),
                char_id.get_char_weapon(),
                char_id.get_char_armor(),
                char_id.get_char_shield(),
                ', '.join(f'{item}' for item in set(char_id.get_char_proficiencies())),
                ', '.join(f'{item}' for item in char_id.get_char_features())
            ])
        print(char_id)
        print("---Character saved!---")
    except Exception as e:
        print(e)

def help_character(char_id):
    print(char_id)

def help_details(char_id):
    char_id.race.get_subrace_name()
    print(
        f"Character name: {char_id.get_char_name()} \n"
        f"Character alignment: {char_id.get_char_alignment()} \n"
        f"Character gender: {char_id.get_char_gender()} \n"
        f"Character race: {char_id.get_char_race()} \n"
        f"Character subrace: {char_id.get_char_subrace()} \n"
        f"Character class: {char_id.get_char_class()} \n"
        f"Character subclass: {char_id.get_char_subclass()[0]} \n"
        f"Character languages: {', '.join(char_id.get_char_languages())} \n"
        f"Character speed: {char_id.get_char_speed()} \n"
        f"Character size: {char_id.get_char_size()} \n"
        f"Character stats: {', '.join(f'{key}: {value}' for key, value in char_id.get_char_stats().items())} \n"
        f"Character saving throws: " + ', '.join(f'{key}: {"+" if value > 0 else ""}{value}' for key, value in char_id.get_char_saving_throws().items()) + "\n"
        f"Character level: {char_id.get_char_level()} \n"
        f"Character HP: {char_id.get_char_hp()} \n"
        f"Character AC: {char_id.get_char_ac()} \n"
        f"Character weapon: {char_id.get_char_weapon()} \n"
        f"Character armor: {char_id.get_char_armor()} \n"
        f"Character shield: {char_id.get_char_shield()} \n"
        f"Character proficiencies: {', '.join(f'{item}' for item in set(char_id.get_char_proficiencies()))} \n"
        f"Character features: {', '.join(f'{item}' for item in char_id.get_char_features())}"
    )



# Fast roll function that rolls and saves a character without prompting the user
def fast_roll():
    char_class = class_roll()
    char_id = class_mapping[char_class](random.randint(100000, 999999))
    try:
        with open("saved_characters.csv", mode = "a", newline = "") as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
            file_writer.writerow(
                [char_id.get_char_id(),
                char_id.get_char_name(),
                char_id.get_char_alignment(),
                char_id.get_char_gender(),
                char_id.get_char_race(),
                char_id.get_char_subrace(),
                char_id.get_char_class(),
                char_id.get_char_subclass()[0],
                ", ".join(char_id.get_char_languages()),
                char_id.get_char_speed(),
                char_id.get_char_size(),
                ', '.join(f'{key}: {"+" if value > 0 else ""}{value}' for key, value in char_id.get_char_saving_throws().items()),
                char_id.get_char_saving_throws(),
                char_id.get_char_level(),
                char_id.get_char_hp(),
                char_id.get_char_ac(),
                char_id.get_char_weapon(),
                char_id.get_char_armor(),
                char_id.get_char_shield(),
                ', '.join(f'{item}' for item in set(char_id.get_char_proficiencies())),
                ', '.join(f'{item}' for item in char_id.get_char_features())
            ])
        print(char_id)
        print("---Character saved!---")
    except Exception as e:
        print(e)
    

# Bull fast roll function that rolls and saves an amount of characters decided by the user without any prompts
def bulk_fast_roll(value):
        for i in range(value):
            fast_roll()