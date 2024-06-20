def main():
    m = int(input("m= "))
    print(f"e= {m * squared(300000000)}")

def squared(c):
    return pow(c, 2)

main()