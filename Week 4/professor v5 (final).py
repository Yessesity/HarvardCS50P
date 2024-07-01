import random


def main():
    level = get_level()
    question_number: int = 0
    incorrect: int = 0

    while question_number != 10:
        x = generate_integer(level)
        y = generate_integer(level)
        ans = generate_question(x, y)
        if correct_answer(x, y, ans):
            question_number += 1
        elif incorrect_answer(x, y, ans):
            print("EEE")
            guess: int = 1
            while True:
                ans = generate_question(x, y)
                if correct_answer(x, y, ans):
                    question_number += 1
                    break
                if incorrect_answer(x, y, ans):
                    print("EEE")
                    guess += 1
                if guess == 3:
                    generate_correct_ans(x, y)
                    incorrect += 1
                    question_number += 1
                    break

    check_score(incorrect)


def check_score(x):
    score = 10 - x
    print(f"Score: {score}")


def correct_answer(x, y, ans):
    return ans == x + y


def incorrect_answer(x, y, ans):
    return ans != x + y


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                pass
            else:
                return level
        except ValueError:
            pass


def generate_question(x, y):
    return int(input(f"{x} + {y} = "))


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def generate_correct_ans(x, y):
    return print(f"{x} + {y} = {x+y}")


if __name__ == "__main__":
    main()

