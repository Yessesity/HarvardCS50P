import csv


class CharWrite:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def write(self, binary):
        if binary != "n":
            return
        with open(f"charsheet_{self.name}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", self.name])

    def has_char():
        binary = input("Welcome to DND! Do you already have a character? (y/n)\n")
        return binary

    @classmethod
    def get_name(cls, binary):
        if binary != "n":
            name = input("Input Character Name: ").lower().replace(" ", "")
            return cls(name)
        else:
            while True:
                name = input("ATTENTION: Max character length 12\nInput Character Name: ").lower().replace(" ", "")
                if len(name) > 12:
                    print("Too many characters! Try again")
                else:
                    return cls(name)
