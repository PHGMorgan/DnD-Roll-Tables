import random
import os
import csv
from Character_Classes import *
from variables_page import class_odds_list


exit = False


#Check if saved characters file exists. If it doesn't, create it and write the header.
if os.path.exists("saved_characters.csv"):
    print("Saved characters directory csv file exists!")
else:
    with open("saved_characters.csv", mode="w") as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
        file_writer.writerow(["Character ID", "Name", "Gender", "Race", "Class", "Stats", "Level", "HP"])
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

def class_roll():
    global class_mapping
    return random.choices(list(class_mapping.keys()), weights = class_odds_list, k=1)[0]


def __main__():
    #Have main funciton use global exit variable.
    global exit
    
    #Create user_input variable and prompt user with a quesiton.
    user_input = input("Press Enter to create an NPC character. Type \"quit\" or \"exit\" to exit. ")
    
    #First part of creation loop. Exits program if user input is exit or quit. Otherwise creates a Character class object then displays it.
    if  user_input == "quit" or user_input == "exit":
        exit = True
        return exit
    user_input = "y"
    print("First, roll for a class.")

    #Second part of creation loop. Prompts user to roll for class, and gives option to exit program. Once class is selected, it initializes the appropriate class.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        char_class = class_roll()
        print(f"Character's class is {char_class}.")
        user_input = input("Would you like to reroll this character's class? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            pass
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            char_id = class_mapping[char_class](random.randint(100000, 999999))
            print(char_id)
            user_input = "y"
            break

    #Third part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to reroll this character's name? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.name_roll()
            print(f"This character's name is now {char_id.name}.")
            print(char_id)
            user_input = "y"
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            user_input = "y"
            break

    #Fourth part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to change this character's gender? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.change_gender()
            print(f"This character's gender is now {char_id.get_gender()}.")
            print(char_id)
            user_input = "y"
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            user_input = "y"
            break

    #Fifth part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to reroll this character's race? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.race_roll()
            char_id.stats_compile()
            char_id.roll_hp()
            print(f"This character's race is now {char_id.__char_race__[0]}.")
            print(char_id)
            user_input
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            user_input = "y"
            break

    #Sixth part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to reroll this character's stats? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.stats_roll()
            char_id.stats_compile()
            char_id.roll_hp()
            print(f"This character's stats are now {char_id.__char_stats_dict__}.")
            print(char_id)
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            user_input = "y"
            break

    #Seventh part of creation loop. Checks if character is commoner. If not, prompts user for reroll, and gives option to exit program.
    if char_id.get_class() != "Commoner":
        while user_input == "y" or user_input == "exit" or user_input == "quit":
            user_input = input("Would you like to reroll this character's level? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
            if  user_input == "quit" or user_input == "exit":
                exit = True
                return exit
            if user_input == "y":
                char_id.random_char_level()
                char_id.roll_hp()
                print(f"This character's stats are now {char_id.__char_stats_dict__}.")
                print(char_id)
            if user_input != "y" and user_input != "exit" and user_input != "quit":
                user_input = "y"
                break

    #Final part of creation loop. Displays final character details and prompts user if they would like to save it.
    user_input = input("Would you like to save this character? Press Enter to discard and start over. Type \"y\" for yes. Type \"quit\" or \"exit\" to discard and exit. ")
    if  user_input == "quit" or user_input == "exit":
        exit = True
        return exit
    if user_input == "y":
        with open("saved_characters.csv", mode = "a", newline = "") as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
            file_writer.writerow([char_id.get_char_id(),
                                char_id.get_name(),
                                char_id.get_gender(),
                                char_id.get_race(),
                                char_id.get_stats(),
                                char_id.get_class(),
                                char_id.get_char_level(),
                                char_id.get_hp()
                            ])
            print(char_id)
            print("Character saved!")
        return
    return


if __name__ == "__main__":
    while exit == False:
        __main__()