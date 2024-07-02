def main():
    while True:
        try:
            fuel_level = input("Fraction: ")
            number = convert(fuel_level)
            print(gauge(number))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(prompt):
    if prompt.isalpha():
        raise ValueError
    else:
        x, y = prompt.split("/")
        if int(y) == 0:
            raise ZeroDivisionError
        elif int(x) > int(y):
            raise ValueError
        else:
            return round((int(x)/int(y))*100)


def gauge(f):
    if f <= 1:
        return "E"
    elif f >= 99:
        return "F"
    else:
        return f"{f}%"


if __name__ == "__main__":
    main()
