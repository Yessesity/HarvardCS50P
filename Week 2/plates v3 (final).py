def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    if len(string) > 2 and len(string) <= 6:
        if '.' in string or ',' in string:
            return False
        if letter_inbetween_num(string):
            return False
        if string[2:].startswith("0"):
            return False
        if string[0:2].isalpha():
            return True

def letter_inbetween_num(string):
    for i in range(1, len(string) - 1):
        if string[i].isalpha():
            if string[i - 1].isdigit() and string[i + 1].isdigit():
                return True

main()
