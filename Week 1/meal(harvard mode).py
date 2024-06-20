def main():
    time = input("What time is it? ")
    if convert(time) >= 18:
        print("dinner time")
    elif convert(time) >= 12:
        print("lunch time")
    else:
        print("breakfast time")

def convert(t):
    hours, minutes = t.split(":")
    return float(hours) + float(minutes)/60

if __name__ == "__main__":
    main()