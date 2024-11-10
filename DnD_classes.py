import random
from parent_character_class import Character
from variables_page import stat_mod_dict
import ast



# Child classes of the main Character class. Each child (except Commoner) is used to store data specific to that class.
class Artificer(Character):
    def __init__(self, char_id):
        self.__char_class__= "Artificer"
        super().__init__(char_id)
        
    def key_stat_index(self):
        return [3, "INT"]
    
    def hp_stat_index(self):
        return 8

    def subclass_roll(self):
        list_of_subclasses = [
            ("Alchemist", ((3, "Alchemist Spells"), (3, "Experimental Elixir"), (5, "Alchemical Savant"), (9, "Restorative Reagents"), (15, "Chemical Mastery"))),
            ("Armorer", ((3, "Armorer Spells"), (3, "Arcane Armor"), (3, "Armor Model"), (5, "Extra Attack"), (9, "Armor Modifications"), (15, "Perfected Armor"))),
            ("Artillerist", ((3, "Artillerist Spells"), (3, "Eldritch Cannon"), (5, "Arcane Firearm"), (9, "Explosive Cannon"), (15, "Foritified Position"))),
            ("Battle Smith", ((3, "Battle Smith Spells"), (3, "Battle Ready"), (3, "Steel Defender"), (5, "Extra Attack"), (9, "Arcane Jolt"), (15, "Improved Defender")))
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        class_proficiencies = ["light armor", "medium armor", "shield", "simple weapon"]
        if self.__char_level__ >= 3 and self.subclass[0] == "Battle Smith":
            class_proficiencies.append("martial weapon")
        return class_proficiencies

    def get_class_features(self):
        class_features = [
            (1, "Magical Tinkering"),
            (1, "Spellcasting"),
            (2, "Infuse Item"),
            (3, "The Right Tool for the Job"),
            (6, "Tool Expertise"), (7, "Flash of Genius"),
            (10, "Magic Item Adept"),
            (11, "Spell-Storing Item"),
            (14, "Magic Item Savant"),
            (18, "Magic Item Master"),
            (20, "Soul of Artifice")]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features


class Barbarian(Character): # Rework speed for "Fast Movement"
    def __init__(self, char_id):
        self.__char_class__= "Barbarian"
        super().__init__(char_id)

    def key_stat_index(self):
        return [0, "STR"]
    
    def hp_stat_index(self):
        return 12
    
    def subclass_roll(self):
        subclass_list = [
            ("Ancestral Guardian", ((3, "Ancestral Protectors"), (6, "Spirit Shield"), (10, "Consult the Spirits"), (14, "Vengeful Ancestors"))),
            ("Battlerager", ((3, "Battlerager Armor"), (6, "Reckless Abandon"), (10, "Battlerager Charge"), (14, "Spiked Retribution"))),
            ("Beast", ((3, "Form of the Beast"), (6, "Bestial Soul"), (10, "Infectious Fury"), (14, "Call the Hunt"))),
            ("Berserker", ((3, "Frenzy"), (6, "Mindless Rage"), (10, "Intimidating Presence"), (14, "Retaliation"))),
            ("Giant", ((3, "Giant's Might"), (3, "Giant's Havoc"), (6, "Elemental Cleaver"), (10, "Mighty Impel"), (14, "Demiurgic Colossus"))),
            ("Storm Herald", ((3, "Storm Aura"), (6, "Storm Soul"), (10, "Shielding Storm"), (14, "Raging Storm"))),
            ("Totem Warrior", ((3, "Spirit Seeker"), (3, "Totem Spirit"), (6, "Aspect of the Beast"), (10, "Spirit Walker"), (14, "Totemic Attunement"))),
            ("Wild Magic", ((3, "Magic Awareness"), (3, "Wild Surge"), (6, "Bolstering Magic"), (10, "Unstable Backlash"), (14, "Controlled Surge"))),
            ("Zealot", ((3, "Divine Fury"), (3, "Warrior of the Gods"), (6, "Fanatical Focus"), (10, "Zealous Presence"), (14, "Rage Beyond Death")))
        ]
        while True:
            if self.__char_level__ >= 3:  
                self.subclass = random.choice(subclass_list)
                if self.subclass[0] == "Battlerager" and self.race.get_race_name() != "Dwarf":
                    continue
                else:
                    break
            else:
                self.subclass = "None"
                break

    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi
    
    def calculate_ac(self):
        if self.__shield__ == "None":
            self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]] + stat_mod_dict[self.__char_stats_dict__["CON"]]
        else:
            self.__ac__ = 12 + stat_mod_dict[self.__char_stats_dict__["DEX"]] + stat_mod_dict[self.__char_stats_dict__["CON"]]


    def get_class_proficiencies(self):
        return ["shield", "simple weapon", "martial weapon"]
    
    def get_class_features(self):
        class_features = [(1, "Rage"), (1, "Unarmored Defense"), (2, "Danger Sense"), (2, "Reckless Attack"), (3, "Primal KNowledge"), (5, "Extra Attack"), (5, "Fast Movement"), (7, "Feral Instinct"), (7, "Instinctive Pounce"), (9, "Brutal Critical"), (11, "Relentless Rage"), (15, "Persistent Rage"), (18, "Indomitable Might"), (20, "Primal Champion")]
        return class_features
    
    def get_class_features(self):
        class_features = [
            (1, "Rage"),
            (1, "Unarmored Defense"),
            (2, "Reckless Attack"),
            (2, "Danger Sense"),
            (3, "Primal Path"),
            (5, "Extra Attack"),
            (5, "Fast Movement"),
            (7, "Feral Instinct"),
            (9, "Brutal Critical (1 die)"),
            (11, "Relentless Rage"),
            (13, "Brutal Critical (2 dice)"),
            (15, "Persistent Rage"),
            (17, "Brutal Critical (3 dice)"),
            (18, "Indomitable Might"),
            (20, "Primal Champion")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Bard(Character): # Have a maybe on 3 colleges.
    def __init__(self, char_id):
        self.__char_class__= "Bard"
        super().__init__(char_id)

    def key_stat_index(self):
        return [5, "CHA"]
    
    def hp_stat_index(self):
        return 8
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("College of Creation", ((3, "Mote of Potential"), (3, "Performance of Creation"), (6, "Animating Performance"), (14, "Creative Crescendo"))),
            ("College of Eloquence", ((3, "Silver Tongue"), (3, "Unsettling Words"), (6, "Unfailing Inspiration"), (6, "Universal Speech"), (14, "Infectious Inspiration"))),
            ("College of Glamour", ((3, "Mantle of Inspiration"), (3, "Enthralling Performance"), (6, "Mantle of Majesty"), (14, "Unbreakable Majesty"))),
            ("College of Lore", ((3, "Bonus Proficiencies"), (3, "Cutting Words"), (6, "Additional Magical Secrets"), (14, "Peerless Skill"))), # Maybe redo proficiencies eventually
            ("College of Spirits", ((3, "Guiding Whispers"), (3, "Spiritual Focus"), (6, "Tales from Beyond"), (14, "Mystical Connection"))),
            ("College of Swords", ((3, "Bonus Proficiencies"), (3, "Fighting Style"), (3, "Blade Flourish"), (6, "Extra Attack"), (14, "Master's Flourish"))), # Maybe redo proficiencies eventually
            ("College of Valor", ((3, "Bonus Proficiencies"), (3, "Combat Inspiration"), (6, "Extra Attack"), (14, "Battle Magic"))), # Maybe redo proficiencies eventually
            ("College of Whispers", ((3, "Psychic Blades"), (3, "Words of Terror"), (6, "Mantle of Whispers"), (14, "Shadow Lore"))) 
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"

    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi
    
    def get_class_proficiencies(self):
        return ["light armor", "simple weapon", "hand crossbow", "longsword", "rapier", "shortsword"]

    def get_class_features(self):
        class_features = [
            (1, "Spellcasting"),
            (1, "Bardic Inspiration"),
            (2, "Jack of All Trades"),
            (2, "Song of Rest"),
            (2, "Magical Inspiration"),
            (3, "Expertise"),
            (4, "Bardic Versatility"),
            (5, "Font of Inspiration"),
            (6, "Countercharm"),
            (10, "Magical Secrets"),
            (20, "Superior Inspiration")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Cleric(Character): # Multiple subclasses need a second look
    def __init__(self, char_id):
        self.__char_class__= "Cleric"
        super().__init__(char_id)

    def key_stat_index(self):
        return [4, "WIS"]
    
    def hp_stat_index(self):
        return 8
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("Arcana Domain", ((1, "Arcane Initiate"), (2, "Channel Divinity: Arcane Abjuration"), (6, "Spell Breaker"), (8, "Potent Spellcasting"), (17, "Arcane Mastery"))), # Maybe redo proficiencies eventually
            ("Death Domain", ((1, "Bonus Proficiency"), (1, "Reaper"), (2, "Channel Divinity: Touch of Death"), (6, "Inescapable Destruction"), (8, "Divine Strike"), (17, "Improved Reaper"))), # Add martial weapon proficiency
            ("Forge Domain", ((1, "Bonus Proficiency"),(1, "Blessing of the Forge"), (2, "Channel Divinity: Artisan's Blessing"), (6, "Soul of the Forge"), (8, "Divine Strike"), (17, "Saint of Forge and Fire"))), # Maybe redo proficiencies eventually and heavy armor
            ("Grave Domain", ((1, "Circle of Mortality"), (1, "Eyes of the Grave"), (2, "Channel Divinity: Path to the Grave"), (6, "Sentinel at Death's Door"), (8, "Potent Spellcasting"), (17, "Keeper of Souls"))),
            ("Knowledge Domain", ((1, "Blessings of Knowledge"), (2, "Channel Divinity: Knowledge of the Ages"), (6, "Channel Divinity: Read Thoughts"), (8, "Potent Spellcasting"), (17, "Visions of the Past"))), # Maybe redo proficiencies eventually
            ("Life Domain", ((1, "Bonus Proficiency"), (1, "Disciple of Life"), (2, "Channel Divinity: Preserve Life"), (6, "Blessed Healer"), (8, "Divine Strike"), (17, "Supreme Healing"))), # Add heavy armor proficiency
            ("Light Domain", ((1, "Bonus Cantrip"), (1, "Warding Flare"), (2, "Channel Divinity: Radiance of the Dawn"), (6, "Improved Flare"), (8, "Potent Spellcasting"), (17, "Corona of Light"))),
            ("Nature Domain", ((1, "Acolyte of Nature"), (1, "Bonus Cantrip"), (2, "Channel Divinity: Charm Animals and Plants"), (6, "Dampen Elements"), (8, "Divine Strike"), (17, "Master of Nature"))), # Maybe redo proficiencies eventually and heavy armor
            ("Order Domain", ((1, "Bonus Proficiencies"), (1, "Voice of Authority"), (2, "Channel Divinity: Order's Demand"), (6, "Embodiment of the Law"), (8, "Divine Strike"), (17, "Order's Wrath"))), # Maybe redo proficiencies eventually and heavy armor
            ("Peace Domain", ((1, "Implement of Peace"), (1, "Emboldening Bond"), (2, "Channel Divinity: Balm of Peace"), (6, "Protective Bond"), (8, "Potent Spellcasting"), (17, "Expansive Bond"))), # Maybe redo proficiencies eventually
            ("Tempest Domain", ((1, "Bonus Proficiencies"), (1, "Wrath of the Storm"), (2, "Channel Divinity: Destructive Wrath"), (6, "Thunderous Strike"), (8, "Divine Strike"), (17, "Stormborn"))), # Proficiency with martial weapons, heavy armor, and a fly speed
            ("Trickery Domain", ((1, "Blessing of the Trickster"), (2, "Channel Divinity: Invoke Duplicity"), (6, "Channel Divinity: Cloak of Shadows"), (8, "Divine Strike"), (17, "Improved Duplicity"))),
            ("Twilight Domain", ((1, "Bonus Proficiency"), (1, "Eyes of Night"), (1, "Vigilant Blessing"), (2, "Channel Divinity: Twilight Sanctuary"), (6, "Steps of Night"), (8, "Divine Strike"), (17, "Twilight Shroud"))), # Proficiency with martial weapons and heavy armor
            ("War Domain", ((1, "Bonus Proficiencies"), (1, "War Priest"), (2, "Channel Divinity: Guided Strike"), (6, "Channel Divinity: War God's Blessing"), (8, "Divine Strike"), (17, "Avatar of Battle"))), # Proficiency with martial weapons and heavy armor
        ]
        self.subclass = random.choice(list_of_subclasses)

    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi
    
    def get_class_proficiencies(self):
        return ["light armor", "medium armor", "shield", "simple weapon"]

    def get_class_features(self):
        class_features = [
            (1, "Spellcasting"),
            (1, "Divine Domain"),
            (2, "Channel Divinity (1 use)"),
            (6, "Channel Divinity (2 uses)"),
            (8, "Divine Strike or Potent Spellcasting (varies by domain)"),
            (10, "Divine Intervention"),
            (18, "Channel Divinity (3 uses)"),
            (20, "Improved Divine Intervention")
        ]
        class_features.extend(self.subclass[1])
        return class_features



# Commoner is the only different child class and sets the character level to 0, uses its own stat roll function (which limits its range), and roll hp function ().
class Commoner(Character):
    def __init__(self, char_id):
        self.__char_class__= "Commoner"
        super().__init__(char_id)

    def key_stat_index(self):
        return [2, "CON"]

    def subclass_roll(self):
        self.subclass = "None"
    
    def get_asi(self):
        return 0
    
    def random_char_level(self):
        self.__char_level__ = 0
    
    def stats_roll(self):
        self.rolls_for_stats = [0, 0, 0, 0, 0, 0]
        while self.rolls_for_stats[self.key_stat_index()[0]] == 0 or self.rolls_for_stats[self.key_stat_index()[0]] < max(self.rolls_for_stats):
            numbers_rolled = []
            for i in range(6):
                stat_roll = random.choices([6, 7, 8, 9, 10, 11, 12, 13, 14], weights = [1, 2, 3, 4, 5, 4, 3, 2, 1], k=1)[0]
                numbers_rolled.append(stat_roll)
            self.rolls_for_stats = numbers_rolled

    def roll_hp(self):
        self.__hp__ = 4 + stat_mod_dict[self.__char_stats_dict__["CON"]]

    def calculate_ac(self):
        self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]]

    def get_class_proficiencies(self):
        return []
    
    def secondary_score(self):
        return random.choice([(0, "STR"), (1, "DEX"), (3, "INT"), (4, "WIS"), (5, "CHA")])

    def get_class_features(self):
        return []



