import random


scar_size = [
    "tiny",
    "small",
    "medium",
    "large",
    "huge"
]


scar_type = [
    "ropey",
    "twisted",
    "pitted",
    "faint",
    "smooth",
    "rough",
    "jagged",
    "gnarled",
    "pulled",
    "flat"
]


scar_location = [
    "face",
    "neck",
    "chest",
    "abdomen",
    "torso",
    "head",
    "jawline",
    "arms",
    "hands",
    "fingers",
    "upper arm",
    "lower arm",
    "hips",
    "back",
    "upper back",
    "lower back",
    "sides",
    "legs",
    "knees",
    "thigh",
    "lower leg",
    "foot",
    "toes"
]

severe_scar_types = {
    "missing eye": "-2 Perception when spotting by sight",
    "missing finger": "-1 Sleight of Hand",
    "missing nose": "-1 Perception when spotting by scent",
    "missing ear":  "-1 Perception when listening",
    "missing part of your nose": "-1 Perception when spotting by scent",
    "missing part of your ear": "-1 Perception when listening",
    "missing toe": "nothing",
    "missing chunk of flesh from your torso": "nothing",
    "missing chunk of flesh from your arm": "-1 Sleight of Hand",
    "missing chunk of flesh from your back": "nothing",
    "missing chunk of flesh from your leg": "-1 Athletics and Acrobatics when using your legs",
    "missing tooth": "nothing",
    "fucked up knee": "-1 Stealth",
    "fucked up elbow": "-1 Sleight of Hand",
    "fucked up shoulder": "-1 Sleight of Hand",
    "fucked up wrist": "-1 Sleight of Hand",
    "missing skull chunk": "-1 CON",
    "fucked up hip": "-1 Stealth",
    "missing ribs": "nothing",
    "damaged organ": "nothing"
}


def randnum_through_hundred():
    return random.randrange(1, 101)


def randnum_through_ten():
    return random.randrange(1, 11)


def random_fifty_fifty ():
    return random.randrange(0, 2)


def __main__():
    input("Press Enter to roll on scar chart!")
    does_char_get_scar = random_fifty_fifty()
    if does_char_get_scar == 0:
        print("You didn't get a scar this time!")
        return
    does_char_get_severe_scar = randnum_through_ten()
    if does_char_get_severe_scar == 1:
        print("You got a severe scar! Rolling on the severe scar table...")
        severe_scar_key = random.choices(list(severe_scar_types.keys()), weights = [2, 4, 4, 3, 4, 4, 7, 8, 7, 8, 8, 7, 4, 7, 7, 3, 2, 4, 5, 4], k = 1)[0]
        print(f"You now have a {severe_scar_key}. Your penalty is {severe_scar_types[severe_scar_key]}.")
        return
    scar_details = [
        random.choices(scar_size, weights = [15, 20, 30, 20, 15], k = 1)[0],
        random.choices(scar_type, k = 1)[0],
        random.choices(scar_location, weights = [4, 4, 6, 5, 7, 5, 4, 5, 2, 2, 4, 4, 4, 7, 5, 5, 5, 6, 3, 5, 4, 3, 1], k = 1)[0]
    ]
    print(f"You now have a {scar_details[0]}, {scar_details[1]} scar on your {scar_details[2]}.")


if __name__ == "__main__":
    __main__()