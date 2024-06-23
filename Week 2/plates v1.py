def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) == 4:
        mid = len(s)//2
        if s[:mid].isalpha():
            return True

main()
