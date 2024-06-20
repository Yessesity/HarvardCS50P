def main():
    x = int(input("What's the value of x? "))
    if x_is_even(x):
        print("Even")
    else:
        print("Odd")

def x_is_even(n):
    return n % 2 == 0

main ()