class Druid(Character): # One subclass change
    def __init__(self, char_id):
        self.__char_class__= "Druid"
        super().__init__(char_id)

    def key_stat_index(self):
        return [4, "WIS"]
    
    def hp_stat_index(self):
        return 8
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("Circle of Dreams", ((2, "Balm of the Summer Court"), (6, "Hearth of Moonlight and Shadow"), (10, "Hidden Paths"), (14, "Walker in Dreams"))),
            ("Circle of the Land", ((2, "Bonus Cantrip"), (2, "Natural Recovery"), (6, "Land's Stride"), (10, "Nature's Ward"), (14, "Nature's Sanctuary"))),
            ("Circle of the Moon", ((2, "Combat Wild Shape"), (2, "Circle Forms"), (6, "Primal Strike"), (10, "Elemental Wild Shape"), (14, "Thousand Forms"))),
            ("Circle of the Shepherd", ((2, "Speech of the Woods"), (2, "Spirit Totem"), (6, "Mighty Summoner"), (10, "Guardian Spirit"), (14, "Faithful Summons"))), # Maybe rework languages
            ("Circle of Spores", ((2, "Halo of Spores"), (2, "Symbiotic Entity"), (6, "Fungal Infestation"), (10, "Spreading Spores"), (14, "Fungal Body"))),
            ("Circle of Stars", ((2, "Star Map"), (2, "Starry Form"), (6, "Cosmic Omen"), (10, "Twinkling Constellation"), (14, "Full of Stars"))),
            ("Circle of Wildfire", ((2, "Summon Wildfire Spirit"), (6, "Enhanced Bond"), (10, "Cauterizing Flames"), (14, "Blazing Revival")))
        ]
        if self.__char_level__ >= 2:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        return ["light armor", "medium armor", "shield", "club", "dagger", "dart", "javelin", "mace", "quarterstaff", "scimitar", "sickle", "sling", "spear"]

    def get_class_features(self):
        class_features = [
            (1, "Druidic"),
            (1, "Spellcasting"),
            (2, "Wild Shape"),
            (2, "Druid Circle"),
            (4, "Wild Shape Improvement"),
            (18, "Timeless Body"),
            (18, "Beast Spells"),
            (20, "Archdruid")
        ]
        if self.__char_level__ >= 2:
            class_features.extend(self.subclass[1])
        return class_features



