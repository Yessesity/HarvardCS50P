import csv


class Char:
    def __init__(self, name):
        self.name = name.lower().replace(" ", "")

    def write(self):    
        with open(f"CS_{self.name}.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["name", self.name])

    @classmethod
    def get_name(cls):
        ans = input("Welcome to DND! Do you already have a character? (y/n)\n")
        if ans == "n":
            while True:
                name = input("ATTENTION: Max character length 12\nInput Character Name: ")
                if len(name) > 12:
                    print("Too many characters! Try again")
                else:
                    return cls(name)
        else:
            name = input("Input Character Name: ")
            cls(name)
        #ask what character name, open csv of that character name
        ...