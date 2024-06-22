def main():
    time = input("What time is it? ")
    x, y = time.split(":")
    meal(x)

def meal(t):
    if int(t) >= 18:
        print("dinner time")
    elif int(t) >= 12:
        print("lunch time")
    else:
        print("breakfast time")

main()
