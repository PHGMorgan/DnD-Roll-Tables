import random
from variables_page import *

def replace_placeholder(roll_list, replacement):
    for index, item in enumerate(roll_list):
        if isinstance(item, list):
            for i, nested_item in enumerate(item):
                if isinstance(nested_item, list):
                    if nested_item[1] == "Placeholder":
                        roll_list[index][i][1] = replacement
                        return roll_list
        elif item == "Placeholder":
                roll_list[index] = replacement
                return roll_list
    return roll_list

class Race:
    def __init__(self):
       self.race_bonus = {}
       self.subrace = self.subrace_roll()
       self.size = self.get_size()
       self.speed = self.get_speed()

    def get_race_name(self):
        return self.subrace[0]

    def get_subrace_name(self):
        if self.subrace[0] == self.subrace[1]:
            self.subrace[1] = "None"
            return self.subrace[0]
        elif self.subrace[1] == "None":
            return self.subrace[0]
        return self.subrace[1]
    
    def get_true_subrace(self):
        return self.subrace[1]

    def get_size(self):
        return "Size- Medium"
    
    def get_speed(self):
        return "Walk- 30"
    
    def get_languages(self):
        return []
    
    def get_features(self):
        features_list = []
        features_list.extend(self.subrace[3])
        return features_list
    
    def get_proficiencies(self):
        return []
    
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
    
    def tough_flag(self):
        return (False, 0)