class Fighter(Character):
    def __init__(self, char_id):
        self.__char_class__= "Fighter"
        super().__init__(char_id)

    def key_stat_index(self):
        self.key_stat = random.randint(0, 1)
        if self.key_stat == 0:
            return [0, "STR"]
        else:
            return [1, "DEX"]
    
    def hp_stat_index(self):
        return 10

    def subclass_roll(self):
        list_of_subclasses = [
            ("Arcane Archer", ((3, "Arcane Archer Lore"), (3, "Arcane Shot"), (7,"Magic Arrow"), (7, "Curving Shot"), (15, "Ever-Ready Shot"))),#Arcane Archer Lore- skill prof and cantrips
            ("Banneret", ((3, "Rallying Cry"), (7, "Royal Envoy"), (10, "Inspiring Surge"), (15, "Bulwark"))),#Royal Envoy- persuasion prof or other skill
            ("Battle Master", ((3, "Combat Superiority"), (3, "Student of War"), (7, "Know Your Enemy"), (10, "Improved Combat Superiority"), (15, "Relentless"))),#Student of War- tool prof
            ("Cavalier", ((3, "Bonus Proficiency"), (3, "Born to the Saddle"), (3, "Unwavering Mark"), (7, "Warding Maneuver"), (10, "Hold the Line"), (15, "Ferocious Charger"), (18, "Vigilant Defender"))),#Bonus Proficiency- skill prof or extra language
            ("Champion", ((3, "Improved Critical"), (7, "Remarkable Athlete"), (10, "Additional Fighting Style"), (15, "Superior Critical"), (18, "Survivor"))),
            ("Echo Knight", ((3, "Manifest Echo"), (3, "Unleash Incarnation"), (7, "Echo Avatar"), (10, "Shadow Martyr"), (15, "Reclaim Potential"), (18, "Legion of One"))),
            ("Eldritch Knight", ((3, "Spellcasting"), (3, "Weapon Bond"), (7, "War Magic"), (10, "Eldritch Strike"), (15, "Arcane Charge"), (18, "Improved War Magic"))),
            ("Psi Warrior", ((3, "Psionic Power"), (7, "Telekinetic Adept"), (10, "Guarded Mind"), (15, "Bulwark of Force"), (18, "Telekinetic Master"))),
            ("Rune Knight", ((3, "Bonus Proficiencies"), (3, "Rune Carver"), (3, "Giant's Might"), (7, "Runic Shield"), (10, "Great Stature"), (15, "Master of Runes"), (18, "Runic Juggernaut"))),#Bonus Proficiencies smith tools + giant language
            ("Samurai", ((3, "Bonus Proficiencies"), (3, "Fighting Spirit"), (7, "Elegant Courtier"), (10, "Tireless Spirit"), (15, "Rapid Strike"), (18, "Strength Before Death"))) #Bonus Proficiency- skill prof or extra language
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 14:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 6:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi
    
    def roll_weapon(self):
        while True:
            self.__weapon__ = random.choice(self.weapon_list)
            if self.__char_stats_dict__["DEX"] > self.__char_stats_dict__["STR"] and ast.literal_eval(self.__weapon__[4]):
                break
            elif self.__char_stats_dict__["DEX"] <= self.__char_stats_dict__["STR"]:
                break

    def get_class_proficiencies(self):
        return ["light armor", "medium armor", "heavy armor", "shield", "simple weapon", "martial weapon"]

    def get_class_features(self):
        class_features = [
            (1, "Fighting Style"),
            (1, "Second Wind"),
            (2, "Action Surge (1 use)"),
            (5, "Extra Attack (1)"),
            (9, "Indomitable (1 use)"),
            (11, "Extra Attack (2)"),
            (13, "Indomitable (2 uses)"),
            (17, "Action Surge (2 uses)"),
            (17, "Indomitable (3 uses)"),
            (20, "Extra Attack (3)")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Monk(Character):
    def __init__(self, char_id):
        self.__char_class__= "Monk"
        super().__init__(char_id)

    def key_stat_index(self):
        self.key_stat = random.choice([1, 4])
        if self.key_stat == 1:
            return [1, "DEX"]
        else:
            return [4, "WIS"]
    
    def secondary_score(self):
        if self.key_stat == 1:
            return [4, "WIS"]
        else:
            return [1, "STR"]
    
    def hp_stat_index(self):
        return 8

    def subclass_roll(self):
        list_of_subclasses = [
            ("Way of Mercy", ((3, "Implements of Mercy"), (3, "Hand of Healing"), (3, "Hand of Harm"), (6, "Physician's Touch"), (11, "Flurry of Healing and Harm"), (17, "Hand of Ultimate Mercy"))),#Implements of Mercy- skill prof + herb kit
            ("Way of the Ascendant Dragon", ((3, "Draconic Disciple"), (3, "Breath of the Dragon"), (6, "Wings Unfurled"), (11, "Aspect of the Wyrm"), (17, "Ascendant Aspect"))),#Ascendant Dragon Origin
            ("Way of the Astral Self", ((3, "Arms of the Astral Self"), (6, "Visage of the Astral Self"), (11, "Body of the Astral Self"), (17, "Awakened Astral Self"))),
            ("Way of the Drunken Master", ((3, "Bonus Proficiencies"), (3, "Drunken Technique"), (6, "Tipsy Sway"), (11, "Drunkard's Luck"), (17, "Intoxicated Frenzy"))),#Bonus Proficiencies- performance + brewer supplies
            ("Way of the Four Elements", ((3, "Disciple of the Elements"), (6, "Elemental Disciplines"), (11, "Elemental Disciplines"), (17, "Elemental Disciplines"))),  # Note: Features are chosen from Elemental Disciplines
            ("Way of the Kensei", ((3, "Path of the Kensei"), (6, "One with the Blade"), (11, "Sharpen the Blade"), (17, "Unerring Accuracy"))),#Path of the Kensei- kensei weapons- gain proficiency with chosen weapons | way of the brush- prof calluigrapher supp or painter supp
            ("Way of the Long Death", ((3, "Touch of Death"), (6, "Hour of Reaping"), (11, "Mastery of Death"), (17, "Touch of the Long Death"))),
            ("Way of the Open Hand", ((3, "Open Hand Technique"), (6, "Wholeness of Body"), (11, "Tranquility"), (17, "Quivering Palm"))),
            ("Way of Shadow", ((3, "Shadow Arts"), (6, "Shadow Step"), (11, "Cloak of Shadows"), (17, "Opportunist"))),
            ("Way of the Sun Soul", ((3, "Radiant Sun Bolt"), (6, "Searing Arc Strike"), (11, "Searing Sunburst"), (17, "Sun Shield")))
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi
    
    def roll_weapon(self):
        while True:
            self.__weapon__ = random.choice(self.weapon_list)
            if "Finesse" in ast.literal_eval(self.__weapon__[4]):
                break

    def calculate_ac(self):
        print(self.__char_stats_dict__)
        print(self.__char_level__)
        self.__ac__ = 10 + stat_mod_dict[self.__char_stats_dict__["DEX"]] + stat_mod_dict[self.__char_stats_dict__["WIS"]]

    def get_class_proficiencies(self):
        return ["simple weapon", "shortsword"]

    def get_class_features(self):
        class_features = [
            (1, "Unarmored Defense"),
            (1, "Martial Arts"),
            (2, "Ki"),
            (2, "Unarmored Movement"),
            (3, "Monastic Tradition"),
            (4, "Slow Fall"),
            (5, "Extra Attack"),
            (5, "Stunning Strike"),
            (6, "Ki-Empowered Strikes"),
            (7, "Evasion"),
            (7, "Stillness of Mind"),
            (10, "Purity of Body"),
            (13, "Tongue of the Sun and Moon"),
            (14, "Diamond Soul"),
            (15, "Timeless Body"),
            (18, "Empty Body"),
            (20, "Perfect Self")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Paladin(Character):
    def __init__(self, char_id):
        self.__char_class__= "Paladin"
        super().__init__(char_id)

    def key_stat_index(self):
        self.key_stat = random.choice([0, 5])
        if self.key_stat == 0:
            return [0, "STR"]
        else:
            return [5, "CHA"]
        
    def secondary_score(self):
        if self.key_stat == 0:
            return [5, "CHA"]
        else:
            return [0, "STR"]
    
    def hp_stat_index(self):
        return 10

    def subclass_roll(self):
        list_of_subclasses = [
            ("Oath of the Ancients", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of Warding"), (15, "Undying Sentinel"), (20, "Elder Champion"))),
            ("Oath of Conquest", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of Conquest"), (15, "Scornful Rebuke"), (20, "Invincible Conqueror"))),
            ("Oath of the Crown", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Divine Allegiance"), (15, "Unyielding Spirit"), (20, "Exalted Champion"))),
            ("Oath of Devotion", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of Devotion"), (15, "Purity of Spirit"), (20, "Holy Nimbus"))),
            ("Oath of Glory", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of Alacrity"), (15, "Glorious Defense"), (20, "Living Legend"))),
            ("Oath of Redemption", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of the Guardian"), (15, "Protective Spirit"), (20, "Emissary of Redemption"))),
            ("Oath of Vengeance", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Relentless Avenger"), (15, "Soul of Vengeance"), (20, "Avenging Angel"))),
            ("Oath of the Watchers", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of the Sentinel"), (15, "Vigilant Rebuke"), (20, "Mortal Bulwark"))),
            ("Oathbreaker", ((3, "Oath Spells"), (3, "Channel Divinity"), (7, "Aura of Hate"), (15, "Supernatural Resistance"), (20, "Dread Lord")))
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        return ["light armor", "medium armor", "heavy armor", "shield", "simple weapon", "martial weapon"]

    def get_class_features(self):
        class_features = [
            (1, "Divine Sense"),
            (1, "Lay on Hands"),
            (2, "Fighting Style"),
            (2, "Spellcasting"),
            (2, "Divine Smite"),
            (3, "Divine Health"),
            (3, "Sacred Oath"),
            (6, "Aura of Protection"),
            (10, "Aura of Courage"),
            (14, "Cleansing Touch"),
            (18, "Improved Aura of Protection"),
            (20, "Sacred Oath Feature")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Ranger(Character):
    def __init__(self, char_id):
        self.__char_class__= "Ranger"
        super().__init__(char_id)

    def key_stat_index(self):
        return [1, "DEX"]
    
    def hp_stat_index(self):
        return 10

    def subclass_roll(self):
        list_of_subclasses = [
            ("Beast Master", ((3, "Ranger's Companion"), (3, "Primal Companion (Optional)") (7, "Exceptional Training"), (11, "Bestial Fury"), (15, "Share Spells"))),
            ("Fey Wanderer", ((3, "Dreadful Strikes"), (3, "Fey Wanderer Magic"), (3, "Otherworldly Glamour"), (7, "Beguiling Twist"), (11, "Fey Reinforcements"), (15, "Misty Wanderer"))),#Otherworldly Glamour- skill prof
            ("Gloom Stalker", ((3, "Gloom Stalker Magic"), (3, "Dread Ambusher"), (3, "Umbral Sight"), (7, "Iron Mind"), (11, "Stalker's Flurry"), (15, "Shadowy Dodge"))),#Iron Mind- saving throw prof
            ("Horizon Walker", ((3, "Horizon Walker Magic"), (3, "Detect Portal"), (3, "Planar Warrior"), (7, "Ethereal Step"), (11, "Distant Strike"), (15, "Spectral Defense"))),
            ("Hunter", ((3, "Hunter's Prey"), (7, "Defensive Tactics"), (11, "Multiattack"), (15, "Superior Hunter's Defense"))),
            ("Monster Slayer", ((3,"Monster Slayer Magic"), (3, "Hunter's Sense"), (3, "Slayer's Prey"), (7, "Supernatural Defense"), (11, "Magic-User's Nemesis"), (15, "Slayer's Counter"))),
            ("Swarmkeeper", ((3, "Swarmkeeper Magic"), (3, "Gathered Swarm"), (7, "Writhing Tide"), (11, "Mighty Swarm"), (15, "Swarming Dispersal"))),
            ("Drakewarden", ((3, "Draconic Gift"), (3, "Drake Companion"), (7, "Bond of Fang and Scale"), (11, "Drake's Breath"), (15, "Perfected Bond")))#Drakewarden Origin, Drakewarden Origin- draconic or other language
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        return ["light armor", "medium armor", "shield", "simple weapon", "martial weapon"]

    def get_class_features(self):
        class_features = [
            (1, "Favored Enemy"),
            (1, "Natural Explorer"),
            (2, "Fighting Style"),
            (2, "Spellcasting"),
            (3, "Ranger Archetype"),
            (5, "Extra Attack"),
            (6, "Favored Enemy Improvement"),
            (8, "Land's Stride"),
            (10, "Natural Explorer Improvement"),
            (14, "Favored Enemy Improvement"),
            (18, "Feral Senses"),
            (20, "Foe Slayer")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Rogue(Character):
    def __init__(self, char_id):
        self.__char_class__= "Rogue"
        super().__init__(char_id)

    def key_stat_index(self):
        return [1, "DEX"]
    
    def hp_stat_index(self):
        return 8
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("Arcane Trickster", ((3, "Spellcasting"), (3, "Mage Hand Legerdemain"), (9, "Magical Ambush"), (13, "Versatile Trickster"), (17, "Spell Thief"))),
            ("Assassin", ((3, "Bonus Proficiencies"), (3, "Assassinate"), (9, "Infiltration Expertise"), (13, "Impostor"), (17, "Death Strike"))),#Bonus Proficiencies- disguise kit & poisoners kit
            ("Inquisitive", ((3, "Ear for Deceit"), (3, "Eye for Detail"), (3, "Insightful Fighting"), (9, "Steady Eye"), (13, "Unerring Eye"), (17, "Eye for Weakness"))),
            ("Mastermind", ((3, "Master of Intrigue"), (3, "Master of Tactics"), (9, "Insightful Manipulator"), (13, "Misdirection"), (17, "Soul of Deceit"))),#Master of Intrigue- disguise kit, forgery kit, 1 gaming set + 2 extra languages
            ("Phantom", ((3, "Whispers of the Dead"), (3, "Wails from the Grave"), (9, "Tokens of the Departed"), (13, "Ghost Walk"), (17, "Death Friend"))),
            ("Scout", ((3, "Skirmisher"), (3, "Survivalist"), (9, "Superior Mobility"), (13, "Ambush Master"), (17, "Sudden Strike"))),#Survivalist- skill prof, Superior Mobility +10 walk speed (climb & swim to)
            ("Soulknife", ((3, "Psionic Power"), (3, "Psychic Blades"), (9, "Soul Blades"), (13, "Psychic Veil"), (17, "Rend Mind"))),
            ("Swashbuckler", ((3, "Fancy Footwork"), (3, "Rakish Audacity"), (9, "Panache"), (13, "Elegant Maneuver"), (17, "Master Duelist"))),
            ("Thief", ((3, "Fast Hands"), (3, "Second-Story Work"), (9, "Supreme Sneak"), (13, "Use Magic Device"), (17, "Thief's Reflexes"))) #Use Magic Device- ignore class race & level req on magic items
        ]
        if self.__char_level__ >= 3:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 10:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def roll_weapon(self):
        while True:
            self.__weapon__ = random.choice(self.weapon_list)
            if "Finesse" in ast.literal_eval(self.__weapon__[4]):
                break

    def get_class_proficiencies(self):
        return ["light armor", "simple weapon", "hand crossbow", "longsword", "rapier", "shortsword"]

    def get_class_features(self):
        class_features = [
            (1, "Expertise"),
            (1, "Sneak Attack"),
            (1, "Thieves' Cant"),
            (2, "Cunning Action"),
            (3, "Roguish Archetype"),
            (5, "Uncanny Dodge"),
            (7, "Evasion"),
            (11, "Reliable Talent"),
            (14, "Blindsense"),
            (15, "Slippery Mind"),
            (18, "Elusive"),
            (20, "Stroke of Luck")
        ]
        if self.__char_level__ >= 3:
            class_features.extend(self.subclass[1])
        return class_features



class Sorcerer(Character):
    def __init__(self, char_id):
        self.__char_class__= "Sorcerer"
        super().__init__(char_id)        

    def key_stat_index(self):
        return [5, "CHA"]
    
    def hp_stat_index(self):
        return 6
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("Aberrant Mind", ((1, "Telepathic Speech"), (1, "Psionic Spells"), (6, "Psionic Sorcery"), (14, "Revelation in Flesh"), (18, "Warping Implosion"))),#Aberrant Origins
            ("Clockwork Soul", ((1, "Clockwork Magic"), (1, "Restore Balance"), (6, "Bastion of Law"), (14, "Trance of Order"), (18, "Clockwork Cavalcade"))),
            ("Divine Soul", ((1, "Divine Magic"), (1, "Favored by the Gods"), (6, "Empowered Healing"), (14, "Otherworldly Wings"), (18, "Unearthly Recovery"))),
            ("Draconic Bloodline", ((1, "Dragon Ancestor"), (1, "Draconic Resilience"), (6, "Elemental Affinity"), (14, "Dragon Wings"), (18, "Draconic Presence"))),#Draconic Ancestry- lanaguage draconic + cha check x2 with dragons
            ("Shadow Magic", ((1, "Eyes of the Dark"), (1, "Strength of the Grave"), (6, "Hound of Ill Omen"), (14, "Shadow Walk"), (18, "Umbral Form"))),#Shadow Sorcerer Quirks
            ("Storm Sorcery", ((1, "Wind Speaker"), (1, "Tempestuous Magic"), (6, "Heart of the Storm"), (6, "Storm Guide"), (14, "Storm's Fury"), (18, "Wind Soul"))),#Wind Speaker- language primordial
            ("Wild Magic", ((1, "Wild Magic Surge"), (1, "Tides of Chaos"), (6, "Bend Luck"), (14, "Controlled Chaos"), (18, "Spell Bombardment"))),
            ("Phoenix Sorcery", ((1, "Ignite"), (1, "Mantle of Flame"), (6, "Phoenix Spark"), (14, "Nourishing Fire"), (18, "Form of the Phoenix"))),
            ("Lunar Sorcery"), (((1, "Moon Fire"), (6, "Lunar Boons"), (6, "Waxing and Waning"), (14, "Lunar Empowerment"), (18, "LunarPhenomenon"))) #Added was missing?
        ]
        self.subclass = random.choice(list_of_subclasses)

    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        return ["dagger", "dart", "sling", "quarterstaff", "light crossbow"]

    def get_class_features(self):
        class_features = [
            (1, "Spellcasting"),
            (1, "Sorcerous Origin"),
            (2, "Font of Magic"),
            (3, "Metamagic"),
            (10, "Metamagic Improvement"),
            (17, "Metamagic Improvement"),
            (20, "Sorcerous Restoration")
        ]
        class_features.extend(self.subclass[1])
        return class_features



class Warlock(Character):
    def __init__(self, char_id):
        self.__char_class__= "Warlock"
        super().__init__(char_id)

    def key_stat_index(self):
        return [5, "CHA"]
    
    def hp_stat_index(self):
        return 8
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("Archfey", ((1, "Fey Presence"), (6, "Misty Escape"), (10, "Beguiling Defenses"), (14, "Dark Delirium"))),
            ("Celestial", ((1, "Bonus Cantrips"), (1, "Healing Light"), (6, "Radiant Soul"), (10, "Celestial Resilience"), (14, "Searing Vengeance"))),
            ("Fathomless", ((1, "Tentacle of the Deeps"), (1, "Gift of the Sea"), (6, "Oceanic Soul"), (6,"Guardian Coil" ), (10, "Grasping Tentacles"), (14, "Fathomless Plunge"))),#Gift of the Sea- 40 swim
            ("Fiend", ((1, "Dark One's Blessing"), (6, "Dark One's Own Luck"), (10, "Fiendish Resilience"), (14, "Hurl Through Hell"))),
            ("Genie", ((1, "Genie's Vessel"), (6, "Elemental Gift"), (10, "Sanctuary Vessel"), (14, "Limited Wish"))),#Genie Kind patron
            ("Great Old One", ((1, "Awakened Mind"), (6, "Entropic Ward"), (10, "Thought Shield"), (14, "Create Thrall"))),
            ("Hexblade", ((1, "Hexblade's Curse"), (1, "Hex Warrior"), (6, "Accursed Specter"), (10, "Armor of Hexes"), (14, "Master of Hexes"))),#Hex Warrior- prof medium armor, shieldm martial weapon
            ("Undead", ((1, "Form of Dread"), (6, "Grave Touched"), (10, "Necrotic Husk"), (14, "Spirit Projection"))),
            ("Undying", ((1, "Among the Dead"), (6, "Defy Death"), (10, "Undying Nature"), (14, "Indestructible Life")))
        ]
        self.subclass = random.choice(list_of_subclasses)
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        return ["light armor", "simple weapon"]

    def get_class_features(self):
        class_features = [
            (1, "Otherworldly Patron"),
            (1, "Pact Magic"),
            (2, "Eldritch Invocations"),
            (3, "Pact Boon"),
            (11, "Mystic Arcanum (6th level)"),
            (13, "Mystic Arcanum (7th level)"),
            (15, "Mystic Arcanum (8th level)"),
            (17, "Mystic Arcanum (9th level)"),
            (20, "Eldritch Master")
        ]
        class_features.extend(self.subclass[1])
        return class_features



class Wizard(Character):
    def __init__(self, char_id):
        self.__char_class__= "Wizard"
        super().__init__(char_id)

    def key_stat_index(self):
        return [3, "INT"]
    
    def hp_stat_index(self):
        return 6
    
    def subclass_roll(self):
        list_of_subclasses = [
            ("Bladesinging", ((2, "Training in War and Song"), (2, "Bladesong"), (6, "Extra Attack"), (10, "Song of Defense"), (14, "Song of Victory"))),#Training in War and Song- light armor + 1 one handed melee of choice + performance prof
            ("Chronurgy Magic", ((2, "Chronal Shift"), (2, "Temporal Awareness"), (6, "Momentary Stasis"), (10, "Arcane Abeyance"), (14, "Convergent Future"))),
            ("Graviturgy Magic", ((2, "Adjust Density"), (6, "Gravity Well"), (10, "Violent Attraction"), (14, "Event Horizon"))),
            ("Order of Scribes", ((2, "Wizardly Quill"), (2, "Awakened Spellbook"), (6, "Manifest Mind"), (10, "Master Scrivener"), (14, "One with the Word"))),
            ("School of Abjuration", ((2, "Abjuration Savant"), (2, "Arcane Ward"), (6, "Projected Ward"), (10, "Improved Abjuration"), (14, "Spell Resistance"))),
            ("School of Conjuration", ((2, "Conjuration Savant"), (2, "Minor Conjuration"), (6, "Benign Transposition"), (10, "Focused Conjuration"), (14, "Durable Summons"))),
            ("School of Divination", ((2, "Divination Savant"), (2, "Portent"), (6, "Expert Divination"), (10, "The Third Eye"), (14, "Greater Portent"))),
            ("School of Enchantment", ((2, "Enchantment Savant"), (2, "Hypnotic Gaze"), (6, "Instinctive Charm"), (10, "Split Enchantment"), (14, "Alter Memories"))),
            ("School of Evocation", ((2, "Evocation Savant"), (2, "Sculpt Spells"), (6, "Potent Cantrip"), (10, "Empowered Evocation"), (14, "Overchannel"))),
            ("School of Illusion", ((2, "Illusion Savant"), (2, "Improved Minor Illusion"), (6, "Malleable Illusions"), (10, "Illusory Self"), (14, "Illusory Reality"))),
            ("School of Necromancy", ((2, "Necromancy Savant"), (2, "Grim Harvest"), (6, "Undead Thralls"), (10, "Inured to Undeath"), (14, "Command Undead"))),
            ("School of Transmutation", ((2, "Transmutation Savant"), (2, "Minor Alchemy"), (6, "Transmuter's Stone"), (10, "Shapechanger"), (14, "Master Transmuter"))),
            ("War Magic", ((2, "Arcane Deflection"), (2, "Tactical Wit"), (6, "Power Surge"), (10, "Durable Magic"), (14, "Deflecting Shroud")))
        ]
        if self.__char_level__ >= 2:
            self.subclass = random.choice(list_of_subclasses)
        else:
            self.subclass = "None"
    
    def get_asi(self):
        total_asi = 0
        if self.__char_level__ >= 19:
            total_asi += 1
        if self.__char_level__ >= 16:
            total_asi += 1
        if self.__char_level__ >= 12:
            total_asi += 1
        if self.__char_level__ >= 8:
            total_asi += 1
        if self.__char_level__ >= 4:
            total_asi += 1
        return total_asi

    def get_class_proficiencies(self):
        return ["dagger", "dart", "sling", "quarterstaff", "light crossbow"]
    
    def get_class_features(self):
        class_features = [
            (1, "Spellcasting"),
            (1, "Arcane Recovery"),
            (2, "Arcane Tradition"),
            (18, "Spell Mastery"),
            (20, "Signature Spells")
        ]
        if self.__char_level__ >= 2:
            class_features.extend(self.subclass[1])
        return class_features
