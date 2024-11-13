# Range: 1-20. Change this to change the max level a rolled character can be.
max_char_level = 20

# Lower values makes higher levels more likely
char_level_odds = 1.35

# Chance for a rolled character to be a Commoner. Higher values make commoners more likely.
commoner_chance = 1

# Chance for a rolled character to have a shield if eligible. Odds are 1 in 10/number selected. E.g. 100 = 1 in 10, 90 = 1 in 9, 80 = 1 in 8, etc.
shield_chance = 25

# Chance for each of the race types to appear. Higher numbers = higher chance for that race type to appear.
common_races_odds = 7
exotic_races_odds = 2
monstrous_race_odds = 1


# Do not alter the below fields.
stat_mod_dict = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5}
class_odds_list = [1, 1, 1, 1, commoner_chance, 1, 1, 1, 1, 1, 1, 1, 1, 1]
stat_names_list = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
c, e, m = common_races_odds, exotic_races_odds, monstrous_race_odds
race_weights = [e, e, m, m, e, c, c, c, e, e, e, e, e, c, m, e, m, c, c, c, e, m, c, e, m, m, m, m, e, e, m, e, c, e, e, e, m]
# total common races: 9
# total exotic races: 17
# total monstrous races: 11

# Subrace lists stored below
aarakocra_subrace_list = [
    ["Aarakocra", "Aarakocra",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Flight"],
         [1, "Talons"],
         [1, "Wind Caller"]
     ]
    ],
    ["Aarakocra", "Aarakocra",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Flight"],
         [1, "Talons"]
     ]
    ]
]

aasimar_subrace_list = [
        ["Aasimar", "Aasimar",
         [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
         [
             [1, "celestial feature placeholder"],
             [1, "Darkvision- 60"],
             [1, "Celestial Resistance"],
             [1, "Healing Hands"],
             [1, "Light Bearer"],
             [3, "celestial revelation placeholder"]
         ]
        ],
        ["Aasimar", "Protector Aasimar",
         [{"CHA": 2, "WIS": 1}],
         [
             [1, "Darkvision- 60"],
             [1, "Celestial Resistance"],
             [1, "Healing Hands"],
             [1, "Light Bearer"],
             [1, "Radiant Soul"]
         ]
        ],
        ["Aasimar", "Scourge Aasimar",
         [{"CHA": 2, "CON": 1}],
         [
             [1, "Darkvision- 60"],
             [1, "Celestial Resistance"],
             [1, "Healing Hands"],
             [1, "Light Bearer"],
             [1, "Radiant Consumption"]
         ]
        ],
        ["Aasimar", "Fallen Aasimar",
         [{"CHA": 2, "STR": 1}],
         [
             [1, "Darkvision- 60"],
             [1, "Celestial Resistance"],
             [1, "Healing Hands"],
             [1, "Light Bearer"],
             [1, "Necrotic Shroud"]
         ]
        ]
    ]

bugbear_subrace_list = [
    ["Bugbear", "Bugbear",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Long-Limbed"],
         [1, "Powerful Build"],
         [1, "Sneaky"],
         [1, "Surprise Attack"]
     ]
    ],
    ["Bugbear", "Bugbear",
     [{"STR": 2, "DEX": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Long-Limbed"],
         [1, "Powerful Build"],
         [1, "Sneaky"],
         [1, "Surprise Attack"]
     ]
    ]
]

centaur_subrace_list = [
    ["Centaur", "Centaur",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Charge"],
         [1, "Equine Build"],
         [1, "Hooves"],
         [1, "Natural Affinity"]
     ]
    ],
    ["Centaur", "Centaur",
     [{"STR": 2, "WIS": 1}],
     [
         [1, "Fey"],
         [1, "Charge"],
         [1, "Hooves"],
         [1, "Equine Build"],
         [1, "Survivor"]
     ]
    ]
]

changeling_subrace_list = [
    ["Changeling", "Changeling",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Changeling Instincts"],
         [1, "Shapechanger"],
         [1, "Languages- Common/Other"]
     ]
    ],
    ["Changeling", "Changeling",
     [{"CHA": 2, "custom_stat_2": 1}],
     [
         [1, "Shapechanger"],
         [1, "Changeling Instincts"],
         [1, "Languages- Common/Other/Other"]
     ]
    ]
]

