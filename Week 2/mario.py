def main():
    print_square(3)

def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end=" ")
        print()

main()