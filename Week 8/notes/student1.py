def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("What's your name? ")
    student["house"] = input("What's your house? ")
    return student

#name = input("What's your name? ")
#house = input("What's your house? ")
#return {"name": name, "house": house}

#var = list(dict)
#gathers the keys in a dict



if __name__ == "__main__":
    main()