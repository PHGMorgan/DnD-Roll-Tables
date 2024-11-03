# Range: 1-20. Change this to change the max level a rolled character can be.
max_char_level = 20

# Lower values makes higher levels more likely
char_level_odds = 1.35

# Chance for a rolled character to be a Commoner. Higher values make commoners more likely.
commoner_chance = 1

# Chance for a rolled character to have a shield if eligible. Odds are 1 in 10/number selected. E.g. 100 = 1 in 10, 90 = 1 in 9, 80 = 1 in 8, etc.
shield_chance = 50

# Chance for each of the race types to appear. Higher numbers = higher chance for that race type to appear.
common_races_odds = 7
exotic_races_odds = 2
monstrous_race_odds = 1


# Do not alter the below fields.
stat_mod_dict = {1:-5,2:-4,3:-4,4:-3,5:-3,6:-2,7:-2,8:-1,9:-1,10:0,11:0,12:1,13:1,14:2,15:2,16:3,17:3,18:4,19:4,20:5}
class_odds_list = [1, 1, 1, 1, commoner_chance, 1, 1, 1, 1, 1, 1, 1, 1, 1]
stat_names_list = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
c, e, m = common_races_odds, exotic_races_odds, monstrous_race_odds
race_weights = [e, e, m, m, e, c, c, c, e, e, e, e, e, c, m, e, m, c, c, c, e, m, c, e, m, m, m, m, e, e, m, e, c, e, e, e, m]
# total common races: 9
# total exotic races: 17
# total monstrous races: 11