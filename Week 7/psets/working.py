import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$",
        s,
        re.IGNORECASE,
    ):
        if matches.group(3) == "PM":
            if matches.group(1) == "12":
                hours = int(matches.group(1))
            else:
                hours = int(matches.group(1)) + 12
        elif matches.group(3) == "AM" and matches.group(1) == "12":
            hours = int(matches.group(1)) - 12
        else:
            hours = int(matches.group(1))
        if matches.group(6) == "PM":
            if matches.group(4) == "12":
                hours1 = int(matches.group(4))
            else:
                hours1 = int(matches.group(4)) + 12
        elif matches.group(6) == "AM" and matches.group(4) == "12":
            hours1 = int(matches.group(4)) - 12
        else:
            hours1 = int(matches.group(4))
        if matches.group(2):
            minutes = matches.group(2)
        else:
            minutes = "00"
        if matches.group(5):
            minutes1 = matches.group(5)
        else:
            minutes1 = "00"
        return f"{hours:02}:{minutes} to {hours1:02}:{minutes1}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
