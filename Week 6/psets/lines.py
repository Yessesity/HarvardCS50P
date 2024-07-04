import sys


def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        else:
            print(count_lines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(code):
    lines = []
    with open(code) as file:
        for line in file:
            if line.strip().startswith("#"):
                pass
            elif line.isspace():
                pass
            else:
                lines.append(line)
    return len(lines)


if __name__ == "__main__":
    main()
