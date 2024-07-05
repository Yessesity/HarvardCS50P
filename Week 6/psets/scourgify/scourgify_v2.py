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
            new_student_list = []
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list.append(row)
            for name in student_list:
                last_name, first_name = name["name"].replace(" ", "").split(",")
                new_student_list.append(
                    {"first": first_name, "last": last_name, "house": name["house"]}
                )
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in new_student_list:
                    writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
