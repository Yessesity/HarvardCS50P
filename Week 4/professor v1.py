import random


def main():
    level = get_level()
    question_list = {}
    question_number = 1
    guess = 1

    for q in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        equation = f"{x} + {y} = "
        result = x + y
        question_list[equation] = result

    for question in question_list:
        print(question_list[question])


def get_level():
    while True:
        level = int(input("Level: "))
        if level != 1 and level != 2 and level !=3:
            raise ValueError
        else:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10-99)
    else:
        return random.randint(100-999)


if __name__ == "__main__":
    main()
