import random


class Race:
    def __init__(self):
       self.race_bonus = {}
       self.subrace = self.subrace_roll()
       self.name = self.get_name()
       self.size = self.get_size()
       self.speed = self.get_speed()
       self.race_features = self.get_features()

    def get_name(self):
        return self.subrace[0]

    def get_size(self):
        return "Size: Medium"
    
    def get_speed(self):
        return "Speed: 30"
    
    def get_features(self):
        features_list = [self.size, self.speed]
        features_list.extend(self.subrace[2])
        return features_list
    
    def get_race_stats(self, primary_stat, secondary_stat):
        race_stats = self.subrace[1]
        if race_stats.get("custom_stats", False):
            self.race_bonus[primary_stat] = race_stats["custom_stat_1"]
            self.race_bonus[secondary_stat] = race_stats["custom_stat_2"]
        else:
            self.race_bonus = self.subrace[1]
        return self.race_bonus



class Aarakocra(Race):
    def __init__(self):
        self.aarakocra_subrace_list = [
            ("Aarakocra", {"custom_stats": True, "custom_stat_1": 2, "custom_stat_2": 1}, ("Flight: 30", "Talons", "Wind Caller", "Languages: Common/Other")),
            ("Aarakocra", {"custom_stats": False, "DEX": 2, "WIS": 1}, ("Flight: 50", "Talons", "Languages: Common/Aarakocra/Auran"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.aarakocra_subrace_list)

    def get_speed(self):
        if self.subrace == self.aarakocra_subrace_list[0]:
            return "Speed: 30"
        else:
            return "Speed: 25"



class Aasimar(Race):
    def __init__(self):
        self.aasimar_subrace_list = [
            ("Aasimar", {"custom_stats": True, "custom_stat_1": 2, "custom_stat_2": 1}, (self.celestial_feature(), "Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Celestial Revelation", self.celestial_revelation(), "Languages: Common/Other")),
            ("Protector Aasimar", {"custom_stats": False, "CHA": 2, "WIS": 1}, ("Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Radiant Soul", "Languages: Common/Celestial")),
            ("Scourge Aasimar", {"custom_stats": False, "CHA": 2, "CON": 1}, ("Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Radiant Consumption", "Languages: Common/Celestial")),
            ("Fallen Aasimar", {"custom_stats": False, "CHA": 2, "STR": 1}, ("Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Necrotic Shroud", "Languages: Common/Celestial"))
        ]
        super().__init__()
         

    def subrace_roll(self):
        return random.choice(self.aasimar_subrace_list)

    def get_size(self):
        if self.subrace != self.aasimar_subrace_list[0]:
            return "Size: Medium"
        if random.choice([0,1]) == 1:
            return "Size: Medium"
        return "Size: Small"

    def celestial_feature(self):
        function_list = [
            "A dusting of metallic, white, or charcoal freckles",
            "Metallic, luminous, or dark eyes",
            "Starkly colored hair",
            "An unusual hue tinting your shadow",
            "A ghostly halo crowning your head",
            "Rainbows gleaming on your skin"
        ]
        return random.choice(function_list)
    
    def celestial_revelation(self):
        function_list = [
            "Necrotic Shroud",
            "Radiant Consumption",
            "Radiant Soul"
        ]
        return random.choice(function_list)
    


class Bugbear(Race):
    def __init__(self):
        self.bugbear_subrace_list = [
            ("Bugbear", {"custom_stats": True, "custom_stat_1": 2, "custom_stat_2": 1}, ("Darkvision: 60", "Fey Ancestry", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack", "Languages: Common/Other")),
            ("Bugbear", {"custom_stats": False, "STR": 2, "DEX": 1}, "Darkvision: 60", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack", "Languages: Common/Goblin")
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.bugbear_subrace_list)
    
class Centaur(Race):
    def __init__(self):
        self.centaur_subrace_list = [
            ("Centaur", {"custom_stats": True, "custom_stat_1": 2, "custom_stat_2": 1}, ("Charge", "Equine Build", "Hooves", "Natural Affinity", "Languages: Common/Other")),
            ("Centaur", {"custom_stats": False, "STR": 2, "WIS": 1}, ("Fey", "Charge", "Hooves", "Equine Build", "Survivor", "Languages: Common/Sylvan"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.centaur_subrace_list)

    def get_speed(self):
        return "Speed: 40"

#class Changeling(Race):
#class Dragonborn(Race):
#class Dwarf(Race): (Duergar too)
#class Elf(Race): (Eladrin,	Sea Elf, Shadar-Kai too)
#class Fairy(Race):
#class Firbolg(Race):
#class Genasi(Race):
#class Githyanki(Race):
#class Githzerai(Race):
#class Gnome(Race): (Deep Gnome too)
#class Goblin(Race):
#class Goliath(Race):
#class Grung(Race):
#class Half-Elf(Race):
#class Halfling(Race):
#class Half-Orc(Race):
#class Harengon(Race):
#class Hobgoblin(Race):
#class Human(Race):
#class Kenku(Race):
#class Kobold(Race):
#class Lizardfolk(Race):
#class Minotaur(Race):
#class Orc(Race):
#class Owlin(Race):
#class Satyr(Race):
#class Shifter(Race):
#class Tabaxi(Race):
#class Tiefling(Race):
#class Tortle(Race):
#class Triton(Race):
#class Verdan(Race):
#class Yuan-Ti(Race):