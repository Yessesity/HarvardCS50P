class Student:
    #attribute=None in order to make attribute optional
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Rusell Terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print(f"{student}\nPatronus:\nExpecto Patronum!\n{student.charm()}")


def get_student():
    name = input("What's your name? ")
    house = input("What's your house? ")
    patronus = input("What's your patronus? ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()