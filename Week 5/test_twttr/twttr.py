import re


def main():
    twttr = input("Input: ")
    print(f"Output: {shorten(twttr)}")


def shorten(word):
    return re.sub(r"[aeiou]", "", word, flags=re.IGNORECASE).strip()


if __name__ == "__main__":
    main()