dragonborn_subrace_list = [
    ["Dragonborn", "Placeholder", 
     [{"STR": 2, "CHA": 1}], 
     [
         [1, "Placeholder"], 
         [1, "Placeholder"], 
         [1, "Placeholder"]
     ]
    ],
    ["Dragonborn", "Placeholder", 
     [{"INT": 2, "CHA": 1}], 
     [
         [1, "Darkvision- 60"], 
         [1, "Forceful Presence"], 
         [1, "Placeholder"], 
         [1, "Placeholder"]
     ]
    ],
    ["Dragonborn", "Placeholder",
     [{"STR": 2, "CON": 1}], 
     [
         [1, "Darkvision- 60"], 
         [1, "Vegeful Assault"], 
         [1, "Placeholder"], 
         [1, "Placeholder"]
     ]
    ],
    ["Dragonborn", "Chromatic Dragonborn", 
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}], 
     [
         [1, "Placeholder"], 
         [1, "Breath Weapon- 5 by 30ft. line (DEX save)"], 
         [1, "Placeholder"], 
         [5, "Chromatic Warding"]
     ]
    ],
    ["Dragonborn", "Metallic Dragonborn", 
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}], 
     [
         [1, "Placeholder"], 
         [1, "Breath Weapon- 15ft. cone (DEX save)"], 
         [1, "Placeholder"], 
         [5, "Metallic Breath Weapon"]
     ]
    ],
    ["Dragonborn", "Gem Dragonborn", 
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}], 
     [
         [1, "Placeholder"], 
         [1, "Breath Weapon- 15ft. cone (DEX save)"], 
         [1, "Psionic Mind"], 
         [1, "Placeholder"], 
         [5, "Gem Flight"]
     ]
    ]
]

