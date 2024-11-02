import csv
import os
from DnD_classes import *
from parent_character_class import *
from program_functions import *



#Check if saved characters file exists. If it doesn't, create it and write the header.
if os.path.exists("saved_characters.csv"):
    print("Saved characters directory csv file exists!")
else:
    with open("saved_characters.csv", mode="w") as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
        file_writer.writerow(["Character ID", "Name", "Gender", "Race", "Stats", "Class", "Level", "HP", "AC", "Weapon", "Armor", "Shield"])
        print("Saved characters directory csv file created!")



def main():
    program_exit = False
    loop_reset = False

    # First while loop. Prompts user to start while still enabling the fast, bulk, and help options without advancing the program. Also allows for exit.
    while not program_exit:

        while not program_exit:
            user_input = input(f"Press Enter to start rolling a character! Type \"help\" for a full list of commands. ").lower()
            match user_input:
                case "exit" | "quit":
                    if help_exit():
                        program_exit = True
                        break
                case "fast":
                    fast_roll()
                case "bulk":
                    bulk_fast_roll()
                case "help":
                    help_loop_one()
                case "":
                    break
                case _:
                    print("---Command not recognized. Please try again. Type \"help\" for a list of available commands!---")

        if program_exit:
            break
        
        char_class = class_roll()

        # Second while loop. Prompts the user to roll a character class while still enabling the fast, bulk, and help options without advancing the program. Also allows for exit.
        while not program_exit:
            user_input = input(f"Character's class is {char_class}. Would you like to reroll this character's class? Press Enter to continue. Type \"r\" to reroll. Type \"help\" for a full list of commands. ").lower()
            match user_input:
                case "exit" | "quit":
                    if help_exit():
                        program_exit = True
                        break
                case "fast":
                    fast_roll()
                    loop_reset = True
                    break
                case "bulk":
                    bulk_fast_roll()
                    loop_reset = True
                    break
                case "help":
                    help_loop_two()
                case "r":
                    char_class = class_roll()
                case "":
                    char_id = class_mapping[char_class](random.randint(100000, 999999))
                    break
                case "artificer" | "barbarian" | "bard" | "cleric" | "commoner" | "druid" | "fighter" | "monk" | "paladin" | "ranger" | "rogue" | "sorcerer" | "warlock" | "wizard":
                    char_id = class_mapping[user_input.title()](random.randint(100000, 999999))
                    break
                case _:
                    print("---Command not recognized. Please try again. Type \"help\" for a list of available commands!---")

        if loop_reset:
            continue

        if program_exit:
            break
            
        print(char_id)
        print("Character rolled!")
                    
        #  Third while loop. Prompts the user to enter commands to finalize character creation, and handles saves. Still allows for the fast, bulk, and help options without advancing the program. Also allows for exit.
        while not program_exit:
            user_input = input("Please type what you would like to do next. Type \"help\" for a list of available commands! ").lower()
            match user_input:
                case "exit" | "quit":
                    if help_exit():
                        program_exit = True
                        break
                case "fast":
                    fast_roll()
                    break
                case "bulk":
                    bulk_fast_roll()
                    break
                case "help":
                    help_loop_three()
                case "name":
                    help_name(char_id)
                case "gender":
                    help_gender(char_id)
                case "race":
                    help_race(char_id)
                case "stat" | "stats":
                    help_stat(char_id)
                case "level":
                    help_level(char_id)
                case "weapon":
                    help_weapon(char_id)
                case "armor":
                    help_armor(char_id)
                case "shield":
                    help_shield(char_id)
                case "character":
                    help_character(char_id)
                case "save":
                    help_save(char_id)
                    break
                case _:
                    print("---Command not recognized. Please try again. Type \"help\" for a list of available commands!---")
            
        if program_exit:
            break

if __name__ == "__main__":
        main()