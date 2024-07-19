import csv
import sys
import time
from playsound import playsound


def main():
    binary = get()
    work, rest = get_work_rest(binary)
    while True:
        timer_interface(work, "\nTime to start working! Type 'start' to initialize the timer.")
        playsound("alarm.mp3")
        timer_interface(rest, "\nTime to rest! Type 'start' to initialize rest timer.")
        playsound("alarm.mp3")
        if not repeat():
            return
        

def get_work_rest(binary):
    if binary == "n":
        work = 25
        rest = 5
        return work, rest
    elif binary == "y":
        try:
            work, rest = get_durations()
            write_durations(work, rest)
        except TypeError:
            work, rest = reader()
        return work, rest
        

def repeat():
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
            if work > 60 or rest > 60 or work <= 0 or rest <=0:
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