class Aarakocra(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(aarakocra_subrace_list)
        self.subrace_check = roll
        return roll

    def get_speed(self):
        if self.subrace_check == aarakocra_subrace_list[0]:
            return "Walk- 30, Fly- 30"
        else:
            return "Walk- 25, Fly- 50"
        
    def get_languages(self):
        if self.subrace_check == aarakocra_subrace_list[0]:
            return ["Common", "Other"]
        else:
            return ["Common", "Aarakocra", "Auran"]



class Aasimar(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(aasimar_subrace_list)
        self.subrace_check = roll
        if roll == aasimar_subrace_list[0]:
            cel_feat = self.celestial_feature()
            cel_rev = self.celestial_revelation()
            roll = replace_placeholder(roll, f"Celestial Feature: {cel_feat}")
            roll = replace_placeholder(roll, f"Celestial Revelation: {cel_rev}")
        return roll

    def get_size(self):
        if self.subrace_check != aasimar_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"
    
    def get_languages(self):
        if self.subrace_check in [aasimar_subrace_list[1], aasimar_subrace_list[2], aasimar_subrace_list[3]]:
            return ["Common", "Celestial"]
        else:
            return ["Common", "Other"]

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
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(bugbear_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == bugbear_subrace_list [0]:
            return ["Common", "Other"]
        else:
            return ["Common", "Goblin"]



class Centaur(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(centaur_subrace_list)
        self.subrace_check = roll
        return roll

    def get_speed(self):
        return "Walk- 40"
    
    def get_languages(self):
        if self.subrace_check == centaur_subrace_list [0]:
            return ["Common", "Other"]
        else:
            return ["Common", "Sylvan"]



class Changeling(Race):
    def __init__(self):
        super().__init__()
    
    def subrace_roll(self):
        roll = random.choice(changeling_subrace_list)
        self.subrace_check = roll
        return roll

    def get_size(self):
        if self.subrace_check != changeling_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"
    
    def get_languages(self):
        if self.subrace_check == changeling_subrace_list[0]:
            return ["Common", "Other"]
        else:
            return ["Common", "Other", "Other"]



class Dragonborn(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(dragonborn_subrace_list)
        self.subrace_check = roll
        if roll == dragonborn_subrace_list[0]:
            color = self.dragonborn_color()
            roll = replace_placeholder(roll, f"{color[0]} Dragonborn")
            roll = replace_placeholder(roll, f"Draconic Ancestry- {color[0]} Dragon")
            roll = replace_placeholder(roll, f"Breath Weapon- {color[1]} {color[2]}")
            roll = replace_placeholder(roll, f"Damage Resistance- {color[1]}")
            return roll
        elif roll == dragonborn_subrace_list[1]:
            color = self.dragonborn_color()
            roll = replace_placeholder(roll, f"{color[0]} Draconblood Dragonborn")
            roll = replace_placeholder(roll, f"Draconic Ancestry- {color[0]} Dragon")
            roll = replace_placeholder(roll, f"Breath Weapon- {color[1]} {color[2]}")
            return roll
        elif roll == dragonborn_subrace_list[2]:
            color = self.dragonborn_color()
            roll = replace_placeholder(roll, f"{color[0]} Ravenite Dragonborn")
            roll = replace_placeholder(roll, f"Draconic Ancestry- {color[0]} Dragon")
            roll = replace_placeholder(roll, f"Breath Weapon- {color[1]} {color[2]}")
            return roll
        elif roll == dragonborn_subrace_list[3]:
            color = self.chromatic_ancestry()
            roll = replace_placeholder(roll, f"Chromatic Ancestry- {color[0]}")
            roll = replace_placeholder(roll, f"Draconic Resistance- {color[1]}")
            return roll
        elif roll == dragonborn_subrace_list[4]:
            color = self.metallic_ancestry()
            roll = replace_placeholder(roll, f"Metallic Ancestry- {color[0]}")
            roll = replace_placeholder(roll, f"Draconic Resistance- {color[1]}")
            return roll
        else:
            color = self.gem_ancestry()
            roll = replace_placeholder(roll, f"Gem Ancestry- {color[0]}")
            roll = replace_placeholder(roll, f"Draconic Resistance- {color[1]}")
            return roll

    def get_languages(self):
        if self.subrace_check in [dragonborn_subrace_list[0], dragonborn_subrace_list[1], dragonborn_subrace_list[2]]:
            return ["Common" , "Draconic"]
        else:
            return ["Common", "Other"]

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
        return random.choice(color_list)

    def chromatic_ancestry(self):
        color_list = [
            ("Black", "Acid"),
            ("Blue", "Lightning"),
            ("Green", "Poison"),
            ("Red", "Fire"),
            ("White", "Cold")
        ]
        return random.choice(color_list)

    def metallic_ancestry(self):
        color_list = [
            ("Brass", "Fire"),
            ("Bronze", "Lightning"),
            ("Copper", "Acid"),
            ("Gold", "Fire"),
            ("Silver", "Cold")
        ]
        return random.choice(color_list)

    def gem_ancestry(self):
        color_list = [
            ("Amethyst", "Force"),
            ("Crystal", "Radiant"),
            ("Emerald", "Psychic"),
            ("Sapphire", "Thunder"),
            ("Topaz", "Necrotic")
        ]
        return random.choice(color_list)



class Dwarf(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choices(dwarf_subrace_list, weights=[2,2,2,1,1],k=1)[0]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Dwarvish"]

    def get_speed(self):
        if self.subrace_check == dwarf_subrace_list[3]:
            return "Walk- 30"
        return "Walk- 25"
    
    def tough_flag(self):
        if self.subrace_check == dwarf_subrace_list[0]:
            return (True, 1)
        else:
            return (False, 0)
        
    def get_proficiencies(self):
        if self.subrace == dwarf_subrace_list[1]:
            return ["light armor", "medium armor"]
        elif self.subrace == dwarf_subrace_list[4]:
            return ["battleaxe", "handaxe", "light hammer", "warhammer"]
        else:
            return []



class Elf(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll =  random.choices(elf_subrace_list, weights=[3,3,3,3,2,1,1,1,1,1,1], k=1)[0]
        self.subrace_check = roll
        if roll in [elf_subrace_list[5], elf_subrace_list[6]]:
            season = self.eladrin_season()
            roll = replace_placeholder(roll, f"{season} Eladrin")
            return roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == elf_subrace_list[1]:
            return ["Common", "Elven", "Other"]
        elif self.subrace_check in [elf_subrace_list[5], elf_subrace_list[7], elf_subrace_list[9]]:
            return ["Common", "Other"]
        elif self.subrace_check == elf_subrace_list[8]:
            return ["Common", "Elven", "Aquan"]
        else:
            return ["Common", "Elven"]
        
    def get_proficiencies(self):
        if self.subrace == elf_subrace_list[0]:
            return ["rapier", "shorsword", "hand crossbow"]
        elif self.subrace in [elf_subrace_list[1], elf_subrace_list[2]]:
            return ["longsword", "shortsword", "shortbow", "longbow"]
        elif self.subrace == elf_subrace_list[8]:
            return ["spear", "trident", "light crossbow", "net"]
        else:
            return []

    def get_speed(self):
        if self.subrace == elf_subrace_list[2]:
            return "Walk- 35"
        elif self.subrace == elf_subrace_list[7]:
            return "Walk- 30, Swim- 30"
        else:
            return "Walk- 30"
        
    def eladrin_season(self):
        season_list = ["Autum", "Winter", "Spring", "Summer"]
        return random.choice(season_list)



class Fairy(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = ["Fairy", "Fairy", [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],[[1, "Fairy Magic"], [1, "Flight"], ]]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Other"]
        
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 30, Fly- 30"



class Firbolg(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(firbolg_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == firbolg_subrace_list[0]:
            return["Common", "Other"]
        return["Common", "Elvish", "Giant"]



class Genasi(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(genasi_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check in [genasi_subrace_list[0], genasi_subrace_list[2], genasi_subrace_list[4], genasi_subrace_list[6]]:
            return ["Common", "Other"]
        return ["Common", "Primordial"]
    
    def get_size(self):
        if self.subrace not in [genasi_subrace_list[0], genasi_subrace_list[2], genasi_subrace_list[4], genasi_subrace_list[6]]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"
    
    def get_speed(self):
        if self.subrace == genasi_subrace_list[0]:
            return "Walk- 35"
        if self.subrace in [genasi_subrace_list[6], genasi_subrace_list[7]]:
            return "Walk- 30, Swim- 30"
        return "Walk- 30"



class Githyanki(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(githyanki_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == githyanki_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common", "Gith", "Other"]
    
    def get_proficiencies(self):
        if self.subrace != githyanki_subrace_list[1]:
            return []
        return ["light armor", "medium armor", "shortsword", "longsword", "greatsword"]



class Githzerai(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(githzerai_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == githzerai_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common", "Gith"]



class Gnome(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choices(gnome_subrace_list, weights=[2,2,2,1,1], k=1)[0]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == gnome_subrace_list[3]:
            return ["Common", "Other"]
        return ["Common", "Gnomish"]
    
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        if self.subrace != gnome_subrace_list[3]:
            return "Walk- 25"
        return "Walk- 30"



class Goblin(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(goblin_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == goblin_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common", "Goblin"]
            
    def get_size(self):
        return "Size- Small"



class Goliath(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(goliath_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == goliath_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Giant"]



class Grung(Race):
    def __init__(self):
            super().__init__()

    def subrace_roll(self):
        roll = ["Grung", "Grung", [{"DEX": 2, "CON": 1}], [[1, "Arboreal Alertness"], [1, "Amphibious"], [1, "Poison Immunity"], [1, "Poisonous Skin"], [1, "Standing Leap"], [1, "Water Dependency"]]]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Grung"]
    
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 25, Climb- 25"



class HalfElf(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(halfelf_subrace_list)
        self.subrace_check = roll
        if roll == halfelf_subrace_list[0]:
            self.he_heritage = self.heritage()
            roll = replace_placeholder(roll, f"Half-Elf Versatility: {self.he_heritage}")
            return roll
        return roll
    
    def get_languages(self):
        return ["Common", "Elven", "Other"]

    def heritage(self):
        heritage_list = [
            "Skill Versatility (General)",
            "Elf Weapon Training (High or Wood Elf Heritage)",
            "Cantrip (High Elf Heritage)",
            "Fleet of Foot (Wood Elf Heritage)",
            "Mask of the Wild (Wood Elf Heritage)",
            "Drow Magic (Dark Elf Heritage)",
            "Swim Speed (Aquatic Elf Heritage)"
        ]
        return random.choice(heritage_list)

    def get_proficiencies(self):
        if self.subrace_check == halfelf_subrace_list[0]:
            if self.he_heritage == "Elf Weapon Training (High or Wood Elf Heritage)":
                return ["Longsword", "Shortsword","Shortbow", "Longbow"]
        return []
            
    def get_speed(self):
        if self.subrace_check == halfelf_subrace_list[0]:
            if self.he_heritage == "Fleet of Foot (Wood Elf Heritage)":
                return "Walk- 35"
            elif self.he_heritage == "Swim Speed (Aquatic Elf Heritage)":
                return "Walk-30, Swim- 30"
        else:
            return "Walk- 30"



class Halfling(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(halfling_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Halfling"]
    
    def get_size(self):
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 25"



class HalfOrc(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(halforc_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == halforc_subrace_list[0]:
            return ["Common", "Orc"]
        return ["Common" , "Goblin"]



class Harengon(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = ["Harengon", "Harengon", [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}], [[1, "Hare-Trigger"], [1, "Leporine Senses"], [1, "Lucky Footwork"], [1, "Rabbit Hop"]]]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common" , "Other"]
    
    def get_size(self):
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Hobgoblin(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(hobgoblin_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == hobgoblin_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Goblin"]



class Human(Race): 
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(human_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Other"]

    def get_speed(self):
        if self.subrace == human_subrace_list[4]:
            return "Walk- 35"
        return "Walk- 30"



class Kenku(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(kenku_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == kenku_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Auran"]
    
    def get_size(self):
        if self.subrace != kenku_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Kobold(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(kobold_subrace_list)
        self.subrace_check = roll
        if roll == kobold_subrace_list[0]:
            legacy = self.koblegacy()
            roll = replace_placeholder(roll,f"Kobold Legacy: {legacy}")
            return roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == kobold_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Draconic"]

    def get_size(self):
        return "Size- Small"
    
    def koblegacy(self):
        legacy_list = [
            "Craftiness",
            "Defiance",
            "Dracoic Sorcery"
        ]
        return random.choice(legacy_list)



class Lizardfolk(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(lizardfolk_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == lizardfolk_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Draconic"]
    
    def get_speed(self):
        return "Walk- 30, Swim- 30"



class Minotaur(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(minotaur_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == minotaur_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Minotaur"]



class Orc(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(orc_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == orc_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Orc"]



class Owlin(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = ["Owlin", "Owlin", [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}], [[1, "Darkvision- 120"], [1, "Flight"], [1, "Silent Feathers"]]]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Other"]
    
    def get_size(self):
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"
    
    def get_speed(self):
        return "Walk- 30, Fly- 30"



class Satyr(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(satyr_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == satyr_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Sylvan"]
    
    def get_speed(self):
        return "Walk- 35"



class Shifter(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(shifter_subrace_list)
        self.subrace_check = roll
        if roll == shifter_subrace_list[0]:
            ancestor = self.ancestor()
            roll = replace_placeholder(roll, f"Shifting- {ancestor[0]}")
            return roll
        return roll
    
    def get_languages(self):
        return ["Common", "Other"]
    
    def ancestor(self):
        lycanthrope_list = [
            ("Werebear", "Beasthide"),
            ("Wereboar", "Beasthide"),
            ("Wererat", "Swiftstride"),
            ("Weretiger", "Swiftstride"),
            ("Werewolf (Wolflike)", "Longtooth"),
            ("Werewolf (Doglike)", "Wildhunt")
        ]
        return random.choice(lycanthrope_list)



class Tabaxi(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(tabaxi_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Other"]
    
    def get_speed(self):
        if self.subrace == tabaxi_subrace_list[0]:
            return "Walk- 30, Climb- 30"
        return "Walk- 30"

    def get_size(self):
            if self.subrace != tabaxi_subrace_list[0]:
                return "Size- Medium"
            if random.choice([0,1]) == 1:
                return "Size- Medium"
            return "Size- Small"



class Tiefling(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(tiefling_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common" , "Infernal"]



class Tortle(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(tortle_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == tortle_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Aquan"]
    
    def get_size(self):
        if self.subrace != tortle_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"



class Triton(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(triton_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == triton_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Primordial"]
    
    def get_speed(self):
        return "Walk- 30, Swim:- 30"



class Verdan(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll =["Verdan", "Verdan", [{"CHA": 2, "CON": 1}], [[1, "Black Blood Healing"], [1, "Limited Telepathy"], [1, "Persuasive"], [1, "Telepathic Insight"]]]
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        return ["Common", "Goblin", "Other"]
    
    def get_size(self):
        return "Size- Small"



class YuanTi(Race):
    def __init__(self):
        super().__init__()

    def subrace_roll(self):
        roll = random.choice(yuanti_subrace_list)
        self.subrace_check = roll
        return roll
    
    def get_languages(self):
        if self.subrace_check == yuanti_subrace_list[0]:
            return ["Common", "Other"]
        return ["Common" , "Abyssal", "Draconic"]

    def get_size(self):
        if self.subrace != yuanti_subrace_list[0]:
            return "Size- Medium"
        if random.choice([0,1]) == 1:
            return "Size- Medium"
        return "Size- Small"