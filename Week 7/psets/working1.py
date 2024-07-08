import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$",
        s,
    ):
        time = set_time(matches.group(1), matches.group(2), matches.group(3))
        time1 = set_time(matches.group(4), matches.group(5), matches.group(6))
        return f"{time} to {time1}"
    else:
        raise ValueError


def set_time(hour, minute, ampm):
    if ampm == "PM":
        if hour == "12":
            hour = hour
        else:
            hour = int(hour) + 12
    elif ampm == "AM" and hour == "12":
        hour = int(hour) - 12
    else:
        hour = hour
    if minute:
        minute = minute
    else:
        minute = "00"
    return f"{int(hour):02}:{minute}"


if __name__ == "__main__":
    main()
