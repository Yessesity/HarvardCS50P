import csv
import sys


def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            student_list = []
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list.append(row)
            for name in student_list:
                last_name, first_name = name["name"].replace(" ", "").split(",")
                name["name"] = f"{first_name} {last_name}"
            with open(sys.argv[2], "a") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "house"])
                writer.writeheader()
                for row in student_list:
                    writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