dwarf_subrace_list = [
    ["Dwarf", "Hill Dwarf",
     [{"CON": 2, "WIS": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Dwarven Resilience"],
         [1, "Dwarven Combat Training"],
         [1, "Tool Proficiency"],
         [1, "Stonecunning"],
         [1, "Dwarven Toughness"]
     ]
    ],
    ["Dwarf", "Mountain Dwarf",
     [{"CON": 2, "STR": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Dwarven Resilience"],
         [1, "Dwarven Combat Training"],
         [1, "Tool Proficiency"],
         [1, "Stonecunning"],
         [1, "Dwarven Armor Training"]
     ]
    ],
    ["Dwarf", "Mark of Warding Dwarf",
     [{"CON": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Dwarven Resilience"],
         [1, "Dwarven Combat Training"],
         [1, "Tool Proficiency"],
         [1, "Stonecunning"],
         [1, "Warder's Intuition"],
         [1, "Wards and Seals"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Duergar", "Duergar",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 120"],
         [3, "Duergar Magic"],
         [1, "Dwarven Resilience"],
         [1, "Psionic Fortitude"]
     ]
    ],
    ["Duergar", "Duergar",
     [{"CON": 2, "STR": 1}],
     [
         [1, "Superior Darkvision- 120"],
         [1, "Duergar Resilience"],
         [1, "Dwarven Combat Training"],
         [1, "Tool Proficiency"],
         [1, "Stonecunning"],
         [3, "Duergar Magic"],
         [1, "Sunlight Sensitivity"]
     ]
    ]
]

elf_subrace_list = [
    ["Elf", "Dark Elf",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Superior Darkvision- 120"],
         [1, "Sunlight Sensitivity"],
         [1, "Drow Magic"],
         [1, "Drow Weapon Training"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"]
     ]
    ],
    ["Elf", "High Elf",
     [{"DEX": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Cantrip"],
         [1, "Elf Weapon Training"],
         [1, "Extra Language"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"]
     ]
    ],
    ["Elf", "Wood Elf",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Elf Weapon Training"],
         [1, "Fleet of Foot"],
         [1, "Mask of the Wild"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"]
     ]
    ],
    ["Elf", "Pallid Elf",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Incisive Sense"],
         [1, "Blessing of the Moonweaver"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"]
     ]
    ],
    ["Elf", "Mark of Shadow Elf",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Cunning Intuition"],
         [1, "Shape Shadows"],
         [1, "Spells of the Mark"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"]
     ]
    ],
    ["Eladrin", "Placeholder",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Fey Step"],
         [1, "Keen Senses"],
         [1, "Trance"]
     ]
    ],
    ["Eladrin", "Placeholder",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"],
         [1, "Fey Step"]
     ]
    ],
    ["Sea Elf", "Sea Elf",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Child of the Sea"],
         [1, "Fey Ancestry"],
         [1, "Friend of the Sea"],
         [1, "Keen Senses"],
         [1, "Trance"]
     ]
    ],
    ["Sea Elf", "Sea Elf",
     [{"DEX": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"],
         [1, "Sea Elf Training"],
         [1, "Child of the Sea"],
         [1, "Friend of the Sea"]
     ]
    ],
    ["Shadar-Kai", "Shadar-Kai",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Blessing of the Raven Queen"],
         [1, "Fey Ancestry"],
         [1, "Keen Senses"],
         [1, "Necrotic Resistance"],
         [1, "Trance"]
     ]
    ],
    ["Shadar-Kai", "Shadar-Kai",
     [{"DEX": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Trance"],
         [1, "Keen Senses"],
         [1, "Necrotic Resistance"],
         [1, "Blessing of the Raven Queen"]
     ]
    ]
]

firbolg_subrace_list = [
    ["Firbolg", "Firbolg",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Firbolg Magic"],
         [1, "Hidden Step"],
         [1, "Powerful Build"],
         [1, "Speech of Beast and Leaf"]
     ]
    ],
    ["Firbolg", "Firbolg",
     [{"WIS": 2, "STR": 1}],
     [
         [1, "Firbolg Magic"],
         [1, "Hidden Step"],
         [1, "Powerful Build"],
         [1, "Speech of Beast and Leaf"]
     ]
    ]
]

genasi_subrace_list = [
    ["Air Genasi", "Air Genasi",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Unending Breath"],
         [1, "Lightning Resistance"],
         [1, "Mingle with the Wind"]
     ]
    ],
    ["Air Genasi", "Air Genasi",
     [{"CON": 2, "DEX": 1}],
     [
         [1, "Unending Breath"],
         [1, "Mingle with the Wind"]
     ]
    ],
    ["Earth Genasi", "Earth Genasi",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Earth Walk"],
         [1, "Merge with Stone"]
     ]
    ],
    ["Earth Genasi", "Earth Genasi",
     [{"CON": 2, "STR": 1}],
     [
         [1, "Earth Walk"],
         [1, "Merge with Stone"]
     ]
    ],
    ["Fire Genasi", "Fire Genasi",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fire Resistance"],
         [1, "Reach to the Blaze"]
     ]
    ],
    ["Fire Genasi", "Fire Genasi",
     [{"CON": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fire Resistance"],
         [1, "Reach to the Blaze"]
     ]
    ],
    ["Water Genasi", "Water Genasi",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Acid Resistance"],
         [1, "Amphibious"],
         [1, "Call to the Wave"]
     ]
    ],
    ["Water Genasi", "Water Genasi",
     [{"WIS": 1}],
     [
         [1, "Acid Resistance"],
         [1, "Amphibious"],
         [1, "Call to the Wave"]
     ]
    ]
]

githyanki_subrace_list = [
    ["Githyanki", "Githyanki",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Astral Knowledge"],
         [1, "Githyanki Psionics"],
         [1, "Psychic Resilience"]
     ]
    ],
    ["Githyanki", "Githyanki",
     [{"STR": 2, "INT": 1}],
     [
         [1, "Decadent Mastery"],
         [1, "Martial Prodigy"],
         [1, "Githyanki Psionics"]
     ]
    ]
]

githzerai_subrace_list = [
    ["Githzerai", "Githzerai",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Githzerai Psionics"],
         [1, "Mental Discipline"],
         [1, "Psychic Resilience"]
     ]
    ],
    ["Githzerai", "Githzerai",
     [{"WIS": 2, "INT": 1}],
     [
         [1, "Mental Discipline"],
         [1, "Githzerai Psionics"]
     ]
    ]
]

