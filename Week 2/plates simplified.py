def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 2 and len(s) <= 6:
        if '.' in s or ',' in s:
            return False
        for i in range(1, len(s) - 1):
            if s[i].isalpha():
                if s[i - 1].isdigit() and s[i + 1].isdigit():
                    return False
        if s[2:].startswith("0"):
            return False
        if s[0:2].isalpha():
            return True

main()
