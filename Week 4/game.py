import random
import sys

def main():
    try:
        while True:
            level = int(input("Level: "))
            if level <= 0:
                pass
            else:
                correct = random.randint(1, level)
                break
    except ValueError:
        pass
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                pass
            else:
                if check(guess, correct):
                    sys.exit()
        except ValueError:
            pass

def check(n, c):
    if n < c:
        print("Too small!")
        return False
    elif n > c:
        print("Too Large!")
        return False
    else:
        print("Just right!")
        return True

main()
