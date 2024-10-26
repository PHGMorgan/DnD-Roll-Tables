import random
import csv


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
        '''
        self.stats_roll()
        self.stats_compile()
        '''


    #Block of get functions
    def get_char_id(self):
        return self.__char_id__
    
    def get_name(self):
        return self.__name__
    
    def get_gender(self):
        return self.__gender__
    
    def get_race(self):
        return self.__char_race__
    
    def get_class(self):
        return self.__char_class__

    def get_stats(self):
        return self.__char_stats_dict__
    
    
    #Create the global names list variable from the data in the names.csv file.
    def name_roll(self):
        names_list = []
        with open("names.csv", mode = "r", newline = "") as namefile:
            file_reader = csv.reader(namefile)
            for row in file_reader:
                names_list.append(row[0])
        self.name = random.choices(names_list, k=1)[0]
    
    def random_gender(self):
        char_sex = random.randint(1, 2)
        if char_sex == 1:
            self.__gender__ = "Male"
        else:
            self.__gender__ = "Female"

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
        self.rolls_for_stats = []
        for i in range(6):
            stat_roll = self.four_six_drop_low()
            self.rolls_for_stats.append(stat_roll)

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

    def __str__(self):
        return (
            f"Character name: {self.__name__} \n"
            f"Character gender: {self.__gender__} \n"
            f"Character race: {self.__char_race__[0]} \n"
            f"Character class: {self.__char_class__} \n"
            f"Character stats: {self.__char_stats_dict__} \n"
        )



class Artificer(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Artificer"

class Barbarian(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Barbarian"

class Bard(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Bard"

class Cleric(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Cleric"

class Commoner(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Commoner"

class Druid(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Druid"

class Fighter(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Fighter"

class Monk(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Monk"

class Paladin(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Paladin"

class Ranger(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Ranger"

class Rogue(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Rogue"

class Sorcerer(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Sorcerer"

class Warlock(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Warlock"

class Wizard(Character):
    def __init__(self, char_id):
        super().__init__(char_id)
        self.__char_class__= "Wizard"