import csv
import random
from DnD_classes import *
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



# This section is dedicated to the help function and the functions that it mentions
def help_loop_one():
    print("Type \"exit\" or \"quit\" to end the program.")
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to roll and save many characters without prompts.")
    print("Press Enter to begin rolling a character!")

def help_loop_two():
    print("Type \"exit\" or \"quit\" to end the program.")
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to roll and save many characters without prompts.")
    print("Type \"r\" to reroll your character's class!")
    print("Type the name of the class you want to use that character class.")
    print("Press Enter to accept your character's class and roll out the character!")

def help_loop_three():
    print("Type \"exit\" or \"quit\" to end the program.")
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to roll and save many characters without prompts.")
    print("If you've rolled a character, type \"name\" to reroll character's name.")
    print("If you've rolled a character, type \"gender\" to switch character's gender.")
    print("If you've rolled a character, type \"race\" to reroll character's race.")
    print("If you've rolled a character, type \"stat\" or \"stats\" to reroll character's stats.")
    print("If you've rolled a character, type \"level\" to reroll character's level.")
    print("If you've rolled a character, type \"weapon\" to reroll character's weapon.")
    print("If you've rolled a character, type \"armor\" to reroll character's armor.")
    print("If you've rolled a character, type \"shield\" to reroll if a character has a shield.")
    print("If you've rolled a character, type \"save\" to save the character")
    print("If you've rolled a character, type \"character\" to see all the information on the character.")

def help_exit():
    print("---Exiting Program---")
    return True

def help_name(char_id):
    char_id.name_roll()
    print(f"This character's name is now {char_id.get_char_name()}.")
    print(char_id)

def help_gender(char_id):
    char_id.change_gender()
    print(f"This character's gender is now {char_id.get_char_gender()}.")
    print(char_id)

def help_race(char_id):
    char_id.race_roll()
    char_id.stats_compile()
    char_id.roll_hp()
    print(f"This character's race is now {char_id.race.get_name()}.")
    print(char_id)

def help_stat(char_id):
    char_id.stats_roll()
    char_id.stats_compile()
    char_id.roll_hp()
    print(f"This character's stats are now {char_id.get_char_stats()}.")
    print(char_id)

def help_level(char_id):
    char_id.random_char_level()
    char_id.roll_hp()
    print(f"This character's level is now {char_id.get_char_level()}.")
    print(char_id)

def help_weapon(char_id):
    char_id.roll_weapon()
    print(f"This character is now wielding a {char_id.get_char_weapon()}.")
    print(char_id)

def help_armor(char_id):
    char_id.roll_armor()
    char_id.calculate_ac()
    print(f"This character is now wearing {char_id.get_char_armor()}.")
    print(char_id)

def help_shield(char_id):
    char_id.roll_shield()
    char_id.calculate_ac()
    print(f"This character character's shield is now {char_id.get_char_shield()}.")
    print(char_id)

def help_save(char_id):
    try:
        with open("saved_characters.csv", mode = "a", newline = "") as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
            file_writer.writerow(
                [char_id.get_char_id(),
                char_id.get_char_name(),
                char_id.get_char_gender(),
                char_id.get_char_race(),
                ', '.join(f"{key}: {value}" for key, value in char_id.__char_stats_dict__.items()),
                char_id.get_char_class(),
                char_id.get_char_level(),
                char_id.get_char_hp(),
                char_id.get_char_ac(),
                char_id.get_char_weapon(),
                char_id.get_char_armor(),
                char_id.get_char_shield()
            ])
        print(char_id)
        print("---Character saved!---")
    except Exception as e:
        print(e)
    

def help_character(char_id):
    print(char_id)



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
                char_id.get_char_gender(),
                char_id.get_char_race(),
                ', '.join(f"{key}: {value}" for key, value in char_id.__char_stats_dict__.items()),
                char_id.get_char_class(),
                char_id.get_char_level(),
                char_id.get_char_hp(),
                char_id.get_char_ac(),
                char_id.get_char_weapon(),
                char_id.get_char_armor(),
                char_id.get_char_shield()
            ])
        print(char_id)
        print("---Character saved!---")
    except Exception as e:
        print(e)
    

# Bull fast roll function that rolls and saves an amount of characters decided by the user without any prompts
def bulk_fast_roll():
        while True:
            try:
                function_input = int(input("Please enter the number of characters you would like to roll: "))
                break
            except:
                print("User input is not a number. Please try again. ")
        for i in range(function_input):
            fast_roll()