import random


def hundred_number_generator():
    return random.randrange(1,101)


def back_in_time_generator():
    random_number = hundred_number_generator()
    if random_number >= 1 and random_number <= 25:
        return (
            random.randrange(1,8),
            "days back"
        )
    elif random_number >= 26 and random_number <= 50:
        return (
            random.randrange(1,5),
            "weeks back"
        )
    elif random_number >= 51 and random_number <= 75:
        return (
            random.randrange(1,13),
            "months back"
        )
    else:
        return(
            random.randrange(1,21),
            "years back"
        )


def current_time_generator():
    random_number = hundred_number_generator()
    if random_number >= 1 and random_number <= 25:
        return (
            random.randrange(1,25),
            "hours back"            
        )
    elif random_number >= 26 and random_number <= 50:
        return (
            random.randrange(1,61),
            "minutes back"
        )
    elif random_number >= 51 and random_number <= 75:
        return (
            random.randrange(1,61),
            "minutes forward"
        )
    else:
        return (
            random.randrange(1,25),
            "hours forward"
        )


def future_time_generator():
    random_number = hundred_number_generator()
    if random_number >= 1 and random_number <= 25:
        return (
            random.randrange(1,8),
            "days forward"
        )
    elif random_number >= 26 and random_number <= 50:
        return (
            random.randrange(1,5),
            "weeks forward"
        )
    elif random_number >= 51 and random_number <= 75:
        return (
            random.randrange(1,13),
            "months forward"
        )
    else:
        return(
            random.randrange(1,21),
            "years forward"
        )


def __main__():
    input("Press enter to roll on the Faewild time skip chart!")
    result = hundred_number_generator()
    if result >= 1 and result <= 33:
        answer = back_in_time_generator()
        print (f"You've been sent {answer[0]} {answer[1]}!")
    elif result >= 34 and result <= 66:
        answer = current_time_generator()
        print (f"You've been sent {answer[0]} {answer [1]}!")
    else:
        answer = future_time_generator()
        print(f"You've been sent {answer[0]} {answer[1]}!")


if __name__ == "__main__":
    __main__()