import csv
import sys


def main():
    binary = get()
    if binary == "n":
        work = 25
        rest = 5
    elif binary == "y":
        try:
            work, rest = get_durations()
            write_durations(work, rest)
        except TypeError:
            work, rest = reader()
    print(f"Work Duration: {work}, Rest Duration {rest}")


def get() -> str:
    print("-" * 60, "\nWelcome to the Configurable Pomodoro Timer!\n", "-" * 60, sep="")
    binary = (
        input(
            "Do you want to configure your own work duration and break duration? (if no, stick with default values) (y/n)\n"
        )
        .lower()
        .strip()
    )
    if binary not in ["y", "n"]:
        sys.exit("Invalid Answer")
    return binary


def get_durations() -> int:
    bin = (
        input(
            "Would you like to open an existing config.csv? (if no, edit config.csv) (y/n)\n"
        )
        .lower()
        .strip()
    )
    if bin not in ["y", "n"]:
        sys.exit("Invalid answer")
    if bin == "y":
        raise TypeError
    while True:
        try:
            print("-" * 60)
            work = int(
                input(
                    "NOTE: Only put in numbers with no words\nInput the duration (in minutes) for work:\n"
                ).strip()
            )
            rest = int(
                input("Input the duration (in minutes) of your desired rest:\n").strip()
            )
            if work > 60 or rest > 60:
                print("-" * 60, "\nInvalid input/s, try again")
                pass
            else:
                return work, rest
        except ValueError:
            pass


def write_durations(wrk: int, rst: int):
    with open("config.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["work", wrk])
        writer.writerow(["rest", rst])


def reader() -> tuple:
    temp = []
    with open(f"config.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            temp.append(row)
    work = temp[0][1]
    rest = temp[1][1]
    return work, rest


if __name__ == "__main__":
    main()
