def main():
    fuel_level = get_input("Fraction: ")
    gauge(fuel_level)

def get_input(prompt):
        while True:
            try:
                x, y = input(prompt).split("/")
                return int(round((int(x)/int(y))*100))
            except (ValueError, ZeroDivisionError):
                pass

def gauge(f):
    if f <= 1:
        print("E")
    elif f > 100:
        main()
    elif f >= 99:
        print("F")
    else:
        print(f"{f}%")

main()
