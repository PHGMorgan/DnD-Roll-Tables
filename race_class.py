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
        if race_stats.get("custom_stat_1", False) == 2:
            race_stats = {primary_stat: 2, list(race_stats.keys())[1]: list(race_stats.values())[1]}
        if race_stats.get("custom_stat_2", False) == 1:
            race_stats = {list(race_stats.keys())[0]: list(race_stats.values())[0], secondary_stat: 1}
        return race_stats



class Aarakocra(Race):
    def __init__(self):
        self.aarakocra_subrace_list = [
            ("Aarakocra", {"custom_stat_1": 2, "custom_stat_2": 1}, ("Flight: 30", "Talons", "Wind Caller", "Languages: Common/Other")),
            ("Aarakocra", {"DEX": 2, "WIS": 1}, ("Flight: 50", "Talons", "Languages: Common/Aarakocra/Auran"))
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
            ("Aasimar", {"custom_stat_1": 2, "custom_stat_2": 1}, (self.celestial_feature(), "Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Celestial Revelation", self.celestial_revelation(), "Languages: Common/Other")),
            ("Protector Aasimar", {"CHA": 2, "WIS": 1}, ("Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Radiant Soul", "Languages: Common/Celestial")),
            ("Scourge Aasimar", {"CHA": 2, "CON": 1}, ("Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Radiant Consumption", "Languages: Common/Celestial")),
            ("Fallen Aasimar", {"CHA": 2, "STR": 1}, ("Darkvision: 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Necrotic Shroud", "Languages: Common/Celestial"))
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
            ("Bugbear", {"custom_stat_1": 2, "custom_stat_2": 1}, ("Darkvision: 60", "Fey Ancestry", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack", "Languages: Common/Other")),
            ("Bugbear", {"STR": 2, "DEX": 1}, "Darkvision: 60", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack", "Languages: Common/Goblin")
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.bugbear_subrace_list)
    
class Centaur(Race):
    def __init__(self):
        self.centaur_subrace_list = [
            ("Centaur", {"custom_stat_1": 2, "custom_stat_2": 1}, ("Charge", "Equine Build", "Hooves", "Natural Affinity", "Languages: Common/Other")),
            ("Centaur", {"STR": 2, "WIS": 1}, ("Fey", "Charge", "Hooves", "Equine Build", "Survivor", "Languages: Common/Sylvan"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.centaur_subrace_list)

    def get_speed(self):
        return "Speed: 40"

class Changeling(Race):
    def __init__(self):
        self.changeling_subrace_list = [
            ("Changeling", {"custom_stat_1": 2, "custom_stat_2": 1}, ("Changeling Instincts", "Shapechanger", "Languages: Common/Other")),
            ("Changeling", {"CHA": 2, "custom_stat_2": 1}, ("Shapechanger", "Changeline Instincts", "Languages: Common/Other/Other"))
        ]
        super().__init__()
    
    def subrace_roll(self):
        return random.choice(self.changeling_subrace_list)

    def get_size(self):
        if self.subrace != self.changeling_subrace_list[0]:
            return "Size: Medium"
        if random.choice([0,1]) == 1:
            return "Size: Medium"
        return "Size: Small"
    
class Dragonborn(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 5
    def __init__(self):
        self.dragonborn_color()
        self.chromatic_ancestry()
        self.metallic_ancestry()
        self.gem_ancestry()
        self.dragonborn_subrace_list = [
            (f"{self.dragon_color[0]} Dragonborn", {"STR": 2, "CHA": 1}, (f"Draconic Ancestry: {self.dragon_color[0]} Dragon", f"Breath Weapon: {self.dragon_color[1]} {self.dragon_color[2]}", f"Damage Resistance: {self.dragon_color[1]}", "Languages: Common/Draconic")),
            (f"{self.dragon_color[0]} Draconblood Dragonborn", {"INT": 2, "CHA": 1}, ("Darkvision: 60", "Forceful Presence", f"Draconic Ancestry: {self.dragon_color[0]} Dragon", f"Breath Weapon: {self.dragon_color[1]} {self.dragon_color[2]}", "Languages: Common/Draconic")),
            (f"{self.dragon_color[0]} Ravenite Dragonborn", {"STR": 2, "CON": 1}, ("Darkvision: 60", "Vegeful Assault", f"Draconic Ancestry: {self.dragon_color[0]} Dragon", f"Breath Weapon: {self.dragon_color[1]} {self.dragon_color[2]}", "Languages: Common/Draconic")),
            ("Chromatic Dragonborn", {"custom_stat_1": 2, "custom_stat_2": 1}, (f"Chromatic Ancestry: {self.chromatic_color[0]}", "Breath Weapon: 5 by 30ft. line (DEX save)", f"Draconic Resistance: {self.chromatic_color[1]}", "Languages: Common/Other")),
            ("Metallic Dragonborn", {"custom_stat_1": 2, "custom_stat_2": 1}, (f"Metallic Ancestry: {self.metallic_color[0]}", "Breath Weapon: 15ft. cone (DEX save)", f"Draconic Resistance: {self.metallic_color[1]}", "Languages: Common/Other")),
            ("Gem Dragonborn", {"custom_stat_1": 2, "custom_stat_2": 1}, (f"Gem Ancestry: {self.gem_color[0]}", "Breath Weapon: 15ft. cone (DEX save)", "Psionic Mind", f"Draconic Resistance: {self.gem_color[1]}", "Languages: Common/Other")),
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.dragonborn_subrace_list)

    def dragonborn_color(self):
        color_list = [
            ("Black", "Acid", "5 by 30 ft. line (DEX save)"),
            ("Blue", "Lightning", "5 by 30 ft. line (DEX save)"),
            ("Brass", "Fire", "5 by 30 ft. line (DEX save)"),
            ("Bronze", "Lightning", "5 by 30 ft. line (DEX save)"),
            ("Copper", "Acid", "5 by 30 ft. line (DEX save)"),
            ("Gold", "Fire", "15 ft. cone (DEX save)"),
            ("Green", "Poison", "15 ft. cone (CON save)"),
            ("Red", "Fire", "15 ft. cone (DEX save)"),
            ("Silver", "Cold", "15 ft. cone (CON save)"),
            ("White", "Cold", "15 ft. cone (CON save)")
        ]
        self.dragon_color = random.choice(color_list)

    def chromatic_ancestry(self):
        color_list = [
            ("Black", "Acid"),
            ("Blue", "Lightning"),
            ("Green", "Poison"),
            ("Red", "Fire"),
            ("White", "Cold")
        ]
        self.chromatic_color = random.choice(color_list)

    def metallic_ancestry(self):
        color_list = [
            ("Brass", "Fire"),
            ("Bronze", "Lightning"),
            ("Copper", "Acid"),
            ("Gold", "Fire"),
            ("Silver", "Cold")
        ]
        self.metallic_color = random.choice(color_list)

    def gem_ancestry(self):
        color_list = [
            ("Amethyst", "Force"),
            ("Crystal", "Radiant"),
            ("Emerald", "Psychic"),
            ("Sapphire", "Thunder"),
            ("Topaz", "Necrotic")
        ]
        self.gem_color = random.choice(color_list)



#[("Name", {"custom_stat_1": 2, "custom_stat_2": 1}, ("Languages: ")), ("Name", {"stat": number, "stat": number}, ("Languages: "))]

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