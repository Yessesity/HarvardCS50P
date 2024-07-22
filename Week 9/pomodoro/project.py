import csv
import sys
import time

from playsound import playsound

DEFAULT_WORK = 25
DEFAULT_REST = 5
DEFAULT_LONG_REST = 15

def main():
    binary = get()
    work, rest, long_rest = get_work_rest(binary)
    cycle = 0
    while cycle < 4:
        cycle += 1
        timer_interface(work, f"\nTime to start working! Type 'start' to initialize the timer. Cycle: {cycle}")
        playsound("alarm.mp3")
        if cycle < 4:
            timer_interface(rest, "\nTime to rest! Type 'start' to initialize rest timer.")
        else:
            timer_interface(long_rest, "\nTime to get a long rest! Type 'start' to initialize long rest timer.")
        playsound("alarm.mp3")
        if cycle == 4:
            cycle -= 4
        if not repeat():
            return
        

def get_work_rest(binary) -> tuple[int, int, int]:
    if binary == "n":
        return DEFAULT_WORK, DEFAULT_REST, DEFAULT_LONG_REST
    elif binary == "y":
        try:
            work, rest, long_rest = get_durations()
            write_durations(work, rest, long_rest)
        except TypeError:
            work, rest, long_rest = reader()
        return work, rest, long_rest
        

def repeat() -> bool:
    while True:
        binary = input("Do 1 more set of Pomodoro? (y/n)\n").lower().strip()
        if binary == "y":
            return True
        elif binary == "n":
            return False


def timer_interface(time, text):
    print("-" * 60, text)
    while True:
        start = input("").lower().strip()
        if start != "start":
            pass
        else:
            print("Starting timer...")
            countdown(int(time)*60)
            return


def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = "{:02d}:{:02d}".format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print("Times up!") 



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


def get_durations() -> tuple[int, int, int]:
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
            long_rest = int(
                input("Input the duration (in minutes) of your desired long rest:\n").strip()
            )
            if any(x > 60 or x <= 0 for x in (work, rest, long_rest)):
                print("-" * 60, "\nInvalid input/s, try again")
                continue
            else:
                return work, rest, long_rest
        except ValueError:
            pass


def write_durations(wrk: int, rst: int, lngrst: int) -> None:
    with open("config.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["work", wrk])
        writer.writerow(["rest", rst])
        writer.writerow(["long rest", lngrst])


def reader() -> tuple[int, int, int]:
    temp = []
    try:
        with open(f"config.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                temp.append(row)
        work = temp[0][1]
        rest = temp[1][1]
        long_rest = temp[2][1]
        return work, rest, long_rest
    except Exception:
        print("Error reading config.csv, using default values instead")
        return DEFAULT_WORK, DEFAULT_REST, DEFAULT_LONG_REST


if __name__ == "__main__":
    main()
