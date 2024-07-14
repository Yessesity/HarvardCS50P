def main():
    yell("this", "is", "cs50")


def yell(*words):
    #takes in any function, and applies the effect of
    #that function to every member of something
    #you can also use python default functions
    #like str.upper
    uppercased = map(cased, words)
    print(*uppercased)


def cased(word):
    return word.upper()


if __name__ == "__main__":
    main()