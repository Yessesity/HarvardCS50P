def main():
    ans = input("What is the answer to the great questions of life, the universe, and everything? ")

    match ans.strip().lower():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")
            
main()