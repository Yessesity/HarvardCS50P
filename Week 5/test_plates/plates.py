def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    if len(string) not in [2, 3, 4, 5, 6]:
        return False
    if '.' in string or ',' in string:
        return False
    if letter_inbetween_num(string):
        return False
    if number_inbetween_let(string):
        return False
    if string[2:].startswith("0"):
        return False
    if string[0].isdigit():
        return False
    if string[1].isdigit():
        return False
    if not string.isalnum():
        return False
    else:
        return True

def letter_inbetween_num(string):
    for i in range(1, len(string) - 1):
        if string[i].isalpha():
            if string[i - 1].isdigit() and string[i + 1].isdigit():
                return True


def number_inbetween_let(string):
    for i in range(1, len(string) - 1):
        if string[i].isdigit():
            if string[0].isalpha() and string[-1].isalpha():
                return True


if __name__ == "__main__":
    main()
