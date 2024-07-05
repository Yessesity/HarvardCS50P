import csv
from tabulate import tabulate
import sys

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            menu = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append(row)
            headers = menu[0]
            table = menu[1:]
            print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
