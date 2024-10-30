import csv
import os
from DnD_classes import *
from variables_page import class_odds_list


exit = True
exit_keywords_list = ["exit", "quit"]


#Check if saved characters file exists. If it doesn't, create it and write the header.
if os.path.exists("saved_characters.csv"):
    print("Saved characters directory csv file exists!")
else:
    with open("saved_characters.csv", mode="w") as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
        file_writer.writerow(["Character ID", "Name", "Gender", "Race", "Stats", "Class", "Level", "HP", "AC", "Weapon", "Armor", "Shield"])
        print("Saved characters directory csv file created!")

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

# Function that rolls a random class. Odds determined by "class_odds_list" on variables_page.py
def class_roll():
    global class_mapping
    return random.choices(list(class_mapping.keys()), weights = class_odds_list, k=1)[0]

# Prints all the commands and their explanations when called by the main function.
def help():
    print("Type \"exit\" or \"quit\" to end the program.")
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
    print("Type \"fast\" to roll and save a character without prompts.")
    print("Type \"bulk\" to roll and save many characters without prompts.")

# Fast roll function that rolls and saves a character without prompting the user
def fast_roll():
    char_class = class_roll()
    char_id = class_mapping[char_class](random.randint(100000, 999999))
    with open("saved_characters.csv", mode = "a", newline = "") as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
        file_writer.writerow([char_id.get_char_id(),
                            char_id.get_char_name(),
                            char_id.get_char_gender(),
                            char_id.get_char_race(),
                            char_id.get_char_stats(),
                            char_id.get_char_class(),
                            char_id.get_char_level(),
                            char_id.get_char_hp(),
                            char_id.get_char_ac(),
                            char_id.get_char_weapon(),
                            char_id.get_char_armor(),
                            char_id.get_char_shield()
                        ])
    print(char_id)
    print("Character saved!")

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



def main():
    global exit

    # First while loop. Prompts user to start while still enabling the fast, bulk, and help options without advancing the program. Also allows for exit.
    while exit:
        user_input = input(f"Press Enter to start rolling a character! Type \"help\" for a full list of commands. ")
        if user_input.lower() == "fast":
            fast_roll()
        elif user_input.lower() == "bulk":
            bulk_fast_roll()
        elif user_input.lower() == "help":
            help()
        elif  user_input.lower() in exit_keywords_list:
            exit = False
            print("---Exiting Program---")
        elif user_input not in ["", exit_keywords_list[0], exit_keywords_list[1], "help", "fast", "bulk"]:
                print("---Command not recognized. Please try again.---")
        else:
            char_class = class_roll()
            print(f"Character's class is {char_class}.")

            # Second while loop. Prompts the user to roll a character class while still enabling the fast, bulk, and help options without advancing the program. Also allows for exit.
            while exit:
                user_input = input(f"Character's class is {char_class}. Would you like to reroll this character's class? Press Enter to continue. Type \"r\" to reroll. Type \"help\" for a full list of commands. ")
                if user_input.lower() == "fast":
                    fast_roll()
                elif user_input.lower() == "bulk":
                    bulk_fast_roll()
                elif user_input.lower() == "help":
                    help()
                elif  user_input.lower() in exit_keywords_list:
                    exit = False
                    print("---Exiting Program---")
                    continue
                elif user_input == "r":
                    char_class = class_roll()
                    continue
                elif user_input not in ["", "r", exit_keywords_list[0], exit_keywords_list[1], "help", "fast", "bulk"]:
                    print("---Command not recognized. Please try again.---")
                else:
                    char_id = class_mapping[char_class](random.randint(100000, 999999))
                    print(char_id)
                    user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")  
                    
                    #  Third while loop. Prompts the user to enter commands to finalize character creation, and handles saves. Still allows for the fast, bulk, and help options without advancing the program. Also allows for exit.
                    while exit:
                        if user_input.lower() in exit_keywords_list:
                            exit = False
                            print("---Exiting Program---")
                            break
                        elif user_input.lower() == "help":
                            help()
                            user_input = input("Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "character":
                            print(char_id)
                            user_input = input("Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "name":
                            char_id.name_roll()
                            print(f"This character's name is now {char_id.get_char_name()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "gender":
                            char_id.change_gender()
                            print(f"This character's gender is now {char_id.get_char_gender()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "race":
                            char_id.race_roll()
                            char_id.stats_compile()
                            char_id.roll_hp()
                            print(f"This character's race is now {char_id.get_char_race()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() in ["stat", "stats"]:
                            char_id.stats_roll()
                            char_id.stats_compile()
                            char_id.roll_hp()
                            print(f"This character's stats are now {char_id.get_char_stats()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "level":
                            char_id.random_char_level()
                            char_id.roll_hp()
                            print(f"This character's level is now {char_id.get_char_level()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "weapon":
                            char_id.roll_weapon()
                            print(f"This character is now wielding a {char_id.get_char_weapon()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "armor":
                            char_id.roll_armor()
                            char_id.calculate_ac()
                            print(f"This character is now wearing {char_id.get_char_armor()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "shield":
                            char_id.roll_shield()
                            char_id.calculate_ac()
                            print(f"This character character's shield is now {char_id.get_char_shield()}.")
                            print(char_id)
                            user_input = input("Character rolled! Please type what you would like to do next. Type \"help\" for a list of available commands! ")
                        elif user_input.lower() == "save":
                            with open("saved_characters.csv", mode = "a", newline = "") as csvfile:
                                file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
                                file_writer.writerow([char_id.get_char_id(),
                                                    char_id.get_char_name(),
                                                    char_id.get_char_gender(),
                                                    char_id.get_char_race(),
                                                    char_id.get_char_stats(),
                                                    char_id.get_char_class(),
                                                    char_id.get_char_level(),
                                                    char_id.get_char_hp(),
                                                    char_id.get_char_ac(),
                                                    char_id.get_char_weapon(),
                                                    char_id.get_char_armor(),
                                                    char_id.get_char_shield()
                                                ])
                            print(char_id)
                            print("Character saved!")
                            user_input = input("Would you like to roll another character? Type \"y\" for yes and \"n\" for no. ")
                            while user_input not in ["y", "n"]:
                                if user_input.lower() == "y":
                                    break
                                elif user_input.lower() == "n":
                                    exit = False
                                    print("---Exiting Program---")
                                    break
                                else:
                                    user_input = input("Invalid reponse. Please try again and type \"y\" for yes and \"n\" for no. ")
                            break
                        elif user_input.lower() == "fast":
                            fast_roll()
                            break
                        elif user_input.lower() == "bulk":
                            bulk_fast_roll()
                            break
                        else:
                            user_input = input("User input not recognized. Please try again. Type \"help\" for a list of available commands! ")
                    break

if __name__ == "__main__":
        main()