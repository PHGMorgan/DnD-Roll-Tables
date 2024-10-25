import random
import os
import csv


exit = False

#Check if saved characters file exists. If it doesn't, create it and write the header.
if os.path.exists("saved_characters.csv"):
    print("Saved characters directory csv file exists!")
else:
    with open("saved_characters.csv", mode="w") as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ",", quotechar = '"')
        file_writer.writerow(["Character ID", "Name", "Race", "Stats", "Class"])
        print("Saved characters directory csv file created!")


#Create the global names list variable from the data in the names.csv file.
names_list = []
with open("names.csv", mode = "r", newline = "") as namefile:
    file_reader = csv.reader(namefile)
    for row in file_reader:
        names_list.append(row[0])


class Character:
    def __init__(self, char_id):
        self.__char_stats_dict__ = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.__char_race__ = None
        self.__rolls_for_stats__ = []
        self.char_id = char_id
        self.name_roll()
        self.race_roll()
        self.stats_roll()
        self.stats_compile()
        self.class_roll()
    
    def name_roll(self):
        global names_list
        self.name = random.choices(names_list, k=1)[0]

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
        self.__char_race__ = random.choices(races_list, k = 1)[0]

    def stats_roll(self):
        self.__rolls_for_stats__ = []
        for i in range(6):
            stat_roll = self.four_six_drop_low()
            self.__rolls_for_stats__.append(stat_roll)

    def four_six_drop_low(self):
        rolls_list = []
        for i in range(4):
            rolls_list.append(random.randint(1, 6))
        rolls_list.remove(min(rolls_list))
        return rolls_list[0] + rolls_list[1] + rolls_list[2]

    def stats_compile(self):
        self.__char_stats_dict__["STR"] = self.__rolls_for_stats__[0]
        self.__char_stats_dict__["DEX"] = self.__rolls_for_stats__[1]
        self.__char_stats_dict__["CON"] = self.__rolls_for_stats__[2]
        self.__char_stats_dict__["INT"] = self.__rolls_for_stats__[3]
        self.__char_stats_dict__["WIS"] = self.__rolls_for_stats__[4]
        self.__char_stats_dict__["CHA"] = self.__rolls_for_stats__[5]
        race_bonus_dict = self.__char_race__[1]
        for race_bonus in race_bonus_dict:
            if race_bonus in self.__char_stats_dict__:
                self.__char_stats_dict__[race_bonus] += race_bonus_dict[race_bonus]
                
    def class_roll(self):
        classes_list = [
            "Wizard",
            "Fighter",
            "Sorcerer",
            "Barbarian",
            "Cleric",
            "Rogue"
        ]
        self.char_class = random.choices(classes_list, k = 1)[0]

    def __str__(self):
        return (
            f"Character name: {self.name} \n"
            f"Character race: {self.__char_race__[0]} \n"
            f"Character stats: {self.__char_stats_dict__} \n"
            f"Character class: {self.char_class} \n"
        )


     
def __main__():
    #Have main funciton use global exit variable.
    global exit
    
    #Create user_input variable and prompt user with a quesiton.
    user_input = input("Press Enter to create an NPC character. Type \"quit\" or \"exit\" to exit. ")
    
    #First part of creation loop. Exits program if user input is exit or quit. Otherwise creates a Character class object then displays it.
    if  user_input == "quit" or user_input == "exit":
        exit = True
        return exit
    char_id = int(random.random() * 100000)
    char_id = Character(char_id)
    print(char_id)
    user_input = "y"

    #Second part of creation loop. Prompts user for reroll, and gives option to exit program.
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

    #Third part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to reroll this character's race? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.race_roll()
            char_id.stats_compile()
            print(f"This character's race is now {char_id.__char_race__[0]}.")
            print(char_id)
            user_input
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            user_input = "y"
            break

    #Fourth part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to reroll this character's stats? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.stats_roll()
            char_id.stats_compile()
            print(f"This character's stats are now {char_id.__char_stats_dict__}.")
            print(char_id)
        if user_input != "y" and user_input != "exit" and user_input != "quit":
            user_input = "y"
            break

    #Fifth part of creation loop. Prompts user for reroll, and gives option to exit program.
    while user_input == "y" or user_input == "exit" or user_input == "quit":
        user_input = input("Would you like to reroll this character's class? Press Enter to continue. Type \"y\" to reroll. Type \"quit\" or \"exit\" to exit. ")
        if  user_input == "quit" or user_input == "exit":
            exit = True
            return exit
        if user_input == "y":
            char_id.class_roll()
            print(f"This character's class is now {char_id.char_class}.")
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
            file_writer.writerow([char_id.char_id, char_id.name, char_id.__char_race__[0], char_id.__char_stats_dict__, char_id.char_class])
            print(char_id)
            print("Character saved!")
        return
    return


if __name__ == "__main__":
    while exit == False:
        __main__()