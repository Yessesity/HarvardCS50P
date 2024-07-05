import sys
from PIL import Image, ImageOps


def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
            sys.exit("Invalid Input")
        elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
            sys.exit("Invalid Output")
        elif not same_file_extension():
            sys.exit("Input and output have different extensions")
        else:
            shirt = Image.open("shirt.png")
            person = Image.open(sys.argv[1])
            person = ImageOps.fit(person, shirt.size)
            person.paste(shirt, shirt)
            person.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def same_file_extension():
    return sys.argv[1].split(".")[-1] == sys.argv[2].split(".")[-1]


if __name__ == "__main__":
    main()
