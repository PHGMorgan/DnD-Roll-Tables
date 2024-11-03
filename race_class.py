import random
from variables_page import stat_names_list


class Race:
    def __init__(self):
       self.race_bonus = {}
       self.subrace = self.subrace_roll()
       self.name = self.get_name()
       self.size = self.get_size()
       self.speed = self.get_speed()
       self.get_proficiencies()
       self.get_size()
       self.get_speed()

    def get_race_name(self):
        return self.subrace[0]

    def get_subrace_name(self):
        return self.subrace[1]

    def get_size(self):
        return "Size- Medium"
    
    def get_speed(self):
        return "Walk- 30"
    
    def get_features(self):
        features_list = []
        features_list.extend(self.subrace[3])
        return features_list
    
    def get_race_stats(self, primary_stat, secondary_stat):
        race_stats_update = {}
        if len(self.subrace[2]) > 1:
            if random.choice([0,1]) == 1:
                race_stats = self.subrace[2][1]
                if "custom_stat_1" in race_stats.keys():
                    race_stats_update[primary_stat] = 1
                else:
                    race_stats_update[list(race_stats.keys())[0]] = 1
                if "custom_stat_2" in race_stats.keys():
                    race_stats_update[secondary_stat] = 1
                else:
                    race_stats_update[list(race_stats.keys())[1]] = 1
                if "custom_stat_3" in race_stats.keys():
                    while True:
                        random_stat = random.choice(stat_names_list)
                        if random_stat not in race_stats_update.keys():
                            break
                    race_stats_update[random_stat] = 1
                else:
                    race_stats_update[list(race_stats.keys())[2]] = 1
                race_stats = race_stats_update
                return race_stats
            else:
                race_stats = self.subrace[2][0]
                if "custom_stat_1" in race_stats.keys():
                    race_stats_update[primary_stat] = 2
                else:
                    race_stats_update[list(race_stats.keys())[0]] = 2
                if "custom_stat_2" in race_stats.keys():
                    race_stats_update[secondary_stat] = 1
                else:
                    race_stats_update[list(race_stats.keys())[1]] = 1
                race_stats = race_stats_update
                return race_stats
        race_stats = self.subrace[2][0]
        if "custom_stat_1" in race_stats.keys():
            race_stats[primary_stat] = race_stats["custom_stat_1"]
            race_stats.pop("custom_stat_1")
        if "custom_stat_2" in race_stats.keys():
            race_stats[secondary_stat] = race_stats["custom_stat_2"]
            race_stats.pop("custom_stat_2")
        if "custom_stat_3" in race_stats.keys():
            while True:
                random_stat = random.choice(stat_names_list)
                if random_stat not in race_stats.keys():
                    break
            race_stats[random_stat] = race_stats["custom_stat_3"]
            race_stats.pop("custom_stat_3")
        return race_stats
    
    def get_proficiencies(self):
        return []
    
    def tough_flag(self):
        return (False, 0)