gnome_subrace_list = [
    ["Gnome", "Forest Gnome",
     [{"INT": 2, "DEX": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Gnome Cunning"],
         [1, "Natural Illusionist"],
         [1, "Speak with Small Beasts"]
     ]
    ],
    ["Gnome", "Rock Gnome",
     [{"INT": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Gnome Cunning"],
         [1, "Artificer's Lore"],
         [1, "Tinker"]
     ]
    ],
    ["Gnome", "Mark of Scribing Gnome",
     [{"INT": 2, "CHA": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Gnome Cunning"],
         [1, "Gifted Scribe"],
         [1, "Scribe's Insight"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Deep Gnome", "Deep Gnome",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 120"],
         [3, "Gift of the Svirfneblin"],
         [1, "Gnomish Magic Resistance"],
         [1, "Svirfneblin Camouflage"]
     ]
    ],
    ["Deep Gnome", "Deep Gnome",
     [{"INT": 2, "DEX": 1}],
     [
         [1, "Superior Darkvision- 120"],
         [1, "Gnome Cunning"],
         [1, "Stone Camouflage"]
     ]
    ]
]

goblin_subrace_list = [
    ["Goblin", "Goblin",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Fury of the Small"],
         [1, "Nimble Escape"]
     ]
    ],
    ["Goblin", "Goblin",
     [{"DEX": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fury of the Small"],
         [1, "Nimble Escape"]
     ]
    ],
    ["Goblin", "Goblin",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Speak with Small Beasts"],
         [1, "Nimble Escape"]
     ]
    ]
]

goliath_subrace_list = [
    ["Goliath", "Goliath",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Little Giant"],
         [1, "Mountain Born"],
         [1, "Stone's Endurance"]
     ]
    ],
    ["Goliath", "Goliath",
     [{"STR": 2, "CON": 1}],
     [
         [1, "Natural Athlete"],
         [1, "Stone's Endurance"],
         [1, "Powerful Build"],
         [1, "Mountain Born"]
     ]
    ]
]

halfelf_subrace_list = [
    ["Half Elf", "Half Elf",
     [{"CHA": 2, "custom_stat_1": 1, "custom_stat_2": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Placeholder"]
     ]
    ],
    ["Half Elf", "Mark of Detection Half Elf",
     [{"WIS": 2, "custom_stat_1": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Deductive Intuition"],
         [1, "Magical Detection"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Half Elf", "Mark of Storm Half Elf",
     [{"CHA": 2, "DEX": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Windwright's Intuition"],
         [1, "Storm's Boon"],
         [1, "Headwinds"],
         [1, "Spells of the Mark"]
     ]
    ]
]

halfling_subrace_list = [
    ["Halfling", "Lightfoot Halfling",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Lucky"],
         [1, "Brave"],
         [1, "Nimble"],
         [1, "Naturally Stealthy"]
     ]
    ],
    ["Halfling", "Stout Halfling",
     [{"DEX": 2, "CON": 1}],
     [
         [1, "Lucky"],
         [1, "Brave"],
         [1, "Nimble"],
         [1, "Stout Resilience"]
     ]
    ],
    ["Halfling", "Ghostwise Halfling",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Lucky"],
         [1, "Brave"],
         [1, "Nimble"],
         [1, "Silent Speech"]
     ]
    ],
    ["Halfling", "Lotusden Halfling",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Lucky"],
         [1, "Brave"],
         [1, "Nimble"],
         [1, "Children of the Woods"],
         [1, "Timberwalk"]
     ]
    ],
    ["Halfling", "Mark of Hospitality Halfling",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Lucky"],
         [1, "Brave"],
         [1, "Nimble"],
         [1, "Ever Hospitable"],
         [1, "Innkeeper's Magic"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Halfling", "Mark of Healing Halfling",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Lucky"],
         [1, "Brave"],
         [1, "Nimble"],
         [1, "Medical Intuition"],
         [1, "Healing Touch"],
         [1, "Spells of the Mark"]
     ]
    ]
]

halforc_subrace_list = [
    ["Half Orc", "Half Orc",
     [{"STR": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Menacing"],
         [1, "Relentless Endurance"],
         [1, "Savage Attacks"]
     ]
    ],
    ["Half Orc", "Mark of Finding Half Orc",
     [{"WIS": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hunter's Intuition"],
         [1, "Finder's Magic"],
         [1, "Spells of the Mark"]
     ]
    ]
]

hobgoblin_subrace_list = [
    ["Hobgoblin", "Hobgoblin",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Fey Ancestry"],
         [1, "Fey Gift"],
         [1, "Fortune from the Many"]
     ]
    ],
    ["Hobgoblin", "Hobgoblin",
     [{"CON": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Martial Training"],
         [1, "Saving Face"]
     ]
    ]
]

human_subrace_list = [
    ["Human", "Human",
     [{"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}],
     [
         [21, "None"]
     ]
    ],
    ["Human", "Mark of Finding Human",
     [{"WIS": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hunter's Intuition"],
         [1, "Finder's Magic"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Human", "Mark of Handling Human",
     [{"WIS": 2, "custom_stat_1": 1}],
     [
         [1, "Wild Intuition"],
         [1, "Primal Connection"],
         [1, "The Bigger They Are"],
         [3, "The Bigger They Are"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Human", "Mark of Making Human",
     [{"INT": 2, "custom_stat_1": 1}],
     [
         [1, "Artisan's Intuition"],
         [1, "Artisan's Gift"],
         [1, "Spellsmith"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Human", "Mark of Passage Human",
     [{"DEX": 2, "custom_stat_1": 1}],
     [
         [1, "Intuitive Motion"],
         [1, "Magical Passage"],
         [1, "Spells of the Mark"]
     ]
    ],
    ["Human", "Mark of Sentinel Human",
     [{"CON": 2, "WIS": 1}],
     [
         [1, "Sentinel's Intuition"],
         [1, "Guardian's Shield"],
         [1, "Vigilant Guardian"],
         [1, "Spells of the Mark"]
     ]
    ]
]

kenku_subrace_list = [
    ["Kenku", "Kenku",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Expert Duplication"],
         [1, "Kenku Recall"],
         [1, "Mimicry"]
     ]
    ],
    ["Kenku", "Kenku",
     [{"DEX": 2, "WIS": 1}],
     [
         [1, "Expert Forgery"],
         [1, "Kenku Training"],
         [1, "Mimicry"]
     ]
    ]
]

kobold_subrace_list = [
    ["Kobold", "Kobold",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Draconic Cry"],
         [1, "Placeholder"]
     ]
    ],
    ["Kobold", "Kobold",
     [{"DEX": 2}],
     [
         [1, "Darkvision- 60"],
         [1, "Grovel, Cower, and Beg"],
         [1, "Pack Tactics"],
         [1, "Sunlight Sensitivity"]
     ]
    ]
]

lizardfolk_subrace_list = [
    ["Lizardfolk", "Lizardfolk",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Bite"],
         [1, "Hold Breath"],
         [1, "Hungry Jaws"],
         [1, "Natural Armor"],
         [1, "Nature's Intuition"]
     ]
    ],
    ["Lizardfolk", "Lizardfolk",
     [{"CON": 2, "WIS": 1}],
     [
         [1, "Bite"],
         [1, "Cunning Artisan"],
         [1, "Hold Breath"],
         [1, "Hunter's Lore"],
         [1, "Natural Armor"],
         [1, "Hungry Jaws"]
     ]
    ]
]

minotaur_subrace_list = [
    ["Minotaur", "Minotaur",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Horns"],
         [1, "Goring Rush"],
         [1, "Hammering Horns"],
         [1, "Labyrinthine Recall"]
     ]
    ],
    ["Minotaur", "Minotaur",
     [{"STR": 2, "CON": 1}],
     [
         [1, "Horns"],
         [1, "Goring Rush"],
         [1, "Hammering Horns"],
         [1, "Imposing Presence"]
     ]
    ]
]

orc_subrace_list = [
    ["Orc", "Orc",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Adrenaline Rush"],
         [1, "Powerful Build"],
         [1, "Relentless Endurance"]
     ]
    ],
    ["Orc", "Orc",
     [{"STR": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Aggressive"],
         [1, "Primal Intuition"],
         [1, "Powerful Build"]
     ]
    ],
    ["Orc", "Orc",
     [{"STR": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Menacing"],
         [1, "Relentless Endurance"],
         [1, "Savage Attacks"]
     ]
    ]
]

satyr_subrace_list = [
    ["Satyr", "Satyr",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Ram"],
         [1, "Magic Resistance"],
         [1, "Mirthful Leaps"],
         [1, "Reveler"],
         [1, "Languages- Common/Other"]
     ]
    ],
    ["Satyr", "Satyr",
     [{"CHA": 2, "DEX": 1}],
     [
         [1, "Ram"],
         [1, "Magic Resistance"],
         [1, "Mirthful Leaps"],
         [1, "Reveler"],
         [1, "Languages- Common/Sylvan"]
     ]
    ]
]

shifter_subrace_list = [
    ["Shifter", "Shifter",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Bestial Instincts"],
         [1, "Placeholder"]
     ]
    ],
    ["Shifter", "Beasthide",
     [{"CON": 2, "STR": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Keen Senses"],
         [1, "Shifting"],
         [1, "Natural Athlete"],
         [1, "Shifting Feature"]
     ]
    ],
    ["Shifter", "Longtooth",
     [{"STR": 2, "DEX": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Bestial Instincts"],
         [1, "Shifting"],
         [1, "Fierce"],
         [1, "Shifting Feature"]
     ]
    ],
    ["Shifter", "Swiftstride",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Bestial Instincts"],
         [1, "Shifting"],
         [1, "Graceful"],
         [1, "Shifting Feature"]
     ]
    ],
    ["Shifter", "Wildhunt",
     [{"WIS": 2}],
     [
         [1, "Darkvision- 60"],
         [1, "Bestial Instincts"],
         [1, "Shifting"],
         [1, "Mark the Scent"],
         [1, "Shifting Feature"]
     ]
    ]
]

tabaxi_subrace_list = [
    ["Tabaxi", "Tabaxi",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Cat's Claws"],
         [1, "Cat's Talent"],
         [1, "Feline Agility"]
     ]
    ],
    ["Tabaxi", "Tabaxi",
     [{"DEX": 2, "CHA": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Cat's Claws"],
         [1, "Cat's Talent"],
         [1, "Feline Agility"]
     ]
    ]
]

tiefling_subrace_list = [
    ["Tiefling", "Bloodline of Asmodeus Tiefling",
     [{"CHA": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Infernal Legacy"]
     ]
    ],
    ["Tiefling", "Bloodline of Baalzebul Tiefling",
     [{"CHA": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Maladomini"]
     ]
    ],
    ["Tiefling", "Bloodline of Dispater Tiefling",
     [{"CHA": 2, "DEX": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Dis"]
     ]
    ],
    ["Tiefling", "Bloodline of Fierna Tiefling",
     [{"CHA": 2, "WIS": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Phlegethos"]
     ]
    ],
    ["Tiefling", "Bloodline of Glasya Tiefling",
     [{"CHA": 2, "DEX": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Malbolge"]
     ]
    ],
    ["Tiefling", "Bloodline of Levistus Tiefling",
     [{"CHA": 2, "CON": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Stygia"]
     ]
    ],
    ["Tiefling", "Bloodline of Mammon Tiefling",
     [{"CHA": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Minauros"]
     ]
    ],
    ["Tiefling", "Bloodline of Mephistopheles Tiefling",
     [{"CHA": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Cania"]
     ]
    ],
    ["Tiefling", "Bloodline of Zariel Tiefling",
     [{"CHA": 2, "STR": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Hellish Resistance"],
         [1, "Legacy of Avernus"]
     ]
    ]
]

tortle_subrace_list = [
    ["Tortle", "Tortle",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Claws"],
         [1, "Hold Breath"],
         [1, "Natural Armor"],
         [1, "Nature's Intuition"],
         [1, "Shell Defense"]
     ]
    ],
    ["Tortle", "Tortle",
     [{"STR": 2, "WIS": 1}],
     [
         [1, "Claws"],
         [1, "Hold Breath"],
         [1, "Natural Armor"],
         [1, "Shell Defense"],
         [1, "Survival Instinct"]
     ]
    ]
]

triton_subrace_list = [
    ["Triton", "Triton",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Amphibious"],
         [1, "Control Air and Water"],
         [1, "Emissary of the Sea"],
         [1, "Guardians of the Depths"]
     ]
    ],
    ["Triton", "Triton",
     [{"STR": 1, "CON": 1, "CHA": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Amphibious"],
         [1, "Control Air and Water"],
         [1, "Emissary of the Sea"],
         [1, "Guardians of the Depths"]
     ]
    ]
]

yuanti_subrace_list = [
    ["Yuan-Ti", "Yuan-Ti",
     [{"custom_stat_1": 2, "custom_stat_2": 1}, {"custom_stat_1": 1, "custom_stat_2": 1, "custom_stat_3": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Magic Resistance"],
         [1, "Poison Resilience"],
         [1, "Serpentine Spellcasting"]
     ]
    ],
    ["Yuan-Ti", "Yuan-Ti",
     [{"CHA": 2, "INT": 1}],
     [
         [1, "Darkvision- 60"],
         [1, "Innate Spellcasting"],
         [1, "Magic Resistance"],
         [1, "Poison Immunity"]
     ]
    ]
]