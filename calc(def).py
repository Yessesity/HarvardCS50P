def main():
    x = int(input("What's x? "))
    print(f"x squared is {square(x)}")

def square(x):
    return pow(x, 2)

main()