class Aarakocra(Race):
    def __init__(self):
        self.aarakocra_subrace_list = [
            ("Aarakocra", "Aarakocra", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Flight", "Talons", "Wind Caller", "Languages- Common/Other")),
            ("Aarakocra", "Aarakocra", [{"DEX": 2, "WIS": 1}], ("Flight", "Talons", "Languages- Common/Aarakocra/Auran"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.aarakocra_subrace_list)

    def get_speed(self):
        if self.subrace == self.aarakocra_subrace_list[0]:
            return "Walk- 30, Fly- 30"
        else:
            return "Walk- 25, Fly- 50"



class Aasimar(Race):
    def __init__(self):
        self.aasimar_subrace_list = [
            ("Aasimar", "Aasimar", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), (self.celestial_feature(), "Darkvision- 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Celestial Revelation", self.celestial_revelation(), "Languages- Common/Other")),
            ("Aasimar", "Protector Aasimar", [{"CHA": 2, "WIS": 1}], ("Darkvision- 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Radiant Soul", "Languages- Common/Celestial")),
            ("Aasimar", "Scourge Aasimar", [{"CHA": 2, "CON": 1}], ("Darkvision- 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Radiant Consumption", "Languages- Common/Celestial")),
            ("Aasimar", "Fallen Aasimar", [{"CHA": 2, "STR": 1}], ("Darkvision- 60", "Celestial Resistance", "Healing Hands", "Light Bearer", "Necrotic Shroud", "Languages- Common/Celestial"))
        ]
        super().__init__()
         

    def subrace_roll(self):
        return random.choice(self.aasimar_subrace_list)

    def get_size(self):
        if self.subrace != self.aasimar_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"

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
            ("Bugbear", "Bugbear", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Fey Ancestry", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack", "Languages- Common/Other")),
            ("Bugbear", "Bugbear", [{"STR": 2, "DEX": 1}], ("Darkvision- 60", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack", "Languages- Common/Goblin"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.bugbear_subrace_list)



class Centaur(Race):
    def __init__(self):
        self.centaur_subrace_list = [
            ("Centaur", "Centaur", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Charge", "Equine Build", "Hooves", "Natural Affinity", "Languages- Common/Other")),
            ("Centaur", "Centaur", [{"STR": 2, "WIS": 1}], ("Fey", "Charge", "Hooves", "Equine Build", "Survivor", "Languages- Common/Sylvan"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.centaur_subrace_list)

    def get_speed(self):
        return "Walk- 40"



class Changeling(Race):
    def __init__(self):
        self.changeling_subrace_list = [
            ("Changeling", "Changeling", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Changeling Instincts", "Shapechanger", "Languages- Common/Other")),
            ("Changeling", "Changeling", [{"CHA": 2, "custom_stat_2": 1}], ("Shapechanger", "Changeline Instincts", "Languages- Common/Other/Other"))
        ]
        super().__init__()
    
    def subrace_roll(self):
        return random.choice(self.changeling_subrace_list)

    def get_size(self):
        if self.subrace != self.changeling_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Dragonborn(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 5
    def __init__(self):
        self.dragonborn_color()
        self.chromatic_ancestry()
        self.metallic_ancestry()
        self.gem_ancestry()
        self.dragonborn_subrace_list = [
            ("Dragonborn", f"{self.dragon_color[0]} Dragonborn", [{"STR": 2, "CHA": 1}], (f"Draconic Ancestry- {self.dragon_color[0]} Dragon", f"Breath Weapon- {self.dragon_color[1]} {self.dragon_color[2]}", f"Damage Resistance- {self.dragon_color[1]}", "Languages- Common/Draconic")),
            ("Dragonborn", f"{self.dragon_color[0]} Draconblood Dragonborn", [{"INT": 2, "CHA": 1}], ("Darkvision- 60", "Forceful Presence", f"Draconic Ancestry- {self.dragon_color[0]} Dragon", f"Breath Weapon- {self.dragon_color[1]} {self.dragon_color[2]}", "Languages- Common/Draconic")),
            ("Dragonborn", f"{self.dragon_color[0]} Ravenite Dragonborn", [{"STR": 2, "CON": 1}], ("Darkvision- 60", "Vegeful Assault", f"Draconic Ancestry- {self.dragon_color[0]} Dragon", f"Breath Weapon- {self.dragon_color[1]} {self.dragon_color[2]}", "Languages- Common/Draconic")),
            ("Dragonborn", "Chromatic Dragonborn", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), (f"Chromatic Ancestry- {self.chromatic_color[0]}", "Breath Weapon- 5 by 30ft. line (DEX save)", f"Draconic Resistance- {self.chromatic_color[1]}", "Languages- Common/Other")),
            ("Dragonborn", "Metallic Dragonborn", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), (f"Metallic Ancestry- {self.metallic_color[0]}", "Breath Weapon- 15ft. cone (DEX save)", f"Draconic Resistance- {self.metallic_color[1]}", "Languages- Common/Other")),
            ("Dragonborn", "Gem Dragonborn", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), (f"Gem Ancestry- {self.gem_color[0]}", "Breath Weapon- 15ft. cone (DEX save)", "Psionic Mind", f"Draconic Resistance- {self.gem_color[1]}", "Languages- Common/Other")),
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



class Dwarf(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3
    def __init__(self):
        self.dwarf_subrace_list = [
            ("Dwarf", "Hill Dwarf", [{"CON": 2, "WIS": 1}], ("Darkvision 60", "Dwarven Resilience", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning", "Dwarven Toughnes", "Languages- Common/Dwarvish")),
            ("Dwarf", "Mountain Dwarf", [{"CON": 2, "STR": 1}], ("Darkvision 60", "Dwarven Resilience", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning", "Dwarven Armor Training", "Languages- Common/Dwarvish")),
            ("Dwarf", "Mark of Warding Dwarf", [{"CON": 2, "INT": 1}], ("Darkvision 60", "Dwarven Resilience", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning", "Warder's Intuition", "Wards and Seals", "Spells of the Mark", "Languages- Common/Dwarvish")),
            ("Duergar", "Duergar", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 120", "Dwarven Resilience", "Psionic Fortitude", "Languages- Common/Other")),
            ("Duergar", "Duergar", [{"CON": 2, "STR": 1}], ("Superior Darkvision- 120", "Duergar Resilience", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning", "Sulight Sensitivity", "Languages- Common/Dwarvish"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choices(self.dwarf_subrace_list, weights=[2,2,2,1,1],k=1)[0]

    def get_speed(self):
        if self.subrace == self.dwarf_subrace_list[3]:
            return "Walk- 30"
        return "Walk- 25"
    
    def tough_flag(self):
        if self.subrace == self.dwarf_subrace_list[0]:
            return (True, 1)
        else:
            return (False, 0)
        
    def get_proficiencies(self):
        if self.subrace == self.dwarf_subrace_list[1]:
            return ["light armor", "medium armor"]
        elif self.subrace == self.dwarf_subrace_list[4]:
            return ["battleaxe", "handaxe", "light hammer", "warhammer"]
        else:
            return []



class Elf(Race):
    def __init__(self):
        self.eladrin_season()
        self.elf_subrace_list = [
            ("Elf", "Dark Elf", [{"DEX": 2, "CHA": 1}], ("Superior Darkvision- 120", "Sunlight Sensitivity", "Drow Magic", "Drow Weapon Training", "Fey Ancestry", "Trance", "Keen Senses", "Languages- Common/Elven")),
            ("Elf", "High Elf", [{"DEX": 2, "INT": 1}], ("Darkvision- 60", "Cantrip", "Elf Weapon Training", "Extra Language", "Fey Ancestry", "Trance", "Keen Senses", "Languages- Common/Elven/Other")),
            ("Elf", "Wood Elf", [{"DEX": 2, "WIS": 1}], ("Darkvision- 60", "Elf Weapon Training", "Fleet of Foot", "Mask of the Wild", "Fey Ancestry", "Trance", "Keen Senses", "Languages- Common/Elven")),
            ("Elf", "Pallid Elf", [{"DEX": 2, "WIS": 1}], ("Darkvision- 60", "Incisive Sense", "Blessing of the Moonweaver", "Fey Ancestry", "Trance", "Keen Senses", "Languages- Common/Elven")),
            ("Elf", "Mark of Shadow Elf", [{"DEX": 2, "CHA": 1}], ("Darkvision- 60", "Cunning Intuition", "Shape Shadows", "Spells of the Mark", "Fey Ancestry", "Trance", "Keen Senses", "Languages- Common/Elven")),
            ("Eladrin", f"{self.season} Eladrin", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Fey Ancestry", "Fey Step", "Keen Senses", "Trance", "Languages- Common/Other")),
            ("Eladrin", f"{self.season} Eladrin", [{"DEX": 2, "CHA": 1}], ("Darkvision- 60", "Fey Ancestry", "Trance", "Keen Senses", "Fey Step", "Languages- Common/Elven")),
            ("Sea Elf", "Sea Elf", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Child of the Sea", "Fey Ancestry", "Friend of the Sea", "Keen Senses", "Trance", "Languages- Common/Other")),
            ("Sea Elf", "Sea Elf", [{"DEX": 2, "CON": 1}], ("Darkvision- 60", "Fey Ancestry", "Trance", "Keen Senses", "Sea Elf Training", "Child of the Sea", "Friend of the Sea", "Languages- Common/Elven/Aquan")),
            ("Shadar-Kai", "Shadar-Kai", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Blessing of the Raven Queen", "Fey Ancestry", "Keen Senses", "Necrotic Resistance", "Trance", "Languages- Common/Other")),
            ("Shadar-Kai", "Shadar-Kai", [{"DEX": 2, "CON": 1}], ("Darkvision- 60", "Fey Ancestry", "Trance", "Keen Senses", "Necrotic Resistance", "Blessing of the Raven Queen", "Languages- Common/Elven"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choices(self.elf_subrace_list, weights=[3,3,3,3,2,1,1,1,1,1,1], k=1)[0]
        
    def get_proficiencies(self):
        if self.subrace == self.elf_subrace_list[0]:
            return ["rapier", "shorsword", "hand crossbow"]
        elif self.subrace in [self.elf_subrace_list[1], self.elf_subrace_list[2]]:
            return ["longsword", "shortsword", "shortbow", "longbow"]
        elif self.subrace == self.elf_subrace_list[8]:
            return ["spear", "trident", "light crossbow", "net"]
        else:
            return []

    def get_speed(self):
        if self.subrace == self.elf_subrace_list[2]:
            return "Walk- 35"
        elif self.subrace == self.elf_subrace_list[7]:
            return "Walk- 30, Swim- 30"
        else:
            return "Walk- 30"
        
    def eladrin_season(self):
        season_list = ["Autum", "Winter", "Spring", "Summer"]
        self.season = random.choice(season_list)



class Fairy(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        return ("Fairy", "Fairy", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}),("Fairy Magic", "Flight", "Languages- Common/Other"))
        
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 30, Fly- 30"



class Firbolg(Race):
    def __init__(self):
        self.firbolg_subrace_list = [
            ("Firbolg", "Firbolg", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf", "Languages- Common/Other")),
            ("Firbolg", "Firbolg", [{"WIS": 2, "STR": 1}], ("Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf", "Languages- Common/Elvish/Giant"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.firbolg_subrace_list)



class Genasi(Race):
    def __init__(self):
        self.genasi_subrace_list = [
            ("Air Genasi", "Air Genasi", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Unending Breath", "Lightning Resistance", "Mingle with the Wind", "Languages- Common/Other")),
            ("Air Genasi", "Air Genasi", [{"CON": 2, "DEX": 1}], ("Unending Breath", "Mingle with the Wind", "Languages- Common/Primordial")),
            ("Earth Genasi", "Earth Genasi", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Earth Walk", "Merge with Stone", "Languages- Common/Other")),
            ("Earth Genasi", "Earth Genasi", [{"CON": 2, "STR": 1}], ("Earth Walk", "Merge with Stone", "Languages- Common/Primordial")),
            ("Fire Genasi", "Fire Genasi", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Fire Resistance", "Reach to the Blaze", "Languages- Common/Other")),
            ("Fire Genasi", "Fire Genasi", [{"CON": 2, "INT": 1}], ("Darkvision- 60", "Fire Resistance", "Reach to the Blaze", "Languages- Common/Primordial")),
            ("Water Genasi", "Water Genasi", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Acid Reistance", "Amphibious", "Call to the Wave", "Languages- Common/Other")),
            ("Water Genasi", "Water Genasi", [{"WIS": 1}], ("Acid Reistance", "Amphibious", "Call to the Wave", "Languages- Common/Primordial"))
            ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.genasi_subrace_list)
    
    def get_size(self):
        if self.subrace not in [self.genasi_subrace_list[0], self.genasi_subrace_list[2], self.genasi_subrace_list[4], self.genasi_subrace_list[6]]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"
    
    def get_speed(self):
        if self.subrace == self.genasi_subrace_list[0]:
            return "Walk- 35"
        if self.subrace in [self.genasi_subrace_list[6], self.genasi_subrace_list[7]]:
            return "Walk- 30, Swim- 30"
        return "Walk- 30"



class Githyanki(Race):
    def __init__(self):
        self.githyanki_subrace_table = [
            ("Githyanki", "Githyanki", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Astral Knowledge", "Githanki Psionics", "Psychic Resiliance", "Languages- Common/Other")),
            ("Githyanki", "Githyanki", [{"STR": 2, "INT": 1}], ("Decadent Mastery", "Martial Prodigy", "Githyanki Psionics", "Languages- Common/Gith/Other"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.githyanki_subrace_table)
    
    def get_proficiencies(self):
        if self.subrace != self.githyanki_subrace_table[1]:
            return []
        return ["light armor", "medium armor", "shortsword", "longsword", "greatsword"]



class Githzerai(Race):
    def __init__(self):
        self.githzerai_subrace_list = [
            ("Githzerai", "Githzerai", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Githzerai Psionics", "Mental Discipline", "Pychic Resilience", "Languages- Common/Other")),
            ("Githzerai", "Githzerai", [{"WIS": 2, "INT": 1}], ("Mental Discipline", "Githzerai Psionics", "Languages- Common/Gith"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.githzerai_subrace_list)



class Gnome(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3
    def __init__(self):
        self.gnome_subrace_list = [
            ("Gnome", "Forest Gnome", [{"INT": 2, "DEX": 1}], ("Darkvision 60", "Gnome Cunning", "Natural Illuionist", "Speak with Small Beasts", "Languages- Common/Gnomish")),
            ("Gnome", "Rock Gnome", [{"INT": 2, "CON": 1}], ("Darkvision 60", "Gnome Cunning", "Artificer's Lore", "Tinker", "Languages- Common/Gnomish")),
            ("Gnome", "Mark of Scribing Gnome", [{"INT": 2, "CHA": 1}], ("Darkvision 60", "Gnome Cunning", "Gifted Scribe", "Scribe's Insight", "Spells of the Mark", "Languages- Common/Gnomish")),
            ("Deep Gnome", "Deep Gnome", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 120", "Gnomish Magic Resistance", "Svirfneblin Camouflage", "Languages- Common/Other")),
            ("Deep Gnome", "Deep Gnome", [{"INT": 2, "DEX": 1}], ("Superior Darkvision- 120", "Gnome Cunning", "Stone Camouflage", "Languages- Common/Gnomish"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choices(self.gnome_subrace_list, weights=[2,2,2,1,1], k=1)[0]
    
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        if self.subrace != self.gnome_subrace_list[3]:
            return "Walk- 25"
        return "Walk- 30"



class Goblin(Race):
    def __init__(self):
        self.goblin_subrace_list = [
            ("Goblin", "Goblin", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Fey Ancestry", "Fury of the Small", "Nimble Escape", "Languages- Common/Other")),
            ("Goblin", "Goblin", [{"DEX": 2, "CON": 1}], ("Darkvision- 60", "Fury of the Small", "Nimble Escape", "Languages- Common/Goblin")),
            ("Goblin", "Goblin", [{"DEX": 2, "WIS": 1}], ("Darkvision- 60", "Speak with Small Beasts", "Nimble Escape", "Languages- Common/Goblin"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.goblin_subrace_list)
    
    def get_size(self):
        return "Size- Small"



class Goliath(Race):
    def __init__(self):
        self.goliath_subrace_list = [
            ("Goliath", "Goliath", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Little Giant", "Mountain Born", "Stone's Endurance", "Languages- Common/Other")),
            ("Goliath", "Goliath", [{"STR": 2, "CON": 1}], ("Natural Athlete", "Stone's Endurance", "Powerful Build", "Mountian Born", "Languages- Common/Giant"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.goliath_subrace_list)



class Grung(Race):
    def __init__(self):
            super().__init__()

    def subrace_roll(self):
        return ("Grung", "Grung", [{"DEX": 2, "CON": 1}], ("Arboreal Alertness", "Amphibious", "Poison Immunity", "Poisonous Skin", "Standing Leap", "Water Dependency", "Languages- Grung"))
    
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 25, Climb- 25"



class HalfElf(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3 AND 5
    def __init__(self):
        self.heritage()
        self.halfelf_subrace_list = [
            ("Half Elf", "Half Elf", [{"CHA": 2, "custom_stat_1": 1, "custom_stat_2": 1}], ("Darkvision- 60", "Fey Ancestry", f"Half-Elf Versatility: {self.he_heritage}","Languages- Common/Elven/Other")),
            ("Half Elf", "Mark of Detection Half Elf", [{"WIS": 2, "custom_stat_1": 1}], ("Darkvision- 60", "Fey Ancestry", "Deductive Intuition", "Magical Detection", "Spells of the Mark", "Languages- Common/Elven/Other")), #Magical Detection lvl3 see invis
            ("Half Elf", "Mark of Storm Half Elf", [{"CHA": 2, "DEX": 1}], ("Darkvision- 60", "Fey Ancestry", "Windwright's Intuition", "Storm's Boon", "Headwinds", "Spells of the Mark", "Languages- Common/Elven/Other")) #Headwinds lvl3 spell
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.halfelf_subrace_list)

    def heritage(self):
        heritage_list = [
            "Skill Versatility (General)",
            "Elf Weapon Training (High or Wood Elf Heritage)",
            "Cantrip (High Elf Heritage)",
            "Fleet of Foot (Wood Elf Heritage)",
            "Mask of the Wild (Wood Elf Heritage)",
            "Drow Magic (Dark Elf Heritage)", #Drow Magic - spells lvl3 & 5
            "Swim Speed (Aquatic Elf Heritage)"
        ]
        self.he_heritage = random.choice(heritage_list)

    def get_proficiencies(self):
        if self.subrace == self.halfelf_subrace_list[0]:
            if self.he_heritage == "Elf Weapon Training (High or Wood Elf Heritage)":
                return ["Longsword", "Shortsword","Shortbow", "Longbow"]
        return []
            
    def get_speed(self):
        if self.he_heritage == self.halfelf_subrace_list[0]:
            if self.he_heritage == "Fleet of Foot (Wood Elf Heritage)":
                return "Walk- 35"
            elif self.he_heritage == "Swim Speed (Aquatic Elf Heritage)":
                return "Walk-30, Swim- 30"
            else:
                return "Walk- 30"



class Halfling(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3 AND 5
    def __init__(self):
        self.halfling_subrace_list = [
            ("Halfling", "Lightfoot Halfling", [{"DEX": 2, "CHA": 1}], ("Lucky", "Brave", "Nimble", "Naturally Stealthy", "Languages- Common/Halfling")),
            ("Halfling", "Stout Halfling", [{"DEX": 2, "CON": 1}], ("Lucky", "Brave", "Nimble", "Stout Resilience", "Languages- Common/Halfling")),
            ("Halfling", "Ghostwise Halfling", [{"DEX": 2, "WIS": 1}], ("Lucky", "Brave", "Nimble", "Silent Speech", "Languages- Common/Halfling")),
            ("Halfling", "Lotusden Halfling", [{"DEX": 2, "WIS": 1}], ("Lucky", "Brave", "Nimble", "Children of the Woods", "Timberwalk", "Languages- Common/Halfling")), #Children of the Woods - spells lvl3 & 5
            ("Halfling", "Mark of Hospitality Halfling", [{"DEX": 2, "CHA": 1}], ("Lucky", "Brave", "Nimble", "Ever Hospitable", "Innkeeper's Magic", "Spells of the Mark", "Languages- Common/Halfling")),
            ("Halfling", "Mark of Healing Halfling", [{"DEX": 2, "WIS": 1}], ("Lucky", "Brave", "Nimble", "Medical Intuition", "Healing Touch", "Spells of the Mark", "Languages- Common/Halfling")) #Healing Touch - spells lvl3 & 5
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.halfling_subrace_list)
    
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 25"



class HalfOrc(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3
    def __init__(self):
        self.halforc_subrace_list = [
            ("Half Orc", "Half Orc", [{"STR": 2, "CON": 1}], ("Darkvision- 60", "Menacing", "Relentless Endurance", "Savage Attacks", "Languages- Common/Orc")),
            ("Half Orc", "Mark of Finding Half Orc", [{"WIS": 2, "CON": 1}], ("Darkvision- 60", "Hunter's Intuition", "Finder's Magice", "Spells of the Mark", "Languages- Common/Goblin")) #Finder's Magic lvl3
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.halforc_subrace_list)



class Harengon(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        return ("Harengon", "Harengon", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Hare-Trigger", "Leporine Senses", "Lucky Footwork", "Rabbit Hop", "Languages- Common/Other"))
    
    def get_size(self):
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Hobgoblin(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3
    def __init__(self):
        self.hobgoblin_subrace_list = [
            ("Hobgoblin", "Hobgoblin", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Fey Ancestry", "Fey Gift", "Fortune from the Many", "Languages- Common/Other")),  #fey gift lvl3
            ("Hobgoblin", "Hobgoblin", [{"CON": 2, "INT": 1}], ("Darkvision- 60", "Martial Training", "Saving Face", "Languages- Common/Goblin"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.hobgoblin_subrace_list)



class Human(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 3
    def __init__(self):
        self.human_subrace_list = [
            ("Human", "Human", [{"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}], ("Languages- Common/Other")),
            ("Human", "Mark of Finding Human", [{"WIS": 2, "CON": 1}], ("Darkvision- 60", "Hunter's Intuition", "Finder's Magic", "Spells of the Mark", "Languages- Common/Goblin")), #finders magic lvl3
            ("Human", "Mark of Handling Human", [{"WIS": 2, "custom_stat_1": 1}], ("Wild Intuition", "Primal Connection", "The Bigger They Are", "Spells of the Mark", "Languages- Common/Other")), #the bigger they are lvl3
            ("Human", "Mark of Making Human", [{"INT": 2, "custom_stat_1": 1}], ("Artisan's Intuition", "Artisan's Gift", "Spellsmith", "Spells of the Mark", "Languages- Common/Other")),
            ("Human", "Mark of Passage Human", [{"DEX": 2, "custom_stat_1": 1}], ("Intuitive Motion", "Magical Passage", "Spells of the Mark", "Languages- Common/Other")),
            ("Human", "Mark of Sentinel Human", [{"CON": 2, "WIS": 1}], ("Sentinel's Intuition", "Guardian's Shield", "Vigilant Guardian", "Spells of the Mark", "Languages- Common/Other")),
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.human_subrace_list)

    def get_speed(self):
        if self.subrace == self.human_subrace_list[4]:
            return "Walk- 35"
        return "Walk- 30"



class Kenku(Race):
    def __init__(self):
        self.kenku_subrace_list = [
            ("Kenku", "Kenku", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Expert Duplication", "Kenku Recall", "Mimicry", "Languages- Common/Other")),  
            ("Kenku", "Kenku", [{"DEX": 2, "WIS": 1}], ("Expert Forgery", "Kenku Training", "Mimicry", "Languages- Common/Auran"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.kenku_subrace_list)
    
    def get_size(self):
        if self.subrace != self.kenku_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Kobold(Race):
    def __init__(self):
        self.koblegacy()
        self.kobold_subrace_list = [
            ("Kobold", "Kobold", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Draconic Cry", f"Kobold Legacy: {self.kobold_legacy}", "Languages- Common/Other")),  
            ("Kobold", "Kobold", [{"DEX": 2}], ("Darkvision- 60", "Grovel, Cower, and Beg", "Pack Tactics", "Sunlight Sensitivity", "Languages- Common/Draconic")), 
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.kobold_subrace_list)

    def get_size(self):
        return "Size- Small"
    
    def koblegacy(self):
        legacy_list = [
            "Craftiness",
            "Defiance",
            "Dracoic Sorcery"
        ]
        self.kobold_legacy = random.choice(legacy_list)



class Lizardfolk(Race):
    def __init__(self):
        self.lizardfolk_subrace_list = [
            ("Lizardfolk", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Bite", "Hold Breath", "Hungry Jaws", "Natural Armor", "Nature's Intuition", "Languages- Common/Other")), 
            ("Lizardfolk", [{"CON": 2, "WIS": 1}], ("Bite", "Cunning Artisan", "Hold Breath", "Hunter's Lore", "Natural Armor", "Hungry Jaws", "Languages- Common/Draconic"))  
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.lizardfolk_subrace_list)
    
    def get_speed(self):
        return "Walk- 30, Swim- 30"



class Minotaur(Race):
    def __init__(self):
        self.minotaur_subrace_list = [
            ("Minotaur", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Horns", "Goring Rush", "Hammering Horns", "Labyrinthine Recall", "Languages- Common/Other")),
            ("Minotaur", [{"STR": 2, "CON": 1}], ("Horns", "Goring Rush", "Hammering Horns", "Imposing Presence", "Languages- Common/Minotaur"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.minotaur_subrace_list)



class Orc(Race):
    def __init__(self):
        self.orc_subrace_list = [
            ("Orc", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Adrenaline Rush", "Powerful Build", "Relentless Endurance", "Languages- Common/Other")),
            ("Orc", [{"STR": 2, "CON": 1}], ("Darkvision- 60", "Aggressive", "Primal Intuition", "Powerful Build", "Languages- Common/Orc")),  
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.orc_subrace_list)



class Owlin(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        return ("Owlin", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 120", "Flight", "Silent Feathers", "Languages- Common/Other"))
    
    def get_size(self):
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 30, Fly- 30"



class Satyr(Race):
    def __init__(self):
        self.satyr_subrace_list = [
            ("Satyr", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Ram", "Magic Resistance", "Mirthful Leaps", "Reveler", "Languages- Common/Other")), 
            ("Satyr", [{"CHA": 2, "DEX": 1}], ("Ram", "Magic Resistance", "Mirthful Leaps", "Reveler", "Languages- Common/Sylvan")) 
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.satyr_subrace_list)
    
    def get_speed(self):
        return "Walk- 35"



class Shifter(Race):
    def __init__(self):
        self.ancestor()
        self.shifter_subrace_list = [
            ("Shifter", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Bestial Instincts", f"Shifting- {self.ancestor_lycan[0]}", "Languages- Common/Other")),
            ("Shifter", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Keen Senses", "Shifting","Subrace", "Languages- Common")),
            ("Beasthide Shifter", [{"CON": 2, "STR": 1}], ("Darkvision- 60", "Keen Senses", "Shifting","Subrace", "Natural Athlete", "Shifting Feature", "Languages- Common/Other")),
            ("Longtooth Shifter", [{"STR": 2, "DEX": 1}], ("Darkvision- 60", "Bestial Instincts", "Shifting", "Fierce", "Shifting Feature", "Languages- Common/Other")),
            ("Swiftstride Shifter", [{"DEX": 2, "CHA": 1}], ("Darkvision- 60", "Bestial Instincts", "Shifting", "Graceful", "Shifting Feature", "Languages- Common/Other")),  
            ("Wildhunt Shifter", [{"WIS": 2}], ("Darkvision- 60", "Bestial Instincts", "Shifting", "Mark the Scent", "Shifting Feature", "Languages- Common/Other"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.shifter_subrace_list)
    
    def ancestor(self):
        lycanthrope_list = [
            ("Werebear", "Beasthide"),
            ("Wereboar", "Beasthide"),
            ("Wererat", "Swiftstride"),
            ("Weretiger", "Swiftstride"),
            ("Werewolf (Wolflike)", "Longtooth"),
            ("Werewolf (Doglike)", "Wildhunt")
        ]
        self.ancestor_lycan = random.choice(lycanthrope_list)



class Tabaxi(Race):
    def __init__(self):
        self.tabaxi_subrace_list =[
            ("Tabaxi", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Cat's Claws", "Cat's Talent", "Feline Agility", "Languages- Common/Other")),
            ("Tabaxi", [{"DEX": 2, "CHA": 1}], ("Darkvision- 60", "Cat's Claws", "Cat's Talent", "Feline Agility", "Languages- Common/Other"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.tabaxi_subrace_list)
    
    def get_speed(self):
        if self.subrace == self.tabaxi_subrace_list[0]:
            return "Walk- 30, Climb- 30"
        return "Walk- 30"

    def get_size(self):
            if self.subrace != self.tabaxi_subrace_list[0]:
                return "Size- Medium"
            if random.choice([0,1]) == 1:
                return "Size- Medium"
            return "Size- Small"



class Tiefling(Race):
    def __init__(self):
        self.tiefling_subrace_list = [
            ("Bloodline of Asmodeus Tiefling", [{"CHA": 2, "INT": 1}], ("Darkvision- 60", "Hellish Resistance", "Infernal Legacy", "Languages- Common/Infernal")),
            ("Bloodline of Baalzebul Tiefling", [{"CHA": 2, "INT": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Maladomini", "Languages- Common/Infernal")),
            ("Bloodline of Dispater Tiefling", [{"CHA": 2, "DEX": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Dis", "Languages- Common/Infernal")),
            ("Bloodline of Fierna Tiefling", [{"CHA": 2, "WIS": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Phlegethos", "Languages- Common/Infernal")),
            ("Bloodline of Glasya Tiefling", [{"CHA": 2, "DEX": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Malbolge", "Languages- Common/Infernal")),
            ("Bloodline of Levistus Tiefling", [{"CHA": 2, "CON": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Stygia", "Languages- Common/Infernal")),
            ("Bloodline of Mammon Tiefling", [{"CHA": 2, "INT": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Minauros", "Languages- Common/Infernal")),
            ("Bloodline of Mephistopheles Tiefling", [{"CHA": 2, "INT": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Cania", "Languages- Common/Infernal")),
            ("Bloodline of Zariel Tiefling", [{"CHA": 2, "STR": 1}], ("Darkvision- 60", "Hellish Resistance", "Legacy of Avernus", "Languages- Common/Infernal"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.tiefling_subrace_list)



class Tortle(Race):
    def __init__(self):
        self.tortle_subrace_list = [
            ("Tortle", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Claws", "Hold Breath", "Natural Armor", "Nature's Intuition", "Shell Defense", "Languages- Common/Other")),  
            ("Tortle", [{"STR": 2, "WIS": 1}], ("Claws", "Hold Breath", "Natural Armor", "Shell Defense","Survival Instinct", "Languages- Common/Aquan"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.tortle_subrace_list)
    
    def get_size(self):
        if self.subrace != self.tortle_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Triton(Race):
    def __init__(self):
        self.triton_subrace_list = [
            ("Triton", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardians of the Depths", "Languages- Common/Other")),  
            ("Triton", [{"STR": 1, "CON": 1, "CHA": 1}], ("Darkvision- 60", "Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardians of the Depths", "Languages- Common/Primordial"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.triton_subrace_list)
    
    def get_speed(self):
        return "Walk- 30, Swim- 30"



class Verdan(Race): # COME BACK TO THIS RACE SINCE IT HAS A FEATURE THAT ONLY COMES ONLINE AT LEVEL 5
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        return ("Verdan", [{"CHA": 2, "CON": 1}], ("Black Blood Healing", "Limited Telepathy", "Persuasive", "Telepathic Insight" ,"Languages- Common/Goblin/Other"))



class YuanTi(Race):
    def __init__(self):
        self.yuanti_subrace_list = [
            ("Yuan-Ti", ({"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}), ("Darkvision- 60", "Magic Resistance", "Poison Resilience", "Serpentine Spellcasting" ,"Languages- Common/Other")),
            ("Yuan-Ti", [{"CHA": 2, "INT": 1}], ("Darkvision- 60", "Innate Spellcasting", "Magic Resistance", "Poison Immunity","Languages- Common/Abyssal/Draconic"))
        ]
        super().__init__()

    def subrace_roll(self):
        return random.choice(self.yuanti_subrace_list)

    def get_size(self):
        if self.subrace != self.yuanti_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"