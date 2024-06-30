import random


def main():
    level = get_level()
    question_number = 1
    total_guess = 0

    while question_number != 10:
        x = generate_integer(level)
        y = generate_integer(level)
        ans = int(input(f"{x} + {y} = "))
        if ans == x + y:
            question_number += 1
        elif ans != x + y:
            print("EEE")
            guess = 1
            while True:
                ans = int(input(f"{x} + {y} = "))
                if ans == x+y:
                    question_number += 1
                    total_guess += guess
                    break
                if ans != x+y:
                    print("EEE")
                    guess += 1
                if guess == 3:
                    print(f"{x} + {y} = {x+y}")
                    total_guess += guess
                    break
    if question_number == 10:
        score = 10 - total_guess
        print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level !=3:
                pass
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
