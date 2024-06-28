import random

def main():
    result = random.choice(["heads", "tails"])
    print(result)

    result1 = random.randint(1, 10)
    print(f"\n{result1}\n")

    cards = ["jack", "queen", "king", "ace", "joker"]

    random.shuffle(cards)

    for card in cards:
        print(card)

main()
