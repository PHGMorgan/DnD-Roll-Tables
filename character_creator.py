import csv
import os
from program_functions import *


#Check if saved characters file exists. If it doesn't, create it and write the header.
try:
    if os.path.exists("saved_characters.csv"):
        print("Saved characters directory csv file exists!")
    else:
        with open("saved_characters.csv", mode="w") as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
            file_writer.writerow(["Character ID", "Name", "Alignment", "Gender", "Race", "Subrace", "Class", "Subclass", "Languages", "Speed", "Size", "Stats", "Level", "HP", "AC", "Weapon", "Armor", "Shield", "Proficiencies", "Character Features"])
            print("Saved characters directory csv file created!")
except Exception as e:
    print(e)



def main():
    program_exit = False
    loop_reset = False

    # First while loop. Prompts user to start while still enabling the fast, bulk, and help options without advancing the program. Also allows for exit.
    while not program_exit:

        while not program_exit:
            user_input = input(f"Press Enter to start rolling a character! Type \"help\" for a full list of commands. ").lower().strip()
            match user_input:
                case "exit" | "quit":
                    if help_exit():
                        program_exit = True
                        break
                case "fast":
                    fast_roll()
                case "bulk":
                    while True:
                        function_input = input("Please enter the number of characters you would like to roll: ")
                        if function_input == "exit":
                            return help_exit()
                        try:
                            value = int(function_input)
                            break
                        except:
                            print("That is not a valid number. Please enter a valid number to bulk roll.")
                    bulk_fast_roll(value)
                    break
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
            user_input = input(f"Character's class is {char_class}. Would you like to reroll this character's class? Press Enter to continue. Type \"r\" to reroll. Type \"help\" for a full list of commands. ").lower().strip()
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
                    while True:
                        function_input = input("Please enter the number of characters you would like to roll: ")
                        if function_input == "exit":
                            return help_exit()
                        try:
                            value = int(function_input)
                            break
                        except:
                            print("That is not a valid number. Please enter a valid number to bulk roll.")
                    bulk_fast_roll(value)
                    break
                case "help":
                    help_loop_two()
                case "r":
                    char_class = class_roll()
                case "":
                    char_id = class_mapping[char_class](random.randint(100000, 999999))
                    break
                case "class info":
                    print("The available classes are: Artificer, Barbarian, Bard, Cleric, Commoner, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard")
                case (
                    "artificer" | "barbarian" | "bard" | "cleric" | "commoner" | "druid" | "fighter" | 
                    "monk" | "paladin" | "ranger" | "rogue" | "sorcerer" | "warlock" | "wizard"
                ):
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
            user_input = input("Please type what you would like to do next. Type \"help\" for a list of available commands! ").lower().strip()
            match user_input:
                case "exit" | "quit":
                    if help_exit():
                        program_exit = True
                        break
                case "fast":
                    fast_roll()
                    break
                case "bulk":
                    while True:
                        function_input = input("Please enter the number of characters you would like to roll: ")
                        if function_input == "exit":
                            return help_exit()
                        try:
                            value = int(function_input)
                            break
                        except:
                            print("That is not a valid number. Please enter a valid number to bulk roll.")
                    bulk_fast_roll(value)
                    break
                case "help":
                    help_loop_three()
                case "name":
                    help_name(char_id)
                case "enter name":
                    new_name = input("Please enter your character's name: ")
                    help_enter_name(char_id, new_name)
                case "alignment":
                    help_alignment(char_id)
                case "gender":
                    help_gender(char_id)
                case "race":
                    help_race(char_id)
                case (
                    "aarakocra" | "aasimar" | "bugbear" | "centaur" | "changeling" | "dragonborn" | "dwarf" | 
                    "elf" | "fairy" | "firbolg" | "genasi" | "githyanki" | "githzerai" | "gnome" | 
                    "goblin" | "goliath" | "grung" | "halfling" | "harengon" | "hobgoblin" | "human" | 
                    "kenku" | "kobold" | "lizardfolk" | "minotaur" | "orc" | "owlin" | "satyr" | 
                    "shifter" | "tabaxi" | "tiefling" | "tortle" | "triton" | "verdan"
                ):
                    help_race_select(char_id, user_input)
                case "halforc" | "half-orc" | "half orc":
                    char_id.race = HalfOrc()
                case "yuanti" | "yuan-ti" | "yuan ti":
                    char_id.race = YuanTi()
                case "halfelf" | "half-elf" | "half elf":
                    char_id.race = HalfElf()
                case "race info":
                    print("The available races are: Aarakocra, Aasimar, Bugbear, Centaur, Changeling, Dragonborn, Dwarf, Elf, Fairy, Firbolg,") 
                    print("Genasi, Githyanki, Githzerai, Gnome, Goblin, Goliath, Grung, HalfElf, Halfling, Half-Orc, Harengon, Hobgoblin, Human, Kenku,")
                    print("Kobold, Lizardfolk, Minotaur, Orc, Owlin, Satyr, Shifter, Tabaxi, Tiefling, Tortle, Triton, Verdan, Yuan-Ti.")
                    print("Duergar are dwarves. Eladrin, Sea Elf, and Shadar-Kai are elves. Deep Gnomes are gnomes.")
                case "subclass":
                    help_subclass(char_id)
                case "stat" | "stats":
                    help_stat(char_id)
                case "level":
                    help_level(char_id)
                case "select level":
                    while True:
                        function_input = input("Please enter your character level: ")
                        if function_input == "exit":
                            help_exit()
                        try:
                            value = int(function_input)
                            if value > 20 or value < 1:
                                raise Exception(print("Not a valid level. Please enter a level number between 1 and 20."))
                            help_select_level(char_id, value)
                            break
                        except:
                            print("That is not a valid number. Please enter a valid number to change level.")
                case "weapon":
                    help_weapon(char_id)
                case "armor":
                    help_armor(char_id)
                case "shield":
                    help_shield(char_id)
                case "character" | "info":
                    help_character(char_id)
                case "details" | "full":
                    help_details(char_id)
                case "save":
                    help_save(char_id)
                    break
                case _:
                    print("---Command not recognized. Please try again. Type \"help\" for a list of available commands!---")
            
        if program_exit:
            break

if __name__ == "__main__":
        main()