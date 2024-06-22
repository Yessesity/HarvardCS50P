import re

def main():
    string = [input("camelCase: ")]

    for s in string:
        print(f"snake_case: {split_on_capitals(s)}")


def split_on_capitals(s):
    #adds a space before every capital letter.
    return re.sub(r"([A-Z])", r" \1", s).strip().replace(" ", "_").lower()

main()
