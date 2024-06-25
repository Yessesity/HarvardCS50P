def main():
    i = 50
    print(f"Amount Due: {i}")
    while True:
        c = int(input("Insert coin: "))
        if c == 25 or c == 10 or c == 5 or c == 50:
            i = i - c
            if i > 0:
                print(f"Amount Due: {i}")
        else:
            print(f"Amount Due: {i}")
        if i <= 0:
            print(f"Change Owed: {-i}")
            break

main